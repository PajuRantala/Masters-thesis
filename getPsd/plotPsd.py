# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 13:50:12 2020

@author: Koti
"""
import mne
import os
import sys

def makeInv(subj, src, bem_sol):
    camcan_root=r'F:/dippa/'
    raw_fname = camcan_root + 'megraw/' + subj + '/meg/rest_raw_tsss_mc.fif'
    trans_fname = camcan_root + 'megraw/' + subj + '/meg/' + subj + '-new-fid-AR-trans.fif'
    cov_fname = camcan_root + 'emptyroom/' + subj[4:] + '/empty_room_tsss_cov.fif'
    cov = mne.read_cov(cov_fname)
    raw = mne.io.Raw(raw_fname)
    fwd = mne.make_forward_solution(raw.info, trans_fname, src, bem_sol)
    inv = mne.minimum_norm.make_inverse_operator(raw.info, fwd, cov, loose=0.2)
    stc = mne.minimum_norm.apply_inverse_raw(raw, inv,start=None, stop=10000, lambda2=0.1111111111111111, buffer_size=1000)
    return stc
subj ='sub-CC220843'
os.environ['SUBJECTS_DIR'] = r'F:\dippa\anat'
camcan_root=r'F:/dippa/'

ico4_fname = camcan_root + 'processed/' + subj + '/' + subj + '-ico4-src.fif'
bemsolution_fname = camcan_root + 'processed/' + subj + '/' + \
                    subj + '-5120-5120-5120-singles-bem-sol.fif'
                    
bem_sol = mne.read_bem_solution(bemsolution_fname)
src = mne.read_source_spaces(ico4_fname)
stc = makeInv(subj, src, bem_sol)

brain = stc.plot(hemi='rh')
from surfer import TimeViewer
viewer = TimeViewer(brain)