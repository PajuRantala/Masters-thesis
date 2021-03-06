#!/bin/bash
#SBATCH --time=0-02:00:00    # 2 hours
#SBATCH --mem-per-cpu=16000    # 16000MB of memory
#SBATCH --array=0-66
#sbatch --exclude=pe67
#SBATCH --output=./slurm_logs/slurm-%A_%a.out

module load matlab/r2017b
module load spm/12
module load mne
module load freesurfer

export CAMCAN_ROOT=/scratch/nbe/restmeg/data/camcan/

srun matlab -nosplash -nodesktop -r "try; cd $PWD; disp(pwd); calcFids($SLURM_ARRAY_TASK_ID); catch e; disp(e); end; exit";


