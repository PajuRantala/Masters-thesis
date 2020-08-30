#!/bin/bash
subj1=${PWD#*/anat/}
echo subj="${subj1%/anat}"
