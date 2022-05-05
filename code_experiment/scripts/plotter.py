#!/bin/python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from sklearn.metrics import roc_curve, auc


class plotter:
	
	@staticmethod
	def create_plot_roc(predictedprobSVC, test_labels, datasets):

		colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

		with plt.style.context(('ggplot')):
			plt.figure(figsize=(18,19))
			plt.xlabel('False Positive Rate')
			plt.ylabel('True Positive Rate')
			plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
			plt.xlim([0.0, 1.0])
			plt.ylim([0.0, 1.05])
			plt.title('SVM Classifier ROC')
			for i in xrange(predictedprobSVC.shape[1]):
				fpr, tpr, _ = roc_curve(test_labels, predictedprobSVC[:,i], pos_label=i)
				roc_auc = auc(fpr, tpr)
				plt.plot(fpr, tpr, color=colors[i], lw=2, label='SVM ROC area for %s = %0.2f)' % (datasets[i], roc_auc))
			plt.legend(loc="lower right")

	@staticmethod
	def create_plot_pls(mse):
		with plt.style.context(('ggplot')):
		    plt.figure(figsize=(18,19))
		    plt.plot(np.arange(1, len(mse) + 1), np.array(mse), '-v')
		    plt.xlabel('Number of principal components in regression')
		    plt.ylabel('MSE')
		    plt.title('FTIR')
		    plt.xlim(xmin=-1)

	@staticmethod
	def create_plot_results(datasets, test_data, test_labels, results):
		with plt.style.context(('ggplot')):
			fig = plt.figure(figsize=(18,19))
			colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

			handles = []
			for i,dataset in enumerate(datasets):
			    handles.append(mpatches.Patch(color=colors[i], label=dataset))

			ax = fig.add_subplot(211, projection='3d')
			ax.set_title('Original Data')
			for i,sample in enumerate(test_data):
			    ax.scatter(sample[0], sample[1], sample[2], c=colors[test_labels[i]], marker='o')

			ax = fig.add_subplot(212, projection='3d')
			ax.set_title('Classification')
			for i,sample in enumerate(test_data):
			    ax.scatter(sample[0], sample[1], sample[2], color=colors[results[i]], marker = "o")

			fig.legend(handles, datasets, loc='lower center', ncol=len(datasets))

	@staticmethod
	def create_plot_samples(coef, datasets, train_data):
		with plt.style.context(('ggplot')):
			ind_plot = [0, 400, 780, 1080, 1360, 1550, 1635]
			plt_data = np.transpose(train_data[ind_plot,])
			wl = np.transpose(np.arange(1000,2700,1))
			handles = []
			colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
			for i,dataset in enumerate(datasets):
			    handles.append(mpatches.Patch(color=colors[i], label=dataset))

			plt.figure(figsize=(18,19))
			ax1 = plt.subplot(211)
			plt.plot(wl, plt_data)
			plt.ylabel('Normalized Spectra')
			ax1.legend(handles=handles)

			ax2 = plt.subplot(212, sharex=ax1)
			plt.plot(wl, coef)
			plt.xlabel('Wavelength (cm-1)')
			plt.ylabel('PLS coefficients')

	@staticmethod
	def plot():
		plt.show()