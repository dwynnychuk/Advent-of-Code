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

    int digits;
    int totalsum;
    int linenum;
    int linelength;

    while (std::getline(file,line)) {
        digits = 0;
        linelength = line.length();

        for (int i = 0; i < linelength; i++) {
            if (isdigit(line[i])) {
                digits += 1;
            }
        }
        std::cout << digits << "\n";
    }

    std::cout << "\nThe total sum is: " << totalsum << "\n\n";
}