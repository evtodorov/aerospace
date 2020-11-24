Z = 8; % in meters, what ever value is of interest

load('camera_parameters.mat');

dist_amount = 1;

fc_new = dist_amount * fc;

inv_KK = [1/fc_new(1) 0 1/cc(1);0 1/fc_new(2) 1/cc(2) ; 0 0 1];

corners(:,1) = inv_KK * [0;0;1]; 

corners(:,2) = inv_KK * [480;752;1]; % camera resolution is 480x752, inv_KK converts to real space i.e. meters

corners = corners * Z;

% center camera location

corners(1,:) = corners(1,:) - abs(corners(1,1) - corners(1,2))/2;

corners(2,:) = corners(2,:) - abs(corners(2,1) - corners(2,2))/2;