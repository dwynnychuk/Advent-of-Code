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
    std::string c2;
    std::string color;

    int totalsum;
    int oversum;
    int gamesum;
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
    int die_red = 0;
    int die_green = 0;
    int die_blue = 0;
    int hands_left;
    int last_hand;
    int die_left;

    while (std::getline(file,line)) {
        count += 1;
        gamesum += count;
        col_pos = line.find(':');
        allDice = line.substr(col_pos+2);
        hands_left = 1;
        last_hand = 0;

        while (hands_left){ 
            die_left = 1;
            if (allDice.find(';') == string::npos) {
                last_hand = 1;
                hands_left = 0;
                h1 = allDice;
            } else {
                scol_pos = allDice.find(';');
                h1 = allDice.substr(0,scol_pos);
                allDice = allDice.substr(scol_pos+2);
                hands_left = 1;
                last_hand = 0;
            }
            //cout << count << ' ' << h1 << endl;
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
                } else if (color.compare("green") == 0)
                {
                    die_green = stoi(c1.substr(0, sp_pos));
                } else if (color.compare("red") == 0)
                {
                    die_red = stoi(c1.substr(0, sp_pos));
                }
            }
            //cout << "red " << die_red << " green " << die_green << " blue " << die_blue << endl;

            if (die_red > max_red || die_green > max_green || die_blue > max_blue)
            {
                //cout << "MAX " << count << endl;
                oversum += count;
                break;
            }
        }

        /*
             if (total_red <= max_red && total_green <= max_green && total_blue <= max_blue){
            totalsum += count;
        }
        */
    }
    totalsum = gamesum - oversum;
    std::cout << "\nThe total sum is: " << totalsum << "\n\n";
}