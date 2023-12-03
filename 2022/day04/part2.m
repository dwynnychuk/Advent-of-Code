% Advent of Code 2022
% Day 4
% Part 2

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
encapsulated = 0;

for i = 1:numPairs
    pair = split(lines(i),',');
    elf1 = pair(1,1);
    elf2 = pair(2,1);
    
    elf1Lims = split(elf1,'-');
    elf2Lims = split(elf2,'-');

    elf1Low = str2double(elf1Lims(1,1));
    elf1High = str2double(elf1Lims(2,1));

    elf2Low = str2double(elf2Lims(1,1));
    elf2High = str2double(elf2Lims(2,1));

    if ((elf1Low <= elf2High) && (elf1High >= elf2Low)) || ((elf2Low <= elf1High) && (elf2High >= elf1Low))
        encapsulated = encapsulated + 1;
    end
end