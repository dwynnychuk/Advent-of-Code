#include <iostream>
#include <string>
#include <fstream>
#include <tuple>
using namespace std;

struct StringPair {
    std::string first;
    std::string second;
};

struct IntPair {
    int first;
    int second;
};

StringPair split_primary(const std::string str, const char delim) {
    StringPair ranges;
    const int delim_idx = str.find(delim);
    ranges.first = str.substr(0, delim_idx);
    ranges.second = str.substr(delim_idx+1, str.size() - delim_idx);
    return ranges;
}

IntPair split_secondary(const std::string str, const char delim) {
    IntPair extrema;
    const StringPair ranges = split_primary(str, delim);
    extrema.first = stoi(ranges.first);
    extrema.second = stoi(ranges.second);
    return extrema;
}

int main() {
    std::fstream file("input.txt");
    std::string line;
    char delimiter_primary = ',';
    char delimiter_secondary = '-';
    int counter = 0;

    while (std::getline(file,line)) {
        const StringPair rg = split_primary(line, delimiter_primary);
        const IntPair vals1 = split_secondary(rg.first, delimiter_secondary);
        const IntPair vals2 = split_secondary(rg.second, delimiter_secondary);
        const int min1 = vals1.first;
        const int max1 = vals1.second;
        const int min2 = vals2.first;
        const int max2 = vals2.second;

        // Check for overlapping at all
        if (((min1 <= min2) && (max1 >= min2)) || ((max1 >= min2) && (min1 <= max2))) {
            counter += 1;
        }
    }
    std::cout << "Total number of fully overlapping is: " << counter << endl;
}