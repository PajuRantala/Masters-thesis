#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 14:26:20 2018

@author: rantala2
"""
import mne
import os
import numpy as np

os.environ['SUBJECTS_DIR'] = 'F:\dippa'
labels = mne.read_labels_from_annot('fsaverage')
stc = mne.read_source_estimate(r'F:\dippa\processed\total_avg-40hz', subject='fsaverage')
max_alphas = {l:np.max(np.mean(stc.in_label(l).crop(0.005,0.015).data,axis=0)) for l in labels[0:-1]}
stcc = stc.copy()
for l, d in max_alphas.items():
    stcc.data[l.get_vertices_used() + 10242*(0 if l.hemi == 'lh' else 1)] = d
max_label=max(max_alphas , key=lambda key: max_alphas[key])
max_label=[a for a in max_alphas if a.name == 'cuneus-rh']q = []
max_alpha_age_var = []
for idx in range(1,8):
    stc = mne.read_source_estimate('F:\dippa\processed\sub-CC'+ str(idx) +'_avg-40hz', 'fsaverage')
    var = mne.read_source_estimate('F:\dippa\processed\sub-CC'+ str(idx) +'_var-40hz', 'fsaverage')
    max_idx = np.argmax(np.mean(stc.in_label(max_label).crop(0.005,0.015).data, axis=0))
    max_alpha_age.append((0.005+stc.tstep*max_idx)*1000)
    max_alpha_age_var.append(np.mean(var.in_label(max_label).data[:,int(max_idx + 0.005/stc.tstep)]))

ages={}    
with open('F:\dippa\participant_data.tsv') as f:
    f.readline()
    for l in f:
        ages['sub-' + l.split('\t')[0]] = int(l.split('\t')[1])
        
subjs = [i[-12:] for i,_,_ in \
        os.walk('/m/nbe/scratch/restmeg/data/camcan/processed/cc700/mri/pipeline/release004/BIDSsep/megraw/') \
        if i[-12:-8] == 'sub-']

age = []
alpha = []
alphaA = []
i = 0
for s in subjs:
        try:
            try:
                age.append(ages[s])
            except KeyError as e:
                print(e)
                continue
            stc_c = mne.read_source_estimate('/m/nbe/scratch/restmeg/data/camcan/processed/cc700/mri/pipeline/release004/BIDSsep/megraw/' + s + \
                                             '/meg/' + s + '-fsaverage-singles-40hz_psd', 'fsaverage')
            
            max_idx = np.argmax(np.mean(stc_c.in_label(max_label).crop(0.005,0.015).data, axis=0))
            alpha.append((0.005+stc_c.tstep*max_idx)*1000)
            alphaA.append(np.mean(stc_c.in_label(max_label).crop(0.005,0.015).data, axis=0)[max_idx])
            print(i, end='\r')
            i+=1
        except OSError as e:
            print(e)
            age = age[0:-1]