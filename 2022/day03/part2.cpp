#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    std::fstream file("input.txt");
    std::string line;
    std::string e1;
    std::string e2;
    std::string e3;
    std::string pointReference("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ");

    char tempChar;

    int lineLength;
    int counter = 0;
    int tempIdx;
    int totalScore = 0;
    int c2 = 0;

    while (std::getline(file,line)) {
        counter += 1;
        if (counter == 1) {
            lineLength = line.length();
            e1 = line;
        } else if (counter == 2) {
            e2 = line;
        } else if (counter == 3) {
            e3 = line;
            c2 += 1;
            for (int i = 0; i < lineLength; i++) {
                tempChar = e1[i];
                if (e2.find(tempChar) != std::string::npos && e3.find(tempChar) != std::string::npos) {
                    counter = 0;
                    tempIdx = pointReference.find(tempChar);
                    totalScore += (tempIdx + 1);
                    break;
                }
            }
        }
    }

    std::cout << "\nThe total score is: " << totalScore << "\n\n";
}