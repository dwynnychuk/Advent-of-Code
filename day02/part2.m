% Advent of Code 2022
% Day 2
% Part 2

% A Rock
% B Paper
% C Scissors

% X Rock
% Y Paper
% Z Scissors

% 0 Loss
% 3 Draw
% 6 Win
% % % % % % % %
clc
clear all
% % % % % % % %

pairs = fscanf(fopen('input.txt','r'),'%s',[2 Inf]);
numPairs = size(pairs,2);
scoreOutcome = zeros(1,numPairs);
scorePlay = zeros(1,numPairs);

for i = 1:numPairs
    pair = pairs(:,i);
    opponent = pair(1);
    personal = pair(2);
    outcome = '';

    switch opponent
        case 'A'
            if strcmp(personal,'X')
                outcome = 'DRAW';
                scorePlay(i) = 1;
            elseif strcmp(personal,'Y')
                outcome = 'WIN';
                scorePlay(i) = 2;
            else
                outcome = 'LOSS';
                scorePlay(i) = 3;
            end

        case 'B'
            if strcmp(personal,'X')
                outcome = 'LOSS';
                scorePlay(i) = 1;
            elseif strcmp(personal,'Y')
                outcome = 'DRAW';
                scorePlay(i) = 2;
            else
                outcome = 'WIN';
                scorePlay(i) = 3;
            end

        case 'C'
            if strcmp(personal,'X')
                outcome = 'WIN';
                scorePlay(i) = 1;
            elseif strcmp(personal,'Y')
                outcome = 'LOSS';
                scorePlay(i) = 2;
            else
                outcome = 'DRAW';
                scorePlay(i) = 3;
            end
    end

switch outcome
    case 'WIN'
        scoreOutcome(i) = 6;
    case 'DRAW'
        scoreOutcome(i) = 3;
    case 'LOSS'
        scoreOutcome(i) = 0;
end
end

totalScore = sum(scoreOutcome) + sum(scorePlay);
fprintf('The total score is %d!\n\n',totalScore)
