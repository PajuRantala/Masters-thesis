#!/bin/bash

dirnames=(*/)
sub=${dirnames[$1]}
sub=${sub%?}
echo "${sub}"
mne watershed_bem -s ${sub} -d . -o
