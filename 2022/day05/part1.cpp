#include <iostream>
#include <string>
#include <fstream>
#include <stack>
#include <vector>
#include <regex>
using namespace std;

int main() {
    std::fstream file("input.txt");
    std::string line;

    // read initial input
    std::vector<std::string> initial_condition;

    while(std::getline(file, line) && (line[1] != '1')) {
        initial_condition.push_back(line);
    }
    const int input_width = initial_condition[0].size();
    const int input_height = initial_condition.size();
    const int stack_num = round(input_width / 4);

    // make initial stacks
    std::vector<std::stack<char> > stacks(stack_num);
    for (int i = input_height-1; i >= 0; i--) {
        for (int j = 0; j < stack_num; j++){
            const int k = (j+1)*4 - 3;
            if (initial_condition[i][k] == ' ') {
                continue;
            } else {
                stacks[j].push(initial_condition[i][k]);
            }
        }
    }

std::getline(file,line);
const std::regex pattern("move ([0-9]+) from ([0-9]) to ([0-9])");
    while (std::getline(file,line)) {
        // Turn line into 3 columns using regex
        std::smatch match;
        std::regex_match(line, match, pattern);

        const int quantity = std::stoi(match[1]);
        const int from = std::stoi(match[2]);
        const int to = std::stoi(match[3]);

    }

    // print result

}