# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 17:36:27 2018

@author: rantala2
"""

import mne
import sys
import subprocess
# import os


def createBem(subj):
    src = mne.setup_source_space(subj, n_jobs=2)
    subprocess.call(['mne', 'watershed_bem', '-s', subj])
    model = mne.make_bem_model(subj, conductivity=[0.3])
    bem = mne.make_bem_solution(model)
    mne.write_bem_solution(subj+'-5120-5120-5120-bem-sol.fif', bem)
    mne.viz.plot_bem(subj)


def createInv(subj):
    # subjdir = os.environ['SUBJECTS_DIR']
    file_path = '/m/nbe/scratch/restmeg/data/camcan/cc700/mri/pipeline/release004/BIDSsep/megraw/sub-'+subj+'/meg/'
    raw = mne.io.fiff.Raw(file_path+'rest_raw.fif')
    fname_trans = file_path + 'rest_raw-trans.fif'
    src = mne.read_source_spaces('/m/nbe/scratch/restmeg/data/camcan/subjects/'+subj+'/bem/'+subj+'-oct-6-src.fif')
    bem_sol = mne.read_bem_solution(subj+'-5120-5120-5120-bem-sol.fif')

    fwd = mne.make_forward_solution(raw.info, fname_trans, src, bem_sol)
    cov = mne.compute_raw_covariance(raw)
    inv = mne.minimum_norm.make_inverse_operator(raw.info, fwd, cov, loose=0.2)
    mne.minimum_norm.write_inverse_operator(subj+'-inv.fif', inv)
    
def createCov(subj):
    file_path = '/m/nbe/scratch/restmeg/data/camcan/emptyroom/'+subj
    raw = mne.io.fiff.Raw(file_path+'/emptyroom_' + subj + '.fif')
    cov = mne.compute_raw_covariance(raw)
    cov.save(file_path+'/emptyroom_' + subj + '-cov.fif')
    
def doSSS(subj):
    file_path = '/m/nbe/scratch/restmeg/data/camcan/cc700/mri/pipeline/release004/BIDSsep/megraw/sub-'+subj+'/meg/'
    raw = mne.io.fiff.Raw(file_path+'rest_raw.fif')
    sss_cal = '/m/nbe/scratch/restmeg/data/camcan/cc700/mri/pipeline/release004/BIDSsep/megraw/sss_cal.dat'
    ct = '/m/nbe/scratch/restmeg/data/camcan/cc700/mri/pipeline/release004/BIDSsep/megraw/ct_sparse.fif'
    raw_sss = mne.preprocessing.maxfilter(raw, calibration=sss_cal, cross_talk= ct, st_duration=20)
    raw_sss.save('/m/nbe/scratch/restmeg/data/camcan/processed/cc700/mri/pipeline/release004/BIDSsep/megraw/sub-'+subj+'/meg/rest_raw_sss.fif')
    
    
def shortTest(subj):
    file_path = '/m/nbe/scratch/restmeg/data/camcan/cc700/mri/pipeline/release004/BIDSsep/megraw/sub-'+subj+'/meg/'
    raw = mne.io.fiff.Raw(file_path+'rest_raw.fif')
    rank = raw.estimate_rank()
    file_name = '/m/nbe/scratch/restmeg/data/camcan/processed/cc700/mri/pipeline/release004/BIDSsep/megraw/sub-'+subj+'/meg/rank_rest_raw.txt'
    with open(file_name, 'w') as f:
        f.write(str(rank))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        createBem(sys.argv[1])
    else:
        subj = 'CC110033'
        # stc_bin = mne.read_source_estimate(fname=subj+'-bin')
        VALUE = '/m/nbe/scratch/restmeg/data/camcan/subjects/'
        mne.utils.set_config("SUBJECTS_DIR", VALUE, set_env=True)
        createCov(subj)
        
        
        
        
        #createInv('CC110033')