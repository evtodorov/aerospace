%
% Jiri Chmelik (2015). imshow4 (https://www.mathworks.com/matlabcentral/fileexchange/47188-imshow4), MATLAB Central File Exchange. Retrieved March 01, 2015.
%
%%imshow4(im,timeSlice,FreqSlice,range,colormap)
%   im          - 4D tensor to be visualized, dimesnions (x,y,t,f)
%   timeSlice*  - the number of the time slice to be displayed
%   freqSlice*  - the number of the frequency slice to be displayed
%   range       - range behaviour as follows:
%       'all' (default) - from minimum to the maximum on each frame 
%                         (equivalent to [-inf inf],[])
%       [val1 val2]     - from val1 to val2 independent of values on the frame
%                         (can be used together with absolutes to set an
%                          absolute range, e.g. [maxAnywhere-10 maxAnywhere])
%       positive_value  - from the min of the frame to min+positive_value
%       negative_value  - from the max-negative_value to max of the frame
%       'norm'          - same as 'all', but values are normalized from 0 to 1
%   colormap    - 'jet','gray', or any other available colormap
function [] = imshow4(varargin)
% Function for 2D, 3D or 4D image display. Required Matlab version 2012a
% or newer. Recomended Matlab 2013a or newer.
% -------------------------------------------------------------------------
% imshow4(im) - show 2D, 3D or 4D image with default settings
% imshow4(im,slice) - show 3D or 4D image with default settings with
% started at slice number
% imshow4(im,slice,ref_time) - show 3D or 4D image with default settings
% with started at slice number and reference time sample
% imshow4(im,slice,ref_time,range) - show 4D image with default settings
% with started at slice number and reference time sample with specified
% intensity range settings
% imshow4(im,slice,ref_time,range,colormaps) - show 4D image with default
% settings with started at slice number and reference time sample with
% specified intensity range and colormap settings
% imshow4(im,slice,ref_time,range,colormaps,time) - show 4D image time
% fusion, where time is second image inital time sample
% imshow4(im,slice,ref_time,range,colormaps,time,method) - show 4D image
% time fusion, method is same as method in imfuse function
% -------------------------------------------------------------------------
% im - input image 2D/3D/4D
% slice - number of slice (default = 1)
% ref_time - number of reference time sample (default = 1)
% range - intensity range - 'all'/0/[x,y]/'norm'
% (default = 'all' - same as imshow(im,[]))
% colormaps - same as colormap function parameters - 'jet',...0 - def.
% (default = 'gray')
% time - number of time sample (default = 1)
% method - method from imfuse function -
% 'falsecolor'/'blend'/'diff'/'montage' (default = 'falsecolor')
global slice time im mode_out inter colormaps isfused
global xrange yrange zrange F T
warning off
drange = 10;
im = varargin{1};
N = nargin;
slice = 1;
time = 1;
ref_time = 1;
range = 'all';
mode_out = 0;
method = 'falsecolor';
inter = 0;
h = figure('Position',get(0,'ScreenSize'),'WindowStyle','docked','Interruptible','off');
colormaps = colormap('jet');
isfused = 0;
if N==2
    slice = varargin{2};
elseif N==3
    slice = varargin{2};
    ref_time = varargin{3};
elseif N==4
    slice = varargin{2};
    ref_time = varargin{3};
    range = varargin{4};
elseif N==5
    slice = varargin{2};
    ref_time = varargin{3};
    range = varargin{4};
    colormaps = varargin{5};
elseif N==6
    slice = varargin{2};
    ref_time = varargin{3};
    range = varargin{4};
    time = varargin{6};
    isfused = 1;
elseif N==7
    slice = varargin{2};
    ref_time = varargin{3};
    range = varargin{4};
    time = varargin{6};
    method = varargin{7};
    isfused = 1;
end;
if strcmp(range,'norm')
    maximum = max(im(:));
    minimum = min(im(:));
    im = (im - minimum)./(maximum - minimum);
    range = 0;
end;
if colormaps==0
    colormaps = colormap('gray');
end;
colormaps = colormap(colormaps);
figure(h)
colorbar;
grid on
axis on;
xlabel('X-axis')
ylabel('Y-axis')
title('Transversal view: \leftarrow\rightarrow = t-axis; \uparrow\downarrow = f-axis, 0-5 = view')
set(h,'Name',['t=' num2str(zrange(slice)) ' m, f=' num2str(F(ref_time)) 'Hz'],'Colormap',colormaps)
%set(h,'Name',['Z=' num2str(slice) '/' num2str(size(im,3)) ', t=' num2str(time) '/' num2str(size(im,4))])
if N<6
    if strcmp(range,'all')
        imshow(im(:,:,slice,ref_time),[],'XData',[xrange(1) xrange(end)],'YData',[yrange(1) yrange(end)]);
    elseif range==0
        imshow(im(:,:,slice,ref_time),0,'XData',[xrange(1) xrange(end)],'YData',[yrange(1) yrange(end)]);
    elseif (size(range,2)==1) && (range < 0)
        maxrange = max(max(im(:,:,slice,ref_time)));
        temprange = [maxrange+range maxrange];
        imshow(im(:,:,slice,ref_time),temprange,'XData',[xrange(1) xrange(end)],'YData',[yrange(1) yrange(end)]);
    elseif (size(range,2)==1) && (range > 0)
        minrange = min(min(im(:,:,slice,ref_time)));
        temprange = [minrange range+minrange];
        imshow(im(:,:,slice,ref_time),temprange,'XData',[xrange(1) xrange(end)],'YData',[yrange(1) yrange(end)]);
    else
        imshow(im(:,:,slice,ref_time),range,'XData',[xrange(1) xrange(end)],'YData',[yrange(1) yrange(end)]);
    end;
else
    imf = imfuse(im(:,:,slice,ref_time),im(:,:,slice,time),method);
    
    if strcmp(range,'all')
        imshow(imf,[]);
    elseif range==0
        imshow(imf);
    else
        imshow(imf,range);
    end;
end;
colorbar;
xlabel('X-axis')
ylabel('Y-axis')
title('Transversal view: \leftarrow\rightarrow = t-axis, \uparrow\downarrow = f-axis, 0-5 = view')
set(h,'Name',['t=' num2str(zrange(slice)) ' s, f=' num2str(F(ref_time)) 'Hz'],'Colormap',colormaps)
if size(im,3)>1 || size(im,4)>1
    set(h,'KeyPressFcn',{@kresli,h,range,N,ref_time,method})
end;
warning on
set(gca,'YDir','normal');
end

function kresli(~,eventdata,h,range,N,ref_time,method)
global slice time im mode_out inter colormaps isfused
global xrange yrange zrange F T drange
warning off
rng=size(im,3);
rng=[1 rng];
rng_t=size(im,4);
rng_t=[1 rng_t];
if slice>=min(rng) && slice<=max(rng) && time>=min(rng_t) && time<=max(rng_t)
    switch eventdata.Key
        case  'rightarrow'
            slice=slice+1;
            if slice>max(rng)
                slice=max(rng);
            end
        case 'leftarrow'
            slice=slice-1;
            if slice<min(rng)
                slice=min(rng);
            end
        case 'downarrow'
            time=time-1;
            if time<min(rng_t)
                time=min(rng_t);
            end
        case 'uparrow'
            time=time+1;
            if time>max(rng_t)
                time=max(rng_t);
            end
        case {'0','numpad0'}
            if mode_out ~= 0;
            im = ipermutation(im,mode_out);
            end;
            mode_out = 0;
            inter = 0;
        case {'1','numpad1'}
            mode_in = 1;
            if mode_in ~= mode_out
            im = ipermutation(im,mode_out);
            im = permutation(im,mode_in);
            end;
            mode_out = 1;
            inter = 0;
        case {'2','numpad2'}
            mode_in = 2;
            if mode_in ~= mode_out
            im = ipermutation(im,mode_out);
            im = permutation(im,mode_in);
            end;
            mode_out = 2;
            inter = 0;
        case {'3','numpad3'}
            mode_in = 3;
            if mode_in ~= mode_out
            im = ipermutation(im,mode_out);
            im = permutation(im,mode_in);
            end;
            mode_out = 3;
            inter = 1;
        case {'4','numpad4'}
            mode_in = 4;
            if mode_in ~= mode_out
            im = ipermutation(im,mode_out);
            im = permutation(im,mode_in);
            end;
            mode_out = 4;
            inter = 1;
        case {'5','numpad5'}
            mode_in = 5;
            if mode_in ~= mode_out
            im = ipermutation(im,mode_out);
            im = permutation(im,mode_in);
            end;
            mode_out = 5;
            inter = 1;
        case {'f'}
            if isfused==0
                close(h)
                imshow4(im,slice,ref_time,range,colormaps,1)
                isfused = 1;
            elseif isfused==1
                close(h)
                imshow4(im,slice,ref_time,range,colormaps)
                isfused = 0;
            end;
    end
end

if rng(end)~=size(im,3) || rng_t(end)~=size(im,4)
    rng=size(im,3);
    rng=[1 rng];
    rng_t=size(im,4);
    rng_t=[1 rng_t];
    if slice>max(rng)
        slice=max(rng);
    end
    if slice<min(rng)
        slice=min(rng);
    end
    if time<min(rng_t)
        time=min(rng_t);
    end
    if time>max(rng_t)
        time=max(rng_t);
    end
end;
figure(h)
if N<6
    imzobr = im(:,:,slice,time);
    if size(imzobr,2)<200 && inter==1
        imzobr = imresize(imzobr,[size(imzobr,1),200]);
    end;
    if strcmp(range,'all')
        imshow(imzobr,[],'XData',[xrange(1) xrange(end)],'YData',[yrange(1) yrange(end)]);
    elseif range==0
        imshow(imzobr,0,'XData',[xrange(1) xrange(end)],'YData',[yrange(1) yrange(end)]);
    elseif (size(range,2)==1) && (range < 0)
        maxrange = max(max(imzobr));
        range = [maxrange+range maxrange];
        imshow(imzobr,range,'XData',[xrange(1) xrange(end)],'YData',[yrange(1) yrange(end)]);
    elseif (size(range,2)==1) && (range > 0)
        minrange = min(min(imzobr));
        range = [minrange range+minrange];
        imshow(imzobr,range,'XData',[xrange(1) xrange(end)],'YData',[yrange(1) yrange(end)]);
    else
        imshow(imzobr,range,'XData',[xrange(1) xrange(end)],'YData',[yrange(1) yrange(end)]);
    end;
else
    
    imf = imfuse(im(:,:,slice,ref_time),im(:,:,slice,time),method);

    if size(imf,2)<100 && inter==1
        imf = imresize(imf,[size(imf,1),100]);
    end;
    if strcmp(range,'all')
        imshow(imf,[]);
    elseif range==0
        imshow(imf);
    else
        imshow(imf,range);
    end;
end;
switch mode_out
    case 0
        colorbar
        grid on
        axis on;
        xlabel('X-axis')
        ylabel('Y-axis')
        title('Transversal view: \leftarrow\rightarrow = t-axis; \uparrow\downarrow = f-axis, 0-5 = view')
        set(h,'Name',['t=' num2str(T(slice)) '(' num2str(slice) '/' num2str(rng(2)) '), f=' num2str(F(time)) '(' num2str(time) '/' num2str(rng_t(2)) ')'],'Colormap',colormaps)
        %xlim(gca,[-10 10])
        %ylim(gca,[-10 10])
    case 1
        xlabel('X-axis')
        ylabel('Z-axis')
        title('Frontal view: \leftarrow\rightarrow = Y-axis; \uparrow\downarrow = t-axis, 0-5 = view')
        set(h,'Name',['Y=' num2str(slice) '/' num2str(rng(2)) ', t=' num2str(time) '/' num2str(rng_t(2))],'Colormap',colormaps)
    case 2
        xlabel('Y-axis')
        ylabel('Z-axis')
        title('Sagital view: \leftarrow\rightarrow = X-axis; \uparrow\downarrow = t-axis, 0-5 = view')
        set(h,'Name',['X=' num2str(slice) '/' num2str(rng(2)) ', t=' num2str(time) '/' num2str(rng_t(2))],'Colormap',colormaps)
    case 3
        xlabel('t-axis')
        ylabel('X-axis')
        title('X-time view: \leftarrow\rightarrow = Z-axis; \uparrow\downarrow = Y-axis, 0-5 = view')
        set(h,'Name',['Z=' num2str(slice) '/' num2str(rng(2)) ', Y=' num2str(time) '/' num2str(rng_t(2))],'Colormap',colormaps)
    case 4
        xlabel('t-axis')
        ylabel('Y-axis')
        title('Y-time view: \leftarrow\rightarrow = Z-axis; \uparrow\downarrow = X-axis, 0-5 = view')
        set(h,'Name',['Z=' num2str(slice) '/' num2str(rng(2)) ', X=' num2str(time) '/' num2str(rng_t(2))],'Colormap',colormaps)
    case 5
        xlabel('t-axis')
        ylabel('Z-axis')
        title('Z-time view: \leftarrow\rightarrow = Y-axis; \uparrow\downarrow = X-axis, 0-5 = view')
        set(h,'Name',['Y=' num2str(slice) '/' num2str(rng(2)) ', X=' num2str(time) '/' num2str(rng_t(2))],'Colormap',colormaps)
end;
set(gca,'YDir','normal');
end

function [im_out] = permutation(im_in,mode_in)
    switch mode_in
        case 0
            mode_in = [1,2,3,4]; % transversal
        case 1
            mode_in = [3,2,1,4]; % frontal
        case 2
            mode_in = [3,1,2,4]; % sagital
        case 3
            mode_in = [2,4,3,1]; % x-time
        case 4
            mode_in = [1,4,3,2]; % y-time
        case 5
            mode_in = [3,4,1,2]; % z-time
    end;
    im_out = permute(im_in,mode_in);
end

function [im_out] = ipermutation(im_in,mode_in)
    switch mode_in
        case 0
            mode_in = [1,2,3,4]; % transversal
        case 1
            mode_in = [3,2,1,4]; % frontal
        case 2
            mode_in = [3,1,2,4]; % sagital
        case 3
            mode_in = [2,4,3,1]; % x-time
        case 4
            mode_in = [1,4,3,2]; % y-time
        case 5
            mode_in = [3,4,1,2]; % z-time
    end;
    im_out = ipermute(im_in,mode_in);
end
