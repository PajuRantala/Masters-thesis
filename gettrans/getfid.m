function rc = getfid(subj)

    addpath(fullfile(spm('Dir'),'external','fieldtrip'));
    clear ft_defaults
    clear global ft_default
    ft_defaults;
    global ft_default
    ft_default.trackcallinfo = 'no';
    ft_default.showcallinfo = 'no';
    
    camcan_root = getenv('CAMCAN_ROOT');
    fname = strcat(camcan_root, 'cc700/mri/pipeline/release004/BIDSsep/anat/', ...
        subj, '/anat/', subj, '_T1w.nii');
    %fname = strcvat(subj, '_T1w.nii');
    mesh = spm_eeg_inv_mesh(fname, 3);
    fid_fname = strcat(camcan_root, 'subjects_s3/', subj, '/bem/', subj, '-fiducials.fif')
    %fid_fname = strcat(subj, '-fiducials.fif');
    fid = [mesh.fid.fid.pnt ones(5,1)];
    fid = fid*mesh.Affine';
    fid = fid(:,1:3);
    
    fiff_write_fiducial(fid./1000, fid_fname);
    rc = 0;
    
end

function rc = fiff_write_fiducial(r, file)
%fiff_write_fiducial Writes the point r to file file.
%   Detailed explanation goes here

    FIFFV_POINT_CARDINAL =1;
    FIFFV_POINT_HPI      =2;
    FIFFV_POINT_EEG      =3;
    FIFFV_POINT_EXTRA    =4;
    FIFFV_POINT_LPA      =1;
    FIFFV_POINT_NASION   =2;
    FIFFV_POINT_RPA     = 3;
    FIFF = fiff_define_constants();
    
    f = fiff_start_file(file);
    fiff_start_block(f, FIFF.FIFFB_ISOTRAK)
    dig.kind=FIFFV_POINT_CARDINAL;
    
    dig.ident = FIFFV_POINT_NASION;
    dig.r=r(1,:);    
    fiff_write_dig_point(f,dig)
    
    dig.ident = FIFFV_POINT_LPA;
    dig.r=r(4,:);
    fiff_write_dig_point(f,dig)
    
    dig.ident = FIFFV_POINT_RPA;
    dig.r=r(5,:);
    fiff_write_dig_point(f,dig)
    
    fiff_write_int_matrix(f, FIFF.FIFF_MNE_COORD_FRAME,[FIFF.FIFFV_COORD_MRI])
    fiff_end_block(f, FIFF.FIFFB_ISOTRAK)
    fiff_end_file(f)
    rc = 0;

end

