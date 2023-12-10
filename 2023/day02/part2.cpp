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
    std::string c1;
    std::string color;

    int totalsum;
    int prod;
    int count;
    int col_pos;
    int scol_pos;
    int com_pos;
    int sp_pos;
    int max_red;
    int max_green;
    int max_blue;
    int die_red = 0;
    int die_green = 0;
    int die_blue = 0;
    int hands_left;
    int die_left;

    while (std::getline(file,line)) {
        count += 1;
        col_pos = line.find(':');
        allDice = line.substr(col_pos+2);
        hands_left = 1;

        max_red = 0;
        max_green = 0;
        max_blue = 0;

        while (hands_left){ 
            die_left = 1;
            if (allDice.find(';') == string::npos) {
                hands_left = 0;
                h1 = allDice;
            } else {
                scol_pos = allDice.find(';');
                h1 = allDice.substr(0,scol_pos);
                allDice = allDice.substr(scol_pos+2);
                hands_left = 1;
            }
            die_left = 1;
            die_red = 0;
            die_green = 0;
            die_blue = 0;

            while (die_left)
            {
                if (h1.find(',') == string::npos)
                {
                    die_left = 0;
                    c1 = h1;
                    h1 = "";
                } 
                else 
                {
                    com_pos = h1.find(',');
                    c1 = h1.substr(0, com_pos);
                    h1 = h1.substr(com_pos+2);
                    die_left = 1;
                }

                sp_pos = c1.find(' ');
                color = c1.substr(sp_pos+1);
                if (color.compare("blue") == 0)
                {
                    die_blue = stoi(c1.substr(0, sp_pos));
                    if (die_blue > max_blue)
                    {
                        max_blue = die_blue;
                    }
                } else if (color.compare("green") == 0)
                {
                    die_green = stoi(c1.substr(0, sp_pos));
                    if (die_green > max_green)
                    {
                        max_green = die_green;
                    }
                } else if (color.compare("red") == 0)
                {
                    die_red = stoi(c1.substr(0, sp_pos));
                    if (die_red > max_red)
                    {
                        max_red = die_red;
                    }
                }
            }
        }
           if (die_left == 0)
        {
            prod = max_red * max_green * max_blue;
        }
        totalsum += prod;
    }
    std::cout << "\nThe total sum is: " << totalsum << "\n\n";
}