# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:25:27 2020

@author: Koti
"""

import os
import numpy as np

from surfer import Brain
from surfer.io import read_stc
os.environ['SUBJECTS_DIR'] = 'F:\dippa'
# define subject, surface and hemisphere(s) to plot:

#subject_id, surf = 'sub-CC220843', 'inflated'
subject_id, surf = 'fsaverage', 'inflated'
hemi = 'rh'

# create Brain object for visualization
brain = Brain(subject_id, hemi, surf, size=(800, 800), background='w',
              interaction='terrain', cortex='bone', units='m', show_toolbar=True )

# label for time annotation in milliseconds


def time_label(t):
    return 'Freq = %0.2f Hz' % (t * 1e3)


# Read MNE dSPM inverse solution and plot

for hemi in ['rh']:
    stc_fname = os.path.join(r'F:\dippa\processed\total_avg-40hz-' +
                             hemi + '.stc')
    stc_fname = os.path.join(r'F:\dippa\processed\sub-CC220843\sub-CC220843-fsaverage-singles_psd-' +
                             hemi + '.stc')
    stc = read_stc(stc_fname)

    # data and vertices for which the data is defined
    data = stc['data']
    vertices = stc['vertices']
    #data = (data/data.mean(0))*100

    # time points (in seconds)
    time = np.linspace(stc['tmin'], stc['tmin'] + data.shape[1] * stc['tstep'],
                       data.shape[1], endpoint=False)

    # colormap to use
    colormap = 'hot'

    # add data and set the initial time displayed to 100 ms,
    # plotted using the nearest relevant colors
    brain.add_data(data, colormap=colormap, vertices=vertices,
                   smoothing_steps=15, time=time, time_label=time_label,
                   hemi=hemi, initial_time=0.01, verbose=False)
    #brain.scale_data_colormap(fmin=95, fmid=100, fmax=105, transparent=True, verbose=False)
    #brain.save_movie('F:/dippa/movies/test_movie.mov',500, framerate=60)
    #brain.close()
from surfer import TimeViewer
viewer = TimeViewer(brain)
# scale colormap
#brain.scale_data_colormap(fmin=13, fmid=18, fmax=22, transparent=True, verbose=False)