#!/bin/bash

echo "Starting"
if  [ -z "$CAMCAN_ROOT" ]
then
    echo "Setting CAMCAN_ROOT to /m/nbe/scratch/restmeg/data/camcan"
    export CAMCAN_ROOT=/scratch//nbe/restmeg/data/camcan
fi

module load matlab/2017b
module load spm/12
type matlab


matlab -nosplash -nodesktop -r "try; cd $PWD; disp(pwd); getfid($1); catch e; disp(e); end; exit";


