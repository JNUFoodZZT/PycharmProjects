#!/bin/python
import numpy as np

def normalizeDataset(dataset,mean,std):
    dataset_nrm = []
    for i, sample in enumerate(dataset):
        sample_nrm = (sample - mean)/std
        sample_nrm = (sample_nrm - sample_nrm.min())/(sample_nrm.max() - sample_nrm.min())
        dataset_nrm.append(sample_nrm)
    return np.array(dataset_nrm)

def normalizeDataset_robust(dataset,median,mad):
    dataset_nrm = []
    for i, sample in enumerate(dataset):
        sample_nrm = (sample - median)/mad[i]
        sample_nrm = (sample_nrm - sample_nrm.min())/(sample_nrm.max() - sample_nrm.min())
        dataset_nrm.append(sample_nrm)
    return np.array(dataset_nrm)

def normalizeSample(sample,mean,std):
	sample_nrm = (sample - mean)/std
	sample_nrm = (sample_nrm - sample_nrm.min())/(sample_nrm.max() - sample_nrm.min())
	return sample_nrm

def normalizeSample_robust(sample,median,mad):
	sample_nrm = (sample - median)/mad
	sample_nrm = (sample_nrm - sample_nrm.min())/(sample_nrm.max() - sample_nrm.min())
	return sample_nrm