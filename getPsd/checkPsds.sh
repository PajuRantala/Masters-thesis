#!/bin/bash

fine=0
all=0

for d in /m/nbe/scratch/restmeg/data/camcan/processed/cc700/mri/pipeline/release004/BIDSsep/megraw/sub-*/
do
    
    if [ -e ${d}meg/*psd-lh.stc ]
    then
	fine=$((fine+1))
	all=$((all+1))
    else
	all=$((all+1))
	miss=${d%/}
	echo ${miss##*/}
    fi
    
done

echo $fine "/" $all
	   
       
