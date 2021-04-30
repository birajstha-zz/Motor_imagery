#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 01:53:56 2020

@author: biraj
"""


import tensorflow as tf
import brainconn
import numpy as np
import mne
import matplotlib.pyplot as plt
import load_data as ld




fmin=4
fmax=8
how_many=4


def create_training_data(data_array, category):
    plv_list = []
    for i in range(5):
        try:
            print (i)
            T=data_array[i];
            plv, freqs, times, n_epochs, n_tapers=mne.connectivity.spectral_connectivity(T, 
                                                                                         method='plv', 
                                                                                         indices=None, 
                                                                                         mode='cwt_morlet', 
                                                                                         sfreq=ld.LR_T0[i].info['sfreq'], fmin=fmin, 
                                                                                         fmax=fmax, faverage=True, 
                                                                                         tmin=0, tmax=4, 
                                                                                         cwt_freqs=np.linspace(fmin,fmax,how_many), 
                                                                                         cwt_n_cycles=1, n_jobs=1)
            plv_list.append(plv[:,:,0,:].T);
        except Exception as e:
            pass
    return plv_list

## for imaginary
plv_list_T0 = create_training_data(ld.ILR_T0,category=0)
plv_list_T1 = create_training_data(ld.ILR_T1, category=1)
plv_list_T2 = create_training_data(ld.ILR_T2, category=2)

plv_avg_T0 = np.mean(np.array(plv_list_T0), axis=0)
plv_avg_T1 = np.mean(np.array(plv_list_T1), axis=0)
plv_avg_T2 = np.mean(np.array(plv_list_T2), axis=0)

def eigen_v(plv):
    evc = []
    for j in range(len(plv)):
        #evc.append(abs(np.linalg.eig(abs(plv[:,:,0,j]+np.transpose(plv[:,:,0,j])))[0]))
        evc.append(abs(brainconn.centrality.eigenvector_centrality_und(plv[j]+plv[j].T)))
    return evc


I_evc_T0= eigen_v(plv_avg_T0)
I_evc_T1= eigen_v(plv_avg_T1)
I_evc_T2= eigen_v(plv_avg_T2)