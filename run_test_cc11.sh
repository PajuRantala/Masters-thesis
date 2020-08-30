#!/bin/bash
#SBATCH --time=24:00:00 --mem-per-cpu=16000
#SBATCH -o test_cc11_3.out
#SBATCH --array=1

names=(CC110033 CC110037 CC110045 CC110056 CC110062 CC110069 CC110087 CC110098 CC110101 CC110126 CC110174 CC110182 CC110187 CC110319 CC110411 CC110606 CC112141)
module load freesurfer/
export SUBJECTS_DIR=/scratch/nbe/restmeg/data/camcan/subjects
cd /scratch/nbe/restmeg/data/camcan/cc700/mri/pipeline/release004/BIDSsep/anat/
recon-all -i sub-${names[$SLURM_ARRAY_TASK_ID]}/anat/sub-${names[$SLURM_ARRAY_TASK_ID]}_T1w.nii.gz -i sub-${names[$SLURM_ARRAY_TASK_ID]}/anat/sub-${names[$SLURM_ARRAY_TASK_ID]}_T2w.nii.gz -T2 -subjid ${names[$SLURM_ARRAY_TASK_ID]} -all

