% Advent of Code 2022
% Day 3
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

priority = ['a' 'b' 'c' 'd' 'e' 'f' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p'...
    'q' 'r' 's' 't' 'u' 'v' 'w' 'x' 'y' 'z' 'A' 'B' 'C' 'D' 'E' 'F' 'G'...
    'H' 'I' 'J' 'K' 'L' 'M' 'N' 'O' 'P' 'Q' 'R' 'S' 'T' 'U' 'V' 'W' 'X' 'Y' 'Z'];

repeats = strings(size(lines));
values = zeros(size(lines));

for i = 1:size(lines,2)
    rucksacks = strsplit(lines(1,i),'');
    rucksacks(2)
end
