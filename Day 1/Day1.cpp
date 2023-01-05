#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

int main (int argc, char *argv[]) {
    // Checking for correct command line usage
    if (argc != 2) {
        cout << "Error: Correct command line usage is './a.out [input.txt]'" << endl;
        return -1;
    }
    string filename = argv[1];

    // Open input file
    ifstream fp;
    fp.open(filename);
    if (!fp.is_open()) {
        cout << "Error: Cannot open file named '" << filename << "'" << endl;
        return -1;
    }

    // Read input file
    string input;
    int sum;
    int max = -1;
    int maxThree;
    vector<int> totals;
    while (!fp.eof()) {
        getline(fp, input);
        if (input.length() != 0) {
            sum += stoi(input);
        }
        else {
            totals.push_back(sum);
            sum = 0;
        }
    }
    fp.close();

    sort(totals.begin(), totals.end());
    max = totals.at(totals.size()-1);
    maxThree = max + totals.at(totals.size()-2) + totals.at(totals.size()-3);

    // Print max(s)
    cout << "Part 1: The elf with the most calories holds " << max << " calories." << endl;
    cout << "Part 2: The top three elves with the most calories hold " << maxThree << " calories." << endl;

    return 0;
}