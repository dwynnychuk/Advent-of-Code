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
    std::string c1;
    std::string c2;
    std::string color;

    int totalsum;
    int hands;
    int count;
    int col_pos;
    int scol_pos;
    int com_pos;
    int sp_pos;
    int total_red;
    int total_green;
    int total_blue;
    int max_red = 12;
    int max_green = 13;
    int max_blue = 14;
    int die_red;
    int die_green;
    int die_blue;

    while (std::getline(file,line)) {
        count += 1;
        col_pos = line.find(':');
        allDice = line.substr(col_pos+1);

        while (allDice.find(';') != string::npos){ 
            scol_pos = allDice.find(';');
            h1 = allDice.substr(0, scol_pos);
            h2 = allDice.substr(scol_pos+1);

            if (h1.find(',') != string::npos) {
            while (h1.find(',') != string::npos){
                com_pos = h1.find(',');
                c1 = h1.substr(0, com_pos);
                c2 = h1.substr(col_pos+1);

                sp_pos = c1.find(' ');
                color = c1.substr(sp_pos+1);
                if (color == "blue") {
                    die_blue = stoi(c1.substr(0,sp_pos));
                } else if (color == "green") {
                    die_green = stoi(c1.substr(0,sp_pos));
                } else if (color == "red") {
                    die_red == stoi(c1.substr(0,sp_pos));
                }
            }
            } else {

            }

            if (h2.find(';') != string::npos){
                allDice = h2;
            } else {
                allDice = "";
            }
            cout << count << ' ' << h2 << '\n' << '\n' << endl;
        }

        /*
             if (total_red <= max_red && total_green <= max_green && total_blue <= max_blue){
            totalsum += count;
        }
        */
    }

    std::cout << "\nThe total sum is: " << totalsum << "\n\n";
}