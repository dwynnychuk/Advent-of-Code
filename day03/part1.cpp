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
    char pointReference[52][1] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 
                                'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
                                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

    char tempChar;

    int lineLength;
    int rucksackQuantity;

    vector<char> commons;

    while (std::getline(file,line)) {
        lineLength = line.length();
        rucksackQuantity = lineLength / 2;

        for () {
            
        }
    }

    //int totalScore = std::accumulate(scores.begin(), scores.end(), 0);

    //printf("The Total Score is: %i\n\n", totalScore);
}