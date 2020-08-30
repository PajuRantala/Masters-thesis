# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 16:46:51 2018

@author: rantala2
"""

from mne.gui._coreg_gui import CoregModel
import os
import sys


def calcTrans(subj):
    camcan_root = os.environ['CAMCAN_ROOT']
    if camcan_root == '':
        print('No camcan root directory!, exiting!')
        sys.exit()
    cm = CoregModel()
    cm.mri.subject_source.set(use_high_res_head=False)
    cm.mri.subject_source.set(subjects_dir=camcan_root+'subjects_s3/')
    cm.hsp.trait_set(file=camcan_root + 'cc700/mri/pipeline/release004/BIDSsep/megraw/' + subj + '/meg/rest_raw.fif')
    cm.mri.fid.trait_set(file=camcan_root + 'subjects_s3/' + subj + '/bem/' + subj + '-fiducials.fif')
    cm.fit_fiducials()
    cm.omit_hsp_points(0.020, True)
    cm.fit_hsp_points()
    with open(camcan_root+'processed/coreg_logs/' + subj + '_hs.csv', 'w') as f:
        cm.print_traits()
        f.write(str(cm.lpa_distance) + '\n')
        f.write(str(cm.rpa_distance) + '\n')
        f.write(str(cm.nasion_distance) + '\n')
        f.write(str(cm.point_distance) + '\n')
    
    cm.save_trans(camcan_root + 'cc700/mri/pipeline/release004/BIDSsep/megraw/' + subj + '/meg/'+subj + '-new-hs-AR-trans.fif')


if __name__ == "__main__":
    calcTrans(sys.argv[1])
