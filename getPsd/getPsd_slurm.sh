#!/bin/bash
#SBATCH --time=0-00:30:00    # 30 mins
#SBATCH --exclude=pe52,pe59,pe62,ivb25,wsm105,wsm110,pe67,pe51,pe55,pe62,ivb34,pe42,pe43,pe45,pe53,pe57,pe58
#SBATCH --mem-per-cpu=4000    # 4000MB of memory
#SBATCH --array=0-647
#SBATCH --output=./slurm_logs/slurm-%A_%a.out

ml purge
module load teflon
ml anaconda2


cd /scratch/nbe/restmeg/data/camcan/cc700/mri/pipeline/release004/BIDSsep/megraw/


## run the program and redirect all IO to a local drive
## assuming that you have your program and input at $wrk_dir

dirnames=(sub*/)
sub=${dirnames[$SLURM_ARRAY_TASK_ID]}
sub=${sub%?}
echo "${sub}"
export SUBJECTS_DIR=/scratch/nbe/restmeg/data/camcan/subjects_s3
export CAMCAN_ROOT=/scratch/nbe/restmeg/data/camcan/
srun python ${CAMCAN_ROOT}../code/getPsd/getPsd.py ${sub}

