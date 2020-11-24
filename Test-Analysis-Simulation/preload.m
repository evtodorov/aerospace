%% Preload for beamforming v4
%   *   simulation input parser HARDCODED trailing 0s and different length
%   *   saving calculations
%%  *   TODO: Currently using FFT instead of STFT, singleton time
function [ p_n,F,Xn,T] = preload( calculate,window, noverlap,nfft,fs,simulationFolderName )
%LOAD_PN Load the complex pressure values
%   If calculate is True, calculates the parameters, otherwise loads them
%   from a preexisting file named 'preload_window_noverlap_nfft'



if ~exist('simulationFolderName','var')
    simulationFolderName = 0;
end

if simulationFolderName
    fname = [simulationFolderName  '_preload_' num2str(window) '_' num2str(noverlap) '_' num2str(nfft)];
else
    fname = ['preload_' num2str(window) '_' num2str(noverlap) '_' num2str(nfft)];
end
if calculate
    
    %% Import data
    if ~simulationFolderName
        [info, config, data] = read_data;
        for i=1:8
            Xn(1,8*i-7:8*i)=config.x(i:8:end);
            Xn(2,8*i-7:8*i)=config.y(i:8:end);
            Xn(3,8*i-7:8*i)=config.z(i:8:end);
        end
    else
        fprintf('Load simulated data...\n');
        data.file_full = [];
        st = 0;
        en = Inf;
        for i=1:64
            temp = dlmread([simulationFolderName '/' num2str(i-1) '.txt']);
            data.file_full = [data.file_full, temp];
            %dealing with trailing 0s and variable length
            if size(temp==0,1) > st
                st = size(temp==0,1);
            end
            if size(temp) < en
                en = size(temp);
            end
        end
        data.file_full = data.file_full(st:en,:);
        
        fid = fopen([simulationFolderName '/pos.txt']);
        Xn = reshape(cell2mat(textscan(fid,'%n','Delimiter',',','Whitespace',' \b\t()')),3,[]);  
    end    
    
    
    %% Frequency domain
    fprintf('Perform FFT...\n')
    n = length(Xn);
    p_n = [];
    for i=1:n
         [S,F,T] = spectrogram(data.file_full(:,i),window,noverlap,nfft,fs);
         F=F.';
         p_n(i,:,:) = S;    
    end

    fprintf('Save variables...\n');
    save(fname,'p_n','F','Xn','T');
    toc;
    return
else
    fprintf('Load variables...\n')
    load(fname)
    return
end

