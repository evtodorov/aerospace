% TU Delft Acoustic array read_data function
% Copyright TUDelft 2015
function [info, config, data] = read_data
%directory fix
parent = pwd;
cd ..
%% array configuration and measurement info
config.dir = 'config.txt';
info.dir = 'info.txt';

%% Read in info file
fprintf('Read in info file\n')

% open file
fid = fopen(info.dir);
info_file = textscan(fid, '%s %s %s');
fclose(fid);

% organise data
index = find(strcmp([info_file{1,1}], 'acoustic_sample_frequency'));
acoustic_sample_frequency = str2double_c(info_file{1,2}{index,1});
info.sf = acoustic_sample_frequency;

index = find(strcmp([info_file{1,1}], 'number_of_microphones'));
info.N = str2double(info_file{1,2}{index,1});

index = find(strcmp([info_file{1,1}], 'amplification'));
info.amplification = [info_file{1,2}{index,1} ' ' info_file{1,3}{index,1}];

index = find(strcmp([info_file{1,1}], 'acoustic_camera'));
info.acoustic_camera = [info_file{1,2}{index,1}];

index = find(strcmp([info_file{1,1}], 'optical_camera'));
info.optical_camera = info_file{1,2}{index,1};

index = find(strcmp([info_file{1,1}], 'start_time'));
info.start_time = info_file{1,2}{index,1};

index = find(strcmp([info_file{1,1}], 'start_timestamp'));
info.start_timestamp = [info_file{1,3}{index,1} ' ' info_file{1,2}{index,1}];

% open file
fid = fopen(info.dir);
info.comments = fgetl(fid);
while ~strncmp(char(info.comments),'comments',1)
    info.comments = fgetl(fid);
end
fclose(fid);

info.comments = char(info.comments);
info.comments = info.comments(1,10:end);

%% Read in array configuration
fprintf('Read in array configuration\n')

fid = fopen(config.dir);
C = textscan(fid, '%s%d%f%f');
config.index = C{1,1};
config.channel(1:info.N) = C{1,2}; 
config.x(1:info.N) = C{1,3};                    % x-position
config.y(1:info.N) = C{1,4};                    % y-position   
fclose(fid);

config.z(1:info.N) = 0;                         % z-position

%% Read in measurement data
fprintf('Read in measurement data\n')

file = 'acoustic_data.cal';
fid = fopen(file,'r');
data.file_full = fread(fid, [info.N inf], 'single', 0, 'l').';
fclose(fid);    
info.calibrated = 1;

%retrun to orginal folder
cd(parent);
end

function x = str2double_c(s)

