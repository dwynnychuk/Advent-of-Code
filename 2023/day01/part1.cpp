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
    std::string digits;

    int totalsum;
    int linelength;
    int count;

    while (std::getline(file,line)) {
        linelength = line.length();
        count += 1;
        digits = "";

        for (int i = 0; i < linelength; i++) {
            if (isdigit(line[i])) {
                digits += line[i];
            }
        }

        linenum = digits.substr(0,1) + digits.substr(digits.length()-1, digits.length());
        totalsum += std::stoi(linenum);
    }

    std::cout << "\nThe total sum is: " << totalsum << "\n\n";
}