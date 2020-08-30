# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 18:00:06 2020

@author: Koti
"""



import os
import numpy as np
import mne

from surfer import Brain
from surfer.io import read_stc
os.environ['SUBJECTS_DIR'] = 'F:\dippa'
# define subject, surface and hemisphere(s) to plot:

subject_id, surf = 'fsaverage', 'inflated'
hemi = 'lh'
stc_fname = os.path.join(r'F:\dippa\processed\total_avg-40hz-' +
                         hemi + '.stc')
stc = mne.read_source_estimate(stc_fname)
labels = mne.read_labels_from_annot('fsaverage')
stc_label = stc.in_label([a for a in labels if a.name == 'lateraloccipital-lh'][0])

stc_var_fname = os.path.join(r'F:\dippa\processed\total_var-40hz-' +
                         hemi + '.stc')
stc_var = mne.read_source_estimate(stc_var_fname)
labels = mne.read_labels_from_annot('fsaverage')
stc_var_label = stc_var.in_label([a for a in labels if a.name == 'lateraloccipital-lh'][0])