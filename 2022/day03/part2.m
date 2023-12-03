% Advent of Code 2022
% Day 3
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

priority = ['a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p'...
    'q' 'r' 's' 't' 'u' 'v' 'w' 'x' 'y' 'z' 'A' 'B' 'C' 'D' 'E' 'F' 'G'...
    'H' 'I' 'J' 'K' 'L' 'M' 'N' 'O' 'P' 'Q' 'R' 'S' 'T' 'U' 'V' 'W' 'X' 'Y' 'Z'];

numberGroups = size(lines,2)/3;

repeats = strings(1,numberGroups);
values = zeros(1,numberGroups);

for i = 1:numberGroups
    rucksack1 = strsplit(lines(1,(3*(i-1)+1)),'');
    rucksack2 = strsplit(lines(1,(3*(i-1)+2)),'');
    rucksack3 = strsplit(lines(1,(3*(i-1)+3)),'');

    rucksack1 = rucksack1{1};
    rucksack2 = rucksack2{1};
    rucksack3 = rucksack3{1};

    totalItems = length(rucksack1);

    for j = 1:totalItems
        com12 = contains(rucksack2,rucksack1(j));
        com13 = contains(rucksack3,rucksack1(j));
        if com12 > 0 && com13 > 0
            repeats(i) = rucksack1(j);
        end
    end
end

for k = 1:numberGroups
    current = repeats(k);
    current = current{1};
    values(k) = strfind(priority,current);
end

fprintf('The total rucksack sum is %d !\n\n',sum(values))