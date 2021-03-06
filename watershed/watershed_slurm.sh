#!/bin/bash
#SBATCH --time=0-00:15:00    # 15 mins
#SBATCH --exclude=pe52,pe59,pe62,ivb25,wsm105,wsm110,pe67,pe51,pe55,pe62,ivb34,pe42,pe43,pe45,pe53
#SBATCH --mem-per-cpu=8000    # 8000MB of memory
#SBATCH --array=0-660
#SBATCH --output=./slurm_logs/slurm-%A_%a.out

module load teflon
module load mne
source $MNE_ROOT/bin/mne_setup_sh

module load freesurfer

cd /scratch/nbe/restmeg/data/camcan/subjects_s3/


## run the program and redirect all IO to a local drive
## assuming that you have your program and input at $wrk_dir

dirnames=(*/)
sub=${dirnames[$SLURM_ARRAY_TASK_ID]}
sub=${sub%?}
echo "${sub}"
export SUBJECTS_DIR=/scratch/nbe/restmeg/data/camcan/subjects_s3
srun mne_watershed_bem --subject ${sub}

