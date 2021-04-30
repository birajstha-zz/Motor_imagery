#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 23:34:21 2020

@author: biraj
"""




import mne
#import numpy as np
#import brainconn
#import networkx as nx
#import scipy as sp
#import matplotlib.pyplot as plt


def load_data():
    LR_T0=[]; LR_T1=[]; LR_T2=[];
    ILR_T0=[]; ILR_T1=[]; ILR_T2=[];
    HF_T0=[]; HF_T1=[]; HF_T2=[];
    IHF_T0=[]; IHF_T1=[]; IHF_T2=[];
    for i in range(109):
        if i==0:
            continue
        print(i);
        sbj=str(i);
        if i<10:
            sbj='00'+str(i); print(sbj)
        elif ((i>=10) and (i<100)):
            sbj='0'+str(i); print(sbj)
        for j in range(14):
            if j<=2:
                continue
            print(j)
            rec=str(j);
            if((j>=3) and (j<10)):
                rec='0'+str(j);
            if ((j==3) or (j==7) or (j==11)):
                edf_loc= '/run/media/biraj/DATA/Motor Imagery Dataset/S'+sbj+'/S'+sbj+'R'+rec+'.edf'
                Data = mne.io.read_raw_edf(edf_loc)
                events, event_id=mne.events_from_annotations(Data)
                epochs=mne.Epochs(Data, events, event_id, tmin=0, tmax=4, baseline=(None,None))
                LR_T0.append(epochs['T0'].get_data())
                LR_T1.append(epochs['T1'].get_data())
                LR_T2.append(epochs['T2'].get_data())
                continue
            elif ((j==4) or (j==8) or (j==12)):
                edf_loc= '/run/media/biraj/DATA/Motor Imagery Dataset/S'+sbj+'/S'+sbj+'R'+rec+'.edf'
                Data = mne.io.read_raw_edf(edf_loc)
                events, event_id=mne.events_from_annotations(Data)
                epochs=mne.Epochs(Data, events, event_id, tmin=0, tmax=4, baseline=(None,None))
                ILR_T0.append(epochs['T0'].get_data())
                ILR_T1.append(epochs['T1'].get_data())
                ILR_T2.append(epochs['T2'].get_data())
                continue
            elif ((j==5) or (j==9) or (j==13)):
                edf_loc= '/run/media/biraj/DATA/Motor Imagery Dataset/S'+sbj+'/S'+sbj+'R'+rec+'.edf'
                Data = mne.io.read_raw_edf(edf_loc)
                events, event_id=mne.events_from_annotations(Data)
                epochs=mne.Epochs(Data, events, event_id, tmin=0, tmax=4, baseline=(None,None))
                HF_T0.append(epochs['T0'].get_data())
                HF_T1.append(epochs['T1'].get_data())
                HF_T2.append(epochs['T2'].get_data())
                continue
            elif ((j==6) or (j==10) or (j==14)):
                edf_loc= '/run/media/biraj/DATA/Motor Imagery Dataset/S'+sbj+'/S'+sbj+'R'+rec+'.edf'
                Data = mne.io.read_raw_edf(edf_loc)
                events, event_id=mne.events_from_annotations(Data)
                epochs=mne.Epochs(Data, events, event_id, tmin=0, tmax=4, baseline=(None,None))
                IHF_T0.append(epochs['T0'].get_data())
                IHF_T1.append(epochs['T1'].get_data())
                IHF_T2.append(epochs['T2'].get_data())
                continue
    return LR_T0,LR_T1,LR_T2,ILR_T0,ILR_T1,ILR_T2,HF_T0,HF_T1,HF_T2,IHF_T0,IHF_T1,IHF_T2

LR_T0,LR_T1,LR_T2,ILR_T0,ILR_T1,ILR_T2,HF_T0,HF_T1,HF_T2,IHF_T0,IHF_T1,IHF_T2=load_data()