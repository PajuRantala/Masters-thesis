#!/bin/bash

if  [ -z "$CAMCAN_ROOT" ]
then
    echo "Setting CAMCAN_ROOT to /m/nbe/scratch/restmeg/data/camcan"
    export CAMCAN_ROOT=/m/nbe/scratch/restmeg/data/camcan
fi



for d in $CAMCAN_ROOT/emptyroom/*/; do

    cd $d
    if [ ! -e ./*cov.fif ]
    then
	pwd
        python $CAMCAN_ROOT/../code/noisecov/noisecov.py empty_room_tsss.fif
    fi


done
