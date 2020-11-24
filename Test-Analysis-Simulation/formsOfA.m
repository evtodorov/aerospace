%% The following forms of the data are available:
%   *   Single values (to be used in e.g. range)
%             A.maxOfAll        - the maximum value in all directions
%             A.minOfAll        - the minimum value in all directions
%             A.meanOfAll       - the mean of all values
%             A.meanOfPeaks     - the mean of the peaks in the XY plane
%   *   4D Datasets (to be displayed)
%             A.dB              - mean SP^2L (pressure squared level ~ power level) in dB 
%             A.maxPerFrame     - the maximum of each frame in the XY plane is set to 0
%             A.maxPerTime      - the maximum of all time steps for one frequency is set to 0
%             A.maxPerFreq      - the maximum of all frequencies for one time grame is set to 0
%   *   Other can be very easily constructed, for example:
%             A.dB - A.maxOfAll - the maximum computed at any point is set to 0

%single numbers
A.maxOfAll = max(A.dB(:));              % the maximum value in all directions
A.minOfAll = min(A.dB(:));              % the minimum value in all directions
A.meanOfAll = mean(A.dB(:));            % the mean of all values
A.meanOfPEaks = mean(mean(max(max(A.dB))));% the mean of the peaks in the XY plane

%4D matrices
maxPerFrame = max(max(A.dB));
maxPerTime = max(maxPerFrame,[],4);
maxPerFreq = max(maxPerFrame,[],3);
A.maxPerFrame = A.dB;       
A.maxPerTime = A.dB;        
A.maxPerFreq = A.dB;        

for i=1:size(T,2)
    for j=1:size(F,2)
        A.maxPerFrame(:,:,i,j) = A.dB(:,:,i,j)-maxPerFrame(1,1,i,j);    % the maximum of each frame in the XY plane is set to 0
        A.maxPerFreq(:,:,i,j) = A.dB(:,:,i,j)-maxPerFreq(1,1,1,j);      % the maximum of all frequencies for one time frame is set to 0
        A.maxPerTime(:,:,i,j) = A.dB(:,:,i,j)-maxPerTime(1,1,i,1);      % the maximum of all time steps for one frequency is set to 0
    end
end