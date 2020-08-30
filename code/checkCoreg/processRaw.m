files = dir('../../camcan/processed/coreg_logs/')
files = files(endsWith({files.name},{'0.csv','1.csv','2.csv','3.csv','4.csv','5.csv','6.csv','7.csv','8.csv','9.csv'}))

data(1).name = ''

for i = 1:numel(files)
        currF = files(i).name
        fid = fopen(strcat('../../camcan/processed/coreg_logs/', currF));
        data(i).name = currF(1:end-4);
        fid_pnts = fscanf(fid, '%f');
        fscanf(fid,'[');
        dig_pnts = fscanf(fid, '%f');
        fclose(fid);
        
        data(i).lpa = fid_pnts(1);
        data(i).rpa = fid_pnts(2);
        data(i).nas = fid_pnts(3);
        data(i).dig = dig_pnts;
end


        
        
        