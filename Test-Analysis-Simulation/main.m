%% Beamforming v4
%in this version:
%   *   calculated or preloaded input
%   *   simulation or .cal file
%   *   beaforming frequencies vs resulting frequencies
%   *   ingoring faulty mics
%   *   spectrogram for STFT
%   *   precomputed C, itteration over g, flatGrid
%   *   iteration over time (TODO: parfor); iteration over frequency, vectors everywhere else
%   *   output is singleton over Z 
%   *   
clear
global c
global xrange yrange zrange F T


%% ------SETTINGS--------------------------
%program settings
calculate = 1;                  % 0 - use precalculated input; 1 - calculate
simulationFolderName =  0;      % 0 - .cal file, otherwise a string with the folder name

%beamfrom settings
F_min = 1900;
F_max = 2000;

t_min = 0;
t_max = 4;

xres = .05;
yres = .05;

faultyMics = [6,39];            %list of faulty microphones positions, leave empty for none

%Fourier transform settings
window = 65536;                 %time sample length
noverlap = 15536;               %time sample overlap
nfft = 4096;     %2^integer     number of datapoints for FFT, respectively frequencies
fs = 50000;      %Hz            sampling frquency

%constants
c = 340;         %m/s           sound speed
p_ref = 2e-5;    %Pa            hearing threshold
w_ref = 1e-12;   %W             power threshold

%grid settings
%corresponds to picture overlay
%don't change if not necessary
xmin = -4.8;%-5.4;
xmax = 5.45;%4.85;
ymin = -1.85;
ymax = 4.7;
zmin = 8;
zmax = zmin;
zres = 1;
%% -------END SETTINGS---------------------
tic; %start timer

xrange = xmin:xres:xmax;
yrange = ymin:yres:ymax;
zrange = zmin:zres:zmax;
%p_n is constant for every itteration, thus compute it beforehand from the
%signal
%p_n = (n,f) is a function of microphone and the frequency (also possibly time.


[p_n,F,Xn,T] = preload(calculate,window, noverlap,nfft,fs,simulationFolderName);

%alternative corretction for faulty mics
for i=faultyMics
    p_n(i,:,:) = [];
    Xn(:,i) = [];
end


%select the frequency and time range for beamforming
Frange = F > F_min & F < F_max;
Trange = T > t_min & T < t_max;
F = F(Frange);
T = T(Trange);
p_n = p_n(:,Frange,Trange);
nf = size(F,2);         % #frequencies
nm = size(Xn,2);        % #microphones
nt = size(T,2);         % #time steps

%calculate the Cross-Spectral Matrix for each freqency
CSM = zeros(nm,nm,nf,nt);  %frequency last
%p_n = p_n.';

for i=1:nt
    for j=1:nf
        CSM(:,:,j,i) = p_n(:,j,i)*p_n(:,j,i)';
    end
end

%create grid
fprintf('Setting up the grid space...\n')

[x,y,z]=meshgrid(xrange,yrange,zrange);
spaceGrid = permute(cat(4,x,y,z),[4,1,2,3]);
spaceGrid = num2cell(spaceGrid,1);
spaceGrid_store = spaceGrid;
%flatten space coordinates
gridSize = size(spaceGrid);
spaceGrid = spaceGrid(:);       %flatten cells
nl = size(spaceGrid,1);         % #locations
spaceGrid = reshape(cell2mat(spaceGrid),[3,nl]).'; %% checked

%calcualte distances
Rm = zeros(nm,nl);
for i=1:nm
    Rm(i,:)= sqrt(sum(bsxfun(@minus,Xn(:,i).',spaceGrid).^2,2));
end
toc;

%beamform
fprintf(['Beamforming ' num2str(length(xrange)*length(yrange)*length(zrange)) ' cells over ' num2str(size(F,2)) ' frequencies and ' num2str(size(T,2)) ' time steps...\n'])

A.A = zeros(nl,nf,nt);

for i=1:nt
    for j=1:nf
        A.A(:,j,i) = beamform(CSM(:,:,j,i),F(:,j),Rm);
    end
end
toc; 

%visualize
fprintf('For information on visualization options type\n >> help imshow4 \n >> help formsOfA\n')
%order A properly
A.c = A.A;
A.A = real(A.A);
A.A = reshape(A.A,[gridSize nf nt]);
A.A = permute(A.A,[2,3,5,4,1]);
A.dB = 10*log10(A.A/p_ref^2);
formsOfA                    % in a different script to allow easy change and a help function

colormap('jet');
imshow4(A.maxPerFrame,1,1,-10);