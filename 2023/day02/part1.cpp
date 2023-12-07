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
    std::string allDice;
    std::string h1;
    std::string h2;

    int totalsum;
    int hands;
    int count;
    int col_pos;
    int scol_pos;
    int total_red;
    int total_green;
    int total_blue;
    int max_red = 12;
    int max_green = 13;
    int max_blue = 14;

    while (std::getline(file,line)) {
        count += 1;
        col_pos = line.find(':');
        allDice = line.substr(col_pos+1);
        cout << allDice << endl;

        if (allDice.find(';') != string::npos){ 
            scol_pos = allDice.find(';');
            h1 = allDice.substr(0, scol_pos);
            h2 = allDice.substr(scol_pos+1);
            //allDice.erase(0,scol_pos);
            cout << count << ' '<< h1 << '\n' << h2 << '\n' << '\n' << endl;
        }
/*         if (total_red <= max_red && total_green <= max_green && total_blue <= max_blue){
            totalsum += count;
        } */
    }

    std::cout << "\nThe total sum is: " << totalsum << "\n\n";
}