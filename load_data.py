#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 23:34:21 2020

@author: biraj
"""

import mne
import numpy as np

def load_data(data_type):
    if data_type == 'LR':
        LR_T0=[]; LR_T1=[]; LR_T2=[];
        
    elif data_type == 'ILR':
        ILR_T0=[]; ILR_T1=[]; ILR_T2=[];
        
    elif data_type == 'HF': 
        HF_T0=[]; HF_T1=[]; HF_T2=[];
        
    elif data_type == 'IHF': 
        IHF_T0=[]; IHF_T1=[]; IHF_T2=[];
        
    else: print('Wrong data_type selected options :LR, ILR, HF, IHF')
        
    for i in range(109):
        if i==0:
            continue
        sbj=str(i);
        if i<10:
            sbj='00'+str(i); print(sbj)
        elif ((i>=10) and (i<100)):
            sbj='0'+str(i); print(sbj)
        for j in range(14):
            if j<=2:
                continue
            rec=str(j);
            if((j>=3) and (j<10)):
                rec='0'+str(j);
                
            if (data_type =='LR' and ((j==3) or (j==7) or (j==11))):
                edf_loc= '/media/biraj/DATA/Motor Imagery Dataset/S'+sbj+'/S'+sbj+'R'+rec+'.edf'
                Data = mne.io.read_raw_edf(edf_loc)
                events, event_id=mne.events_from_annotations(Data)
                epochs=mne.Epochs(Data, events, event_id, tmin=0, tmax=4, baseline=(None,None))
                LR_T0.append(epochs['T0'])
                LR_T1.append(epochs['T1'])
                LR_T2.append(epochs['T2'])
                continue
            elif (data_type == 'ILR' and ((j==4) or (j==8) or (j==12))):
                edf_loc= '/media/biraj/DATA/Motor Imagery Dataset/S'+sbj+'/S'+sbj+'R'+rec+'.edf'
                Data = mne.io.read_raw_edf(edf_loc)
                events, event_id=mne.events_from_annotations(Data)
                epochs=mne.Epochs(Data, events, event_id, tmin=0, tmax=4, baseline=(None,None))
                ILR_T0.append(epochs['T0'])
                ILR_T1.append(epochs['T1'])
                ILR_T2.append(epochs['T2'])
                continue
            elif (data_type == 'HF' and ((j==5) or (j==9) or (j==13))):
                edf_loc= '/media/biraj/DATA/Motor Imagery Dataset/S'+sbj+'/S'+sbj+'R'+rec+'.edf'
                Data = mne.io.read_raw_edf(edf_loc)
                events, event_id=mne.events_from_annotations(Data)
                epochs=mne.Epochs(Data, events, event_id, tmin=0, tmax=4, baseline=(None,None))
                HF_T0.append(epochs['T0'])
                HF_T1.append(epochs['T1'])
                HF_T2.append(epochs['T2'])
                continue
            elif (data_type == 'IHF' and ((j==6) or (j==10) or (j==14))):
                edf_loc= '/media/biraj/DATA/Motor Imagery Dataset/S'+sbj+'/S'+sbj+'R'+rec+'.edf'
                Data = mne.io.read_raw_edf(edf_loc)
                events, event_id=mne.events_from_annotations(Data)
                epochs=mne.Epochs(Data, events, event_id, tmin=0, tmax=4, baseline=(None,None))
                IHF_T0.append(epochs['T0'])
                IHF_T1.append(epochs['T1'])
                IHF_T2.append(epochs['T2'])
                continue

    if data_type == 'LR':
        return LR_T0, LR_T1,LR_T2;
    elif data_type == 'ILR':
        return ILR_T0, ILR_T1, ILR_T2;
    elif data_type == 'HF': 
        return HF_T0, HF_T1, HF_T2;
    elif data_type == 'IHF': 
        return IHF_T0, IHF_T1, IHF_T2;        
    else: print('Return error'); return (0)
