#!/bin/bash
#SBATCH --time=24:00:00 --mem-per-cpu=16000
#SBATCH -o test_cc_all_5.out
#SBATCH --array=0-18

names=(CC210023 CC210051 CC210088 CC310008 CC310051 CC310052 CC410015 CC410032 CC410040 CC510015 CC510039 CC510043 CC610022 CC610028 CC610039 CC710037 CC710088 CC710099)
#names=(CC210023 CC210051 CC210088 CC510039 CC510043 CC610028 CC610039 CC710037 CC710088 CC710099)

module load freesurfer/
export SUBJECTS_DIR=/scratch/nbe/restmeg/data/camcan/subjects
cd /scratch/nbe/restmeg/data/camcan/cc700/mri/pipeline/release004/BIDSsep/anat/
#recon-all -i sub-${names[$SLURM_ARRAY_TASK_ID]}/anat/sub-${names[$SLURM_ARRAY_TASK_ID]}_T1w.nii.gz -T2 sub-${names[$SLURM_ARRAY_TASK_ID]}/anat/sub-${names[$SLURM_ARRAY_TASK_ID]}_T2w.nii.gz -subjid ${names[$SLURM_ARRAY_TASK_ID]} -all
recon-all -subjid ${names[$SLURM_ARRAY_TASK_ID]} -all 
#-no-isrunning

