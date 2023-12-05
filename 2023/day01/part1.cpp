#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <ctype.h>
using namespace std;

int main() {
    std::fstream file("input.txt");
    std::string line;
    std::string linenum;

    int totalsum;
    int linelength;
    int lnum;
    char d1;
    char d2;

    while (std::getline(file,line)) {
        linelength = line.length();
        linenum = "";
        lnum += 1;

        for (int i = 0; i < linelength; i++) {
            if (isdigit(line[i])) {
                d1 = line[i];
                break;
            }
        }
        linenum += d1;
        for (int i = linelength; i > 0; i--) {
            if (isdigit(line[i])) {
                d2 = line[i];
                break;
            }
        }  
        linenum += d2;
        totalsum += std::stoi(linenum);
        std::cout << lnum << " " << linenum << " " << totalsum << "\n";
    }

    std::cout << "\nThe total sum is: " << totalsum << "\n\n";
}