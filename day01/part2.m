% Advent of Code 2022
% Day 1
% Part 2
clc
clear all
data = dlmread("input.txt",'\n');

numValues = max(size(data));
maxElves = 3;

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

maximumCalories = maxk(calorieArray,maxElves);
maximumCaloriesSum = sum(maximumCalories);

fprintf('The three elves with the most calories had %d Calories in total!\n',maximumCaloriesSum)