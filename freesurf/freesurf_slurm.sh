#!/bin/bash
#SBATCH --time=0-00:30:00    # 30 mins
#SBATCH --exclude=pe52,pe59,pe62,ivb25,wsm105,wsm110,pe67,pe51,pe55,pe62,ivb34,pe42,pe43,pe45,pe53,pe57,pe58
#SBATCH --mem-per-cpu=8000    # 8000MB of memory
#SBATCH --array=0
#SBATCH --output=./slurm_logs/slurm-%A_%a.out

ml purge
module load teflon
module load freesurfer

dirname=$(cat missing.txt)
dirnames=($dirname)
sub=${dirnames[$SLURM_ARRAY_TASK_ID]}
echo "${sub}"
export SUBJECTS_DIR=/scratch/nbe/restmeg/data/camcan/subjects_s3
export CAMCAN_ROOT=/scratch/nbe/restmeg/data/camcan/
srun recon-all -s ${sub} -all

