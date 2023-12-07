#include <iostream>
#include <fstream>
#include <string>
#include <numeric>
using namespace std;

int main() {
    std::fstream file("input.txt");
    std::string line;
    std::string linenum;
    std::string digits;

    int totalsum;
    int linelength;
    int count;
    int numdigits = 9;

    std::string WrittenNumbers[9] = 
        {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    
    std::string ReplaceNumbers[9] = 
        {"o1e", "t2o", "t3e", "f4r", "f5e", "s6x", "s7n", "e8t", "n9e"};

    while (std::getline(file,line)) {
        count += 1;

        for (int i = 0; i < numdigits; i++) {
            while (line.find(WrittenNumbers[i]) != string::npos){
                line.replace(line.find(WrittenNumbers[i]),WrittenNumbers[i].length(), ReplaceNumbers[i]);
            }
        }
        
        linelength = line.length();
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