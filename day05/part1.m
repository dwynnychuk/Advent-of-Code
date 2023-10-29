% Advent of Code 2022
% Day 5
% Part 1

clear
clc

% File reading
% Initial crate stacks
fileID = fopen('input.txt', 'r');
lines = strings(0, 1);
line = fgetl(fileID);
for i = 1:8
    lines(end+1) = line;
    line = fgetl(fileID);
end
fclose(fileID);
clear i fileID line

stacknum = 9;
maxstackheight = 8;

% Determine length of array
for i = 1:maxstackheight
    maxl = length(lines{1,i});
    if length(lines{1,i}) > maxl
        maxl = length(lines{1,i});
    end
end
clear i maxl
idxchar = 2:4:34;
stacks = strings(maxstackheight,stacknum);

% Make Crate Stacks
for i = 1:maxstackheight
    for j = 1:stacknum
        stacks(i,j) = lines{1,i}(idxchar(j));
    end
end
clear i j lines idxchar

% extend stacks
ogstack = maxstackheight;
maxstackheight = 100;
temp = stacks;
stacks = strings(maxstackheight,stacknum);
stacks((maxstackheight-ogstack+1):end,:) = temp;

% Begin parsing data
rowOne = 11;
fileID = fopen('input.txt', 'r');
lines = strings(0, 1);
line = fgetl(fileID);
linecounter = 1;
while ischar(line)
    if linecounter >= rowOne
        lines(end+1) = line;
    end
    line = fgetl(fileID);
    linecounter = linecounter + 1;
end
fclose(fileID);
clear fileID linecounter line rowOne

% make arrays from data
movecount = length(lines);

fromArray = zeros(1,movecount);
toArray = zeros(1,movecount);
numMoves = zeros(1,movecount);

for i = 1:movecount
    splitarray = split(lines(i));
    numMoves(i) = str2num(splitarray(2));
    fromArray(i) = str2num(splitarray(4));
    toArray(i) = str2num(splitarray(6));
end
clear i ans lines splitarray

for i = 1:movecount
    for j = 1:numMoves(i)
        for k = 1:size(stacks,1)
            if ~(strcmp(stacks(k,fromArray(i)),' ') | strcmp(stacks(k,fromArray(i)),''))
                moveLetter = stacks(k,fromArray(i));
                break
            end
        end
        
        for l = 1:maxstackheight
            if (strcmp(stacks(l,toArray(i)),' ') | strcmp(stacks(l,toArray(i)),'')) ...
                    && ~(strcmp(stacks(l+1,toArray(i)),' ') | strcmp(stacks(l+1,toArray(i)),''))
                stacks(l,toArray(i)) = moveLetter;
                break
            end
        end

    end
end


