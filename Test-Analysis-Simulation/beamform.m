%% This beamforming follows the papers on DAMAS
% Assumption Rc approx mean(Rm)
function [ A ] = beamform(CSM,F,Rm)
%BEAMFORM main beamformin function
%   input CSM - cross-spectral matrix; Rm - distance ; F - beamforming frequency
%   output A (source autopower at Rm)
global c
%Rm (#mics rows, #cell cols)
Rc = mean(Rm,2);    %distance to the ~centre of the array
dt = Rm/c;
phasor = exp(-2*pi*F*1i*dt);
clear dt;
v = bsxfun(@rdivide,Rm,Rc).*phasor;
%v= phasor.*Rm;
clear Rc phasor;

A = sum(v'.*(CSM*v).',2)/(size(CSM,1)^2);  %RAM saving alternative of A = diag(v'*CSM*v);  % out of memory error; slower
%A = .5*A./abs(sum(v.^2,1)).^2.';
return
end