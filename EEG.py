# -*- coding: utf-8 -*-
"""
Created on Fri May  1 23:57:56 2020

@author: Biraj
"""


import mne
import numpy as np
import brainconn
#import networkx as nx
#import scipy as sp
import matplotlib.pyplot as plt

sbj='003'
rec='03'

edf_loc= '/run/media/biraj/DATA/Motor Imagery Dataset/S'+sbj+'/S'+sbj+'R'+rec+'.edf'
Data = mne.io.read_raw_edf(edf_loc)

Backup=Data



events, event_id=mne.events_from_annotations(Data)

epochs=mne.Epochs(Data, events, event_id=event_id, tmin=0, tmax=4, baseline=(None,None))

#fig = mne.viz.plot_events(events,event_id=event_id,sfreq=Data.info['sfreq'], first_samp=Data.first_samp)

T0=epochs['T0'].get_data()
T1=epochs['T1'].get_data()
T2=epochs['T2'].get_data()

fmin=4
fmax=8
how_many=10

for i in range(3):
    T=epochs['T'+str(i)]
    plv, freqs, times, n_epochs, n_tapers=mne.connectivity.spectral_connectivity(T, method='pli', indices=None, mode='cwt_morlet', sfreq=info['sfreq'], fmin=fmin, fmax=fmax, faverage=True, tmin=0, tmax=4, cwt_freqs=np.linspace(fmin,fmax,how_many), cwt_n_cycles=1, n_jobs=1)
    evc=[]
    #betweenness=[]
    for j in range(len(plv[1,1,0,:])):
        #evc.append(abs(np.linalg.eig(abs(plv[:,:,0,j]+np.transpose(plv[:,:,0,j])))[0]))
        evc.append(abs(brainconn.centrality.eigenvector_centrality_und(plv[:,:,0,j]+np.transpose(plv[:,:,0,j]))))
        #evc.append(abs(brainconn.centrality.subgraph_centrality(plv[:,:,0,j]+np.transpose(plv[:,:,0,j]))))
        #betweenness.append(brainconn.centrality.kcoreness_centrality_bu(plv[:,:,0,j]+np.transpose(plv[:,:,0,j]))[0])
    if i==0:
        evc_T0=np.transpose(np.array(evc))
        #betweenness_T0=np.transpose(np.array(betweenness))
    if i==1:
        evc_T1=np.transpose(np.array(evc))
        #betweenness_T1=np.transpose(np.array(betweenness))
    if i==2:
        evc_T2=np.transpose(np.array(evc))
        #betweenness_T2=np.transpose(np.array(betweenness))
        
plt.imshow(evc_T1-evc_T1)
#plt.imshow(betweenness_T1-betweenness_T0)

##
