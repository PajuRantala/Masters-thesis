# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 16:46:51 2018

@author: rantala2
"""

from mne.gui._coreg_gui import CoregModel
import os
import sys

os.environ['CAMCAN_ROOT'] = r'F:\dippa' + '\\'

def calcTrans(subj):
    camcan_root = os.environ['CAMCAN_ROOT']
    if camcan_root == '':
        print('No camcan root directory!, exiting!')
        sys.exit()
    cm = CoregModel()
    #cm.mri.subject_source.set(use_high_res_head=False)
    cm.mri.subject_source.set(subjects_dir=camcan_root+'subjects_s3/')
    cm.hsp.trait_set(file=camcan_root + 'megraw/' + subj + '/meg/rest_raw.fif')
    cm.mri.fid.trait_set(file=camcan_root + 'subjects_s3/' + subj + '/bem/' + subj + '-fiducials.fif')

    cm.fit_fiducials()
    cm.omit_hsp_points(0.020)
    #cm.fit_icp()
    with open(camcan_root+'processed/coreg_logs/' + subj + '_hs3.csv', 'w') as f:
        cm.print_traits()
        f.write(str(cm.lpa_distance) + '\n')
        f.write(str(cm.rpa_distance) + '\n')
        f.write(str(cm.nasion_distance) + '\n')
        f.write(str(cm.point_distance) + '\n')
    
    cm.save_trans(camcan_root + 'megraw/' + subj + '/meg/'+subj + '-new-fid-PR-trans.fif')


if __name__ == "__main__":
    calcTrans('sub-CC220843')

