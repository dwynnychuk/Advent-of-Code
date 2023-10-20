% Advent of Code 2022
% Day 4
% Part 1

clear all
clc

fileID = fopen('input.txt', 'r');
lines = strings(0, 1);
line = fgetl(fileID);
while ischar(line)
    lines(end+1) = line;
    line = fgetl(fileID);
end
fclose(fileID);


numPairs = length(lines);

for i = 1:numPairs
    pair = split(lines(i),',');
    elf1 = pair(1,1);
    elf2 = pair(2,1);
end