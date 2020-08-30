# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 16:52:43 2018

@author: rantala2
"""


import os
import sys
import mne

def getAvgPsd(subjs):
    camcan_root = os.environ['CAMCAN_ROOT']
    stc_avg=mne.read_source_estimate(camcan_root + 'processed/cc700/mri/pipeline/release004/BIDSsep/megraw/' + subjs[0] + \
            '/meg/' + subjs[0] + '-fsaverage-singles-40hz_psd', 'fsaverage')
    numS = 1
    Ex = stc_avg - stc_avg
    Ex2 = stc_avg - stc_avg
    K = stc_avg.copy()
    print(stc_avg.shape)
    for s in subjs[1:]:
        try:
            stc_c = mne.read_source_estimate(camcan_root + 'processed/cc700/mri/pipeline/release004/BIDSsep/megraw/' + s + \
                                             '/meg/' + s + '-fsaverage-singles-40hz_psd', 'fsaverage')
            print(stc_c.shape)
            stc_avg += stc_c
            
            Ex += stc_c - K
            Ex2 += (stc_c - K)*(stc_c - K)
            
            numS += 1
            print('     \r' + str(numS),end='\r')
            sys.stdout.flush()
        except OSError as e:
            print(e)
        
    stc_avg = stc_avg/numS
    stc_var = (Ex2 - Ex*Ex/numS)/(numS-1)
    print('Done: ' + str(numS))
    return stc_avg, stc_var

def getAll():
    subj = [i[-12:] for i,_,_ in \
        os.walk('/m/nbe/scratch/restmeg/data/camcan/processed/cc700/mri/pipeline/release004/BIDSsep/megraw/') \
        if i[-12:-8] == 'sub-']
    
    stc_avg, stc_var = getAvgPsd(subj)
    #stc.plot(subject='fsaverage')
#    plt.plot(1e3 * stc.times, stc.data.T)
#    plt.xlabel('Frequency (Hz)')
#    plt.ylabel('PSD (dB)')
#    plt.title('Source Power Spectrum (PSD)')
#    plt.show()
    stc_avg.save('/m/nbe/scratch/restmeg/data/camcan/processed/total_avg-40hz')
    stc_var.save('/m/nbe/scratch/restmeg/data/camcan/processed/total_var-40hz')
    
def getCohort(idx):
    if idx < 1 or idx > 7:
        print('Please use index between 1 and 7')
        return
    subj = [i[-12:] for i,_,_ in \
        os.walk('/m/nbe/scratch/restmeg/data/camcan/processed/cc700/mri/pipeline/release004/BIDSsep/megraw/') \
        if i[-12:-5] == ('sub-CC' + str(idx))]
    
    stc_avg, stc_var = getAvgPsd(subj)
    #stc.plot(subject='fsaverage')
#    plt.plot(1e3 * stc.times, stc.data.T)
#    plt.xlabel('Frequency (Hz)')
#    plt.ylabel('PSD (dB)')
#    plt.title('Source Power Spectrum (PSD)')
#    plt.show()
    stc_avg.save('/m/nbe/scratch/restmeg/data/camcan/processed/sub-CC'+ str(idx) +'_avg-40hz')
    stc_var.save('/m/nbe/scratch/restmeg/data/camcan/processed/sub-CC'+ str(idx) +'_var-40hz')
    
def main():
    os.environ['SUBJECTS_DIR'] = '/m/nbe/scratch/restmeg/data/camcan/subjects_s3/'
    os.environ['CAMCAN_ROOT'] = '/m/nbe/scratch/restmeg/data/camcan/'
    for i in range(1,8):
        print('Starting cohort: ' + str(i))
        getCohort(i)
    getAll()

    
if __name__ == '__main__':
    main()

