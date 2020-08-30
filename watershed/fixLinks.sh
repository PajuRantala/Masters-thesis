#!/bin/bash

for d in /m/nbe/scratch/restmeg/data/camcan/subjects_s3/*/
do
    cd $d/bem/
    echo $d
    /m/nbe/scratch/restmeg/data/code/watershed/fixLink.sh
    
done
