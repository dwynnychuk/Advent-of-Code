% Advent of Code 2022
% Day 5
% Part 1

clear all
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
clear i

stacknum = 9;
maxstackheight = 8;

% Determine length of array
maxl = 0;
for i = 1:maxstackheight
    maxl = length(lines{1,i});
    if length(lines{1,i}) > maxl
        maxl = length(lines{1,i});
    end
end
clear i
idxchar = 2:4:34;
stacks = strings(maxstackheight,stacknum);

% Make Crate Stacks
for i = 1:maxstackheight
    for j = 1:stacknum
        stacks(i,j) = lines{1,i}(idxchar(j));
    end
end

% Begin parsing data
rowOne = 11;

