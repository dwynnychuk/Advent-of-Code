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
int total = 0;
vector<int> totals;
while (std::getline(file,line)) {
    if (line.size() == 0) {
        totals.push_back(total);
        total = 0;
    } else {
        total += std::stoi(line);
    }
}
std::sort(totals.begin(),totals.end(), greater<int>());
int topThree[3] = {totals[0], totals[1], totals[2]};
int topSum = std::accumulate(topThree, topThree + 3, topSum);
printf("The Top Three Sums to %i\n\n", topSum);
}