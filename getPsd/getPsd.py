# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 16:12:31 2018

@author: rantala2
"""

import mne
import os
import sys


def createSrc(subj):
    camcan_root = os.environ['CAMCAN_ROOT']
    ico4_fname = camcan_root + 'processed/cc700/mri/pipeline/release004/BIDSsep/megraw/' + subj + '/meg/' + subj + '-ico4-src.fif'
    try:
        src = mne.read_source_spaces(ico4_fname)
    except IOError:
        src = mne.setup_source_space(subj, spacing='ico4')
        mne.write_source_spaces(ico4_fname, src)

    return src


def makeBem(subj):
    camcan_root = os.environ['CAMCAN_ROOT']
    bemmodel_fname = camcan_root + 'processed/cc700/mri/pipeline/release004/BIDSsep/megraw/' + subj + '/meg/' + subj + \
                    '-5120-5120-5120-singles-bem.fif'
    bemsolution_fname = camcan_root + 'processed/cc700/mri/pipeline/release004/BIDSsep/megraw/' + subj + '/meg/' + \
                    subj + '-5120-5120-5120-singles-bem-sol.fif'
    try:
        model = mne.read_bem_surfaces(bemmodel_fname)
    except IOError:
        model = mne.make_bem_model(subj, conductivity=[0.3])
        mne.write_bem_surfaces(bemmodel_fname, model)
        
    try:
        bem_sol = mne.read_bem_solution(bemsolution_fname)
    except IOError:
        bem_sol = mne.make_bem_solution(model)
        mne.write_bem_solution(bemsolution_fname, bem_sol)
        
    return bem_sol


def makeInv(subj, src, bem_sol):
    camcan_root = os.environ['CAMCAN_ROOT']
    raw_fname = camcan_root + 'cc700/mri/pipeline/release004/BIDSsep/megraw/' + subj + '/meg/rest_raw_tsss_mc.fif'
    trans_fname = camcan_root + 'cc700/mri/pipeline/release004/BIDSsep/megraw/' + subj + '/meg/' + subj + '-new-fid-AR-trans.fif'
    cov_fname = camcan_root + 'emptyroom/' + subj[4:] + '/empty_room_tsss_cov.fif'
    cov = mne.read_cov(cov_fname)
    raw = mne.io.Raw(raw_fname)
    fwd = mne.make_forward_solution(raw.info, trans_fname, src, bem_sol)
    inv = mne.minimum_norm.make_inverse_operator(raw.info, fwd, cov, loose=0.2)
    stc = mne.minimum_norm.compute_source_psd(raw, inv, lambda2=0.1111111111111111, method='dSPM', tmin=None, \
        tmax=None, fmin=0.0, fmax=40.0, n_fft=2048*4, overlap=0.5, pick_ori=None, label=None, nave=1, pca=True,\
        prepared=False)
    stc_fsaverage = stc.morph('fsaverage')
    stc_fsaverage.save(camcan_root + 'processed/cc700/mri/pipeline/release004/BIDSsep/megraw/' + subj + '/meg/' + subj + '-fsaverage-singles-40hz_psd')


def processSubj(subj):
    src = createSrc(subj)
    bem_sol = makeBem(subj)
    makeInv(subj, src, bem_sol)


if __name__ == "__main__":
    processSubj(sys.argv[1])
