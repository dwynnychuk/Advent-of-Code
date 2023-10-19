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

priority = ['a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p'...
    'q' 'r' 's' 't' 'u' 'v' 'w' 'x' 'y' 'z' 'A' 'B' 'C' 'D' 'E' 'F' 'G'...
    'H' 'I' 'J' 'K' 'L' 'M' 'N' 'O' 'P' 'Q' 'R' 'S' 'T' 'U' 'V' 'W' 'X' 'Y' 'Z'];

repeats = strings(size(lines));
values = zeros(size(lines));

for i = 1:size(lines,2)
    rucksack = strsplit(lines(1,i),'');
    rucksack = rucksack{1};

    totalItems = length(rucksack);
    leftHalf = rucksack(1:totalItems/2);
    rightHalf = rucksack(((totalItems/2)+1):totalItems);

    for j = 1:(totalItems/2)
        comLR = contains(rightHalf,leftHalf(j));
        if comLR > 0
            repeats(i) = leftHalf(j);
        end
    end
end

for k = 1:length(lines)
    current = repeats(k);
    current = current{1};
    values(k) = strfind(priority,current);
end

fprintf('The total rucksack sum is %d !\n\n',sum(values))