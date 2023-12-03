#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

int main() {
    std::string line;
    std::fstream file("input.txt");

    char tempPlay;
    char tempOpp;

    int roundScore = 0;
    int idxOpp = 0;
    int idxMe = 2;
    int tempScore = 0;

    vector<char> opponent;
    vector<char> myPlay;
    vector<int> scores;

    while (std::getline(file,line)) {
        tempOpp = line[idxOpp];
        tempPlay = line[idxMe];
        opponent.push_back (tempOpp);
        myPlay.push_back(tempPlay);

        if (tempOpp == 'A' && tempPlay == 'X') {
            // rock x scissors
            tempScore = 3 + 0;
            scores.push_back(tempScore);
        } else if (tempOpp == 'A' && tempPlay == 'Y') {
            // rock x rock
            tempScore = 1 + 3;
            scores.push_back(tempScore);
        } else if (tempOpp == 'A' && tempPlay == 'Z') {
            // rock x paper
            tempScore = 2 + 6;
            scores.push_back(tempScore);
        } else if (tempOpp == 'B' && tempPlay == 'X') {
            // paper x rock
            tempScore = 1 + 0;
            scores.push_back(tempScore);
        } else if (tempOpp == 'B' && tempPlay == 'Y') {
            // paper x paper
            tempScore = 2 + 3;
            scores.push_back(tempScore);
        } else if (tempOpp == 'B' && tempPlay == 'Z') {
            // paper x scissors
            tempScore = 3 + 6;
            scores.push_back(tempScore);
        } else if (tempOpp == 'C' && tempPlay == 'X') {
            // scissors x paper
            tempScore = 2 + 0;
            scores.push_back(tempScore);
        } else if (tempOpp == 'C' && tempPlay == 'Y') {
            // scissors x scissors
            tempScore = 3 + 3;
            scores.push_back(tempScore);
        } else if (tempOpp == 'C' && tempPlay == 'Z') {
            // scissors x rock
            tempScore = 1 + 6;
            scores.push_back(tempScore);
        }

    }

    int totalScore = std::accumulate(scores.begin(), scores.end(), 0);

    printf("The Total Score is: %i\n\n", totalScore);
}