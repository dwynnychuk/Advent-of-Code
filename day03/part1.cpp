#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

int main() {
    std::fstream file("input.txt");
    std::string line;
    std::string lhs;
    std::string rhs;
    std::string pointReference("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ");

    char tempChar;

    int lineLength;
    int rucksackQuantity;
    int tempIdx;
    int tempScore;
    int totalScore;

    vector<char> commons;
    vector<int> scores;

    while (std::getline(file,line)) {
        lineLength = line.length();
        rucksackQuantity = lineLength / 2;
        lhs = line.substr(0, rucksackQuantity);
        rhs = line.substr(rucksackQuantity, lineLength);

        for (int i = 0; i < rucksackQuantity; i++) {
            tempChar = lhs[i];
            if (rhs.find(tempChar) != string::npos) {
                commons.push_back(tempChar);
                break;
            }
        }
        tempIdx = pointReference.find(tempChar);
        totalScore += (tempIdx + 1);

    }

    std::cout << "\nThe total score is: " << totalScore << "\n\n";
}