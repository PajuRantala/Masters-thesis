#!/bin/bash
#SBATCH --time=0-00:15:00    # 15 mins
#SBATCH --exclude=pe52,pe59,pe62,ivb25,wsm105,wsm110,pe67,pe51,pe55,pe62,ivb34,pe42,pe43,pe45,pe53
#SBATCH --mem-per-cpu=8000    # 8000MB of memory
#SBATCH --array=0-1
#SBATCH --output=./slurm_logs/slurm-%A_%a.out

ml purge
ml anaconda2


cd /m/nbe/scratch/restmeg/data/camcan/cc700/mri/pipeline/release004/BIDSsep/megraw/


## run the program and redirect all IO to a local drive
## assuming that you have your program and input at $wrk_dir

dirnames=(sub*/)
sub=${dirnames[0]}
sub=${sub%?}
echo "${sub}"
export SUBJECTS_DIR=/m/nbe/scratch/restmeg/data/camcan/subjects_s3
export CAMCAN_ROOT=/m/nbe/scratch/restmeg/data/camcan/
python ${CAMCAN_ROOT}../code/getPsd/getPsd.py ${sub}

