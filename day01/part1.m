% Advent of Code 2022
% Day 1
% Part 1
clc
clear all
data = dlmread("input.txt",'\n');

numValues = max(size(data));

zeroArray = find(~data);
numElves = length(zeroArray);
calorieArray = zeros(size(zeroArray));

for i = 1:numElves
    if i == 1
        calorieArray(i) = sum(data(1,1:zeroArray(i)));
    else
        calorieArray(i) = sum(data(1,zeroArray(i-1):zeroArray(i)));
    end
end

maximumCalorie = max(calorieArray);
fprintf('The elf with the most calories had %d Calories\n',maximumCalorie)