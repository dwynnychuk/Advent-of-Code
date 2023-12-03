#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
std::string line;
std::fstream file("input.txt");
int max = 0;
int total = 0;
while (std::getline(file,line)) {
    if (line.size() == 0) {
        max = std::max(max, total);
        total = 0;
    } else {
        total += std::stoi(line);
    }
}
printf("Max is equal to: %i\n",max);
}