if ischar(s)
    
    % Try to read simple case of something like 5.75
    [a,count,errmsg,nextindex] = sscanf(s,'%f',1);
    if count == 1 && isempty(errmsg) && nextindex > numel(s)
        x = a;
        return;
    end

    s = deblank(s);
    % Remove any commas so that numbers formatted like 1,200.34 are
    % handled.
    periods = (s == '.');
    commas = (s == ',');
    s(commas) = '.';
    s(periods) = [];
    
    lenS = numel(s); %get len again since it has changed after deblanking
    
    % Try to get 123, 123i, 123i + 45, or 123i - 45
    [a,count,errmsg,nextindex] = sscanf(s,'%f %1[ij] %1[+-] %f',4);
    % simlest case is a double
    if count == 1 && isempty(errmsg) && nextindex > lenS
        x = a;
        return;
    end
    % now deal with complex
    if isempty(errmsg) && nextindex > lenS
       if count==2
            x = a(1)*1i;
        elseif count==4
            sign = (a(3)=='+')*2 - 1;
            x = a(1)*1i + sign*a(4);
        else
            x = NaN;
        end
        return
    end

    % Try to get 123 + 23i or 123 - 23i
    [a,count,errmsg,nextindex] = sscanf(s,'%f %1[+-] %f %1[ij]',4);
    if isempty(errmsg) && nextindex > lenS
        if count==4
            sign = (a(2)=='+')*2 - 1;
            x = a(1) + sign*a(3)*1i;
        else
            x = NaN;
        end
        return
    end

    % Try to get i, i + 45, or i - 45
    [a,count,errmsg,nextindex] = sscanf(s,'%1[ij] %1[+-] %f',3);
    if isempty(errmsg) && nextindex > lenS
        if count==1
            x = 1i;
        elseif count==3
            sign = (a(2)=='+')*2 - 1;
            x = 1i + sign*a(3);
        else
            x = NaN;
        end
        return
    end

    % Try to get 123 + i or 123 - i
    [a,count,errmsg,nextindex] = sscanf(s,'%f %1[+-] %1[ij]',3);
    if isempty(errmsg) && nextindex > lenS
        if count==1
            x = a(1);
        elseif count==3
            sign = (a(2)=='+')*2 - 1;
            x = a(1) + sign*1i;
        else
            x = NaN;
        end
        return
    end

    % Try to get -i, -i + 45, or -i - 45
    [a,count,errmsg,nextindex] = sscanf(s,'%1[+-] %1[ij] %1[+-] %f',4);
    if isempty(errmsg) && nextindex > lenS
        if count==2
            sign = (a(1)=='+')*2 - 1;
            x = sign*1i;
        elseif count==4
            sign1 = (a(1)=='+')*2 - 1;
            sign2 = (a(3)=='+')*2 - 1;
            x = sign1*1i + sign2*a(4);
        else
            x = NaN;
        end
        return
    end

    % Try to get 123 + 23*i or 123 - 23*i
    [a,count,errmsg,nextindex] = sscanf(s,'%f %1[+-] %f %1[*] %1[ij]',5);
    if isempty(errmsg) && nextindex > lenS
        if count==5
            sign = (a(2)=='+')*2 - 1;
            x = a(1) + sign*a(3)*1i;
        else
            x = NaN;
        end
        return
    end

    % Try to get 123*i, 123*i + 45, or 123*i - 45
    [a,count,errmsg,nextindex] = sscanf(s,'%f %1[*] %1[ij] %1[+-] %f',5);
    if isempty(errmsg) && nextindex > lenS
        if count==1
            x = a;
        elseif count==3
            x = a(1)*1i;
        elseif count==5
            sign = (a(4)=='+')*2 - 1;
            x = a(1)*1i + sign*a(5);
        else
            x = NaN;
        end
        return
    end

    % Try to get i*123 + 45 or i*123 - 45
    [a,count,errmsg,nextindex] = sscanf(s,'%1[ij] %1[*] %f %1[+-] %f',5);
    if isempty(errmsg) && nextindex > lenS
        if count==1
            x = 1i;
        elseif count==3
            x = 1i*a(3);
        elseif count==5
            sign = (a(4)=='+')*2 - 1;
            x = 1i*a(3) + sign*a(5);
        else
            x = NaN;
        end
        return
    end

    % Try to get -i*123 + 45 or -i*123 - 45
    [a,count,errmsg,nextindex] = sscanf(s,'%1[+-] %1[ij] %1[*] %f %1[+-] %f',6);
    if isempty(errmsg) && nextindex > lenS
        if count==2
            sign = (a(1)=='+')*2 - 1;
            x = sign*1i;
        elseif count==4
            sign = (a(1)=='+')*2 - 1;
            x = sign*1i*a(4);
        elseif count==6
            sign1 = (a(1)=='+')*2 - 1;
            sign2 = (a(5)=='+')*2 - 1;
            x = sign1*1i*a(4) + sign2*a(6);
        else
            x = NaN;
        end
        return
    end

    % Try to get 123 + i*45 or 123 - i*45
    [a,count,errmsg,nextindex] = sscanf(s,'%f %1[+-] %1[ij] %1[*] %f',5);
    if isempty(errmsg) && nextindex > lenS
        if count==5
            sign = (a(2)=='+')*2 - 1;
            x = a(1) + sign*1i*a(5);
        else
            x = NaN;
        end
        return
    end

    % None of the above cases, but s still is a character array.
    x = NaN;

elseif ~isempty(s) && iscellstr(s)
    x = cellfun(@str2double, s);
elseif iscell(s)
	x = [];
    for k=numel(s):-1:1,
		if iscell(s{k})
			x(k) = NaN;
		else
			x(k) = str2double(s{k});
		end
    end
    x = reshape(x,size(s));
else
    x = NaN;
end

end