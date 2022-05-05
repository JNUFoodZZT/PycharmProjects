#!/bin/python
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from mpl_toolkits.mplot3d import Axes3D
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold

from sklearn.preprocessing import scale 
from sklearn import model_selection
from sklearn.cross_decomposition import PLSRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
from pandas_ml import ConfusionMatrix

from statsmodels import robust
from console import bcolors
from logger import logger
from plotter import plotter
import numpy as np
import dataset as ds
import normalization as norm
import time

class Experiment:
    def __init__(self, datasets, start=1000,end=2700,num=500):
        print('\n')
        logger.log('Initializing Experiment', color='green')

        #Start,end limit the range of frequencies to process
        #num is the number of samples for every different category
        self.start = start
        self.end = end
        self.num = num

        #for every string in self.datasets array there must be 
        #a '_train.csv', and a '_test.csv' in the ./data/ folder
        self.datasets = datasets
        self.train_data, self.train_labels = self.loadTrainDatasets()
        self.test_data , self.test_labels = self.loadTestDatasets()
        self.results=None
        print('\n')

    def stats(self):
        if self.results is not None:
            y_actu = pd.Series(self.test_labels, name='Actual')
            y_pred = pd.Series(self.results, name='Predicted')
            cm = ConfusionMatrix(y_actu, y_pred)
            cm.print_stats()

    #Loads and normalizes the testing datasets. For every sample type in 
    #self.datasets there must be a sampletype_test.csv
    def loadTestDatasets(self):
            logger.log('Loading test Dataset', color='green')

            test_data = []
            sample_num = []
            for dataset in self.datasets:
                temp = ds.loadData([dataset + '_test'],self.start,self.end)
                test_data.append(temp)
                sample_num.append(len(temp))
                logger.log(dataset + '(samples,features): ' + str(temp.shape))
            test_data = np.concatenate(test_data, axis=0)

            #use robust snv normalization on the dataset
            test_data = norm.normalizeDataset_robust(test_data,self.median,self.mad)

            logger.log('Test data(samples,features): ' + str(test_data.shape))

            #create test labels based on the test dataset
            test_labels = []
            for i,num in enumerate(sample_num):
                temp = [i for x in xrange(num)]
                test_labels.append(temp)
            test_labels = np.concatenate(test_labels, axis=0)

            return test_data,test_labels

    #Loads and normalizes the training datasets. for every sample type in 
    #self.datasets there must be a sampletype_train.csv
    def loadTrainDatasets(self):
        logger.log('Loading train Dataset', color='green')

        train_data = []
        sample_num = []
        for dataset in self.datasets:
            temp = ds.loadData([dataset + '_train'],self.start,self.end)
            train_data.append(temp)
            sample_num.append(len(temp))
            logger.log(dataset + '(samples,features): ' + str(temp.shape))
        train_data = np.concatenate(train_data, axis=0)

        self.median = np.median(train_data)
        self.mad = robust.mad(train_data, axis=1)

        #use robust snv normalization on the dataset
        train_data = norm.normalizeDataset_robust(train_data,self.median,self.mad)

        logger.log('Train data(samples,features): ' + str(train_data.shape))

        #create train labels based on the train dataset
        train_labels = []
        for i,num in enumerate(sample_num):
            temp = [i for x in xrange(num)]
            train_labels.append(temp)
        train_labels = np.concatenate(train_labels, axis=0)

        return train_data,train_labels

    def cross_validate(self,classifier,data,labels):
        logger.log('Using cross validation')
        logger.log('This might take some time...')
        start = time.clock()

        #Define the parameters to test with cross validation
        gammas = np.logspace(-6, -1, 10,base=10)
        degree = (2,3,4,5)
        Cs = np.geomspace(0.0001, 1000, num=8)
        parameters = [
        {'kernel': ['linear'], 'C': Cs},
        {'kernel': ['rbf'], 'C': Cs, 'gamma': gammas},
        {'kernel': ['poly'], 'C': Cs, 'gamma': gammas, 'degree' : degree},
        ]

        logger.log('\n')
        for kernel in parameters:
            for param in kernel:
                logger.log(str(param) + ' ' + str(kernel[param]))
            logger.log('\n')

        #Use Grid search combined with KFold splitting algorithm to find the optimal parameters for the classifier
        kfold = KFold(n_splits=10)
        classifier = GridSearchCV(estimator=classifier, cv=kfold, param_grid=parameters, return_train_score=True)
        classifier.fit(data,labels)

        end = time.clock()
        logger.log('Cross validation time: %fs' % end - start)

        logger.log('Mean Best Score:' + str(classifier.best_score_))
        classifier = classifier.best_estimator_

        return classifier

    def svm_train(self, data, labels, cv=True):
        logger.log('SVM: Initializing...')
        classifier = svm.SVC(probability=True)

        #if cv value is True use cross validation else use the (already known) optimal classifier
        if cv:
            classifier = self.cross_validate(classifier,data,labels)
        else:
            classifier = svm.SVC(C=100, cache_size=200, class_weight=None, coef0=0.0,
                decision_function_shape='ovr', degree=0, gamma='auto', kernel='linear',
                max_iter=-1, probability=True, random_state=None, shrinking=True,
                tol=0.001, verbose=False)

        logger.log('Classifier selected: \n' + str(classifier))
        classifier.fit(data, labels)
        return classifier

    def pls_train(self, train_data, train_labels, components=None, max_components=100):
        logger.log('PLS training', color='blue')
        #if the components input variable is not set we use KFold to split the train dataset
        #combined with cross validation to determine the optimal number of pls components to use
        if components is None:
            logger.log('Using cross-validation')
            mse = []

            kf_10 = model_selection.KFold(n_splits=10, shuffle=True, random_state=1)
            for i in xrange(1, max_components + 1):
                pls = PLSRegression(n_components=i, scale=False)
                score = model_selection.cross_val_score(pls, scale(train_data), 
                                                        train_labels, cv=kf_10, scoring='neg_mean_squared_error').mean()
                mse.append(-score)
            
            plotter.create_plot_pls(mse)
            components=mse.index(min(mse))+1

        logger.log('Optimal number of components: ' + str(components))
        self.pls = PLSRegression(n_components=components, scale=False)
        self.pls = self.pls.fit(train_data, train_labels)

    def pls_reduce(self, data):
        return self.pls.transform(data)

    def train(self, pls_components=None, svm_cv=True):
        logger.log('Starting Training', color='blue')
        
        train_data=self.train_data
        train_labels=self.train_labels
        logger.log('Train data(samples,features): ' + str(train_data.shape))
        
        #training pls model with the train data
        self.pls_train(train_data, train_labels, pls_components)

        #reduce the dimension of the train data using the pls model
        train_data = self.pls_reduce(train_data)
        logger.log('Train data(samples,features): ' + str(train_data.shape))

        #train the support vector machine with the train data
        logger.log('SVM: Training...')
        self.svm = self.svm_train(train_data,train_labels, svm_cv)

        logger.log('Training Complete', color='blue')

        coef = np.abs(self.pls.coef_[:,0])
        plotter.create_plot_samples(coef, self.datasets, self.train_data)

    def test(self):
        test_data=self.test_data
        test_labels=self.test_labels
        logger.log('Test data(samples,features): ' + str(test_data.shape))

        #reducing the dimension of the test data
        logger.log('PLS transformation')
        test_data = self.pls_reduce(test_data)
        logger.log('Test data(samples,features): ' + str(test_data.shape))

        #use the support vector machine to predict the classes of the test data
        logger.log('SVM: Predicting...')
        results = self.svm.predict(test_data)
        #print the accuracy of the classifier
        logger.log('Accuracy ' + str(accuracy_score(test_labels, results) * 100) + '%', color='green')

        logger.log('Original Labels:')
        logger.log(str(test_labels))
        logger.log('Test Labels:')
        logger.log(str(results))

        logger.log('Test Complete', color='blue')

        self.results = results
        
        plotter.create_plot_results(self.datasets, test_data, test_labels, results)
        
        predictedprobSVC = self.svm.predict_proba(test_data)
        plotter.create_plot_roc(predictedprobSVC, test_labels, self.datasets)

    def plot(self):
        plotter.plot()

    def run(self):
        self.train()
        self.test()
        plotter.plot()


datasets = ['beef','pork','fish','pineapple','rock', 'chic', 'spinach']
#Create a new experiment and load the appropriate datasets
#all datasets must be in the dataset folder as described in
#the dataset.py
exp = Experiment(datasets)

#Train the model
exp.train()
exp.test()
exp.stats()
exp.plot()