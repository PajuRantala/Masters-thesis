#!/bin/bash

cd /m/nbe/scratch/restmeg/data/camcan/subjects_s3/

export SUBJECTS_DIR=/m/nbe/scratch/restmeg/data/camcan/subjects_s3
export CAMCAN_ROOT=/m/nbe/scratch/restmeg/data/camcan/
	
dirnames=(sub*/)
for i in {0..660}
do 
	 sub=${dirnames[$i]}
	 sub=${sub%?}
	 echo "${sub}"
	 python ${CAMCAN_ROOT}../code/gettrans/calcTrans.py ${sub}
done
