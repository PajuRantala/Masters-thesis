#!/bin/bash

if  [ -z "$CAMCAN_ROOT" ]
then
    echo "Setting CAMCAN_ROOT to /m/nbe/scratch/restmeg/data/camcan"
    export CAMCAN_ROOT=/m/nbe/scratch/restmeg/data/camcan
fi



for d in $CAMCAN_ROOT/cc700/mri/pipeline/release004/BIDSsep/anat/sub-CC520002/; do
    cd $d/anat
    pwd
    condor_submit $CAMCAN_ROOT/../code/gettrans/fidjob.cond    
    done
