#!/bin/python
import csv
import numpy as np
from console import bcolors
from logger import logger

directory = './data/'

def loadData(datasets, start= None, end=None, num=None):
	data = []
	for dataset in datasets:
		data.append(loadDataset(dataset,start,end,num))
	return np.concatenate(data,axis=0)

def loadDataset(name, start=None, end=None, num=None):
	dataset = np.loadtxt(directory+name+'.csv',delimiter = ',', dtype = np.float32)
	if num is not None and num > dataset.shape[0]:
		logger.log('Only ' + str(dataset.shape[0]) + ' samples loaded from file ' + name + '.csv (instead of ' + str(num) + ')','WARNING', bcolors.WARNING)
		# print bcolors.WARNING + 'WARNING\t   Only',dataset.shape[0],'samples loaded from file ' + name + '.csv (instead of ',num,')' + bcolors.ENDC
	return dataset[:num,start:end]

def saveDataset(dataset, name='results'):
	np.savetxt(fname=directory + name + '.csv', delimiter=',', X=dataset)

def loadFile(name):
	return np.loadtxt(directory+name+'.csv',delimiter = ',', dtype = np.float32)
	

#Use this function to fix datasets that contain errors.
#Ex a dataset contain lines that have less or more columns than x
#it creates a new file called filename_fixeds.csv with all 
#lines from fileName that have x features
def fixDataSet(fileName,x):
	fixed = open(fileName[:-4] + '_fixed.csv','wb')
	file = open(fileName)
	writer = csv.writer(fixed,dialect='excel')
	reader = csv.reader(file)
	for line in reader:
		if len(line) != x:
			continue
		print len(line)
		writer.writerow(line[:x])


#Returns a subset of the dataset containing for all samples only 
#the features that are present in the indexes array
def getSubset(dataset,indexes):
	arr = []
	for sample in dataset:
		sample1 = [sample[index] for index in indexes]
		arr.append(sample1)
	x=np.array(arr,dtype=object)
	return x



