#include <string>
#include <fstream>
#include <iostream>
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
        cout << "Error: Cannot open file named '" << filename << ".'" << endl;
        return -1;
    }

    // Read input file
    string input;
    int sum;
    int max = -1;
    while (!fp.eof()) {
        getline(fp, input);
        if (input.length() != 0) {
            sum += stoi(input);
        }
        else {
            if (sum > max) {
                max = sum;
            }
            sum = 0;
        }
    }
    fp.close();

    // Print max
    cout << "The elf with the most calories holds " << max << " calories." << endl;

    return 0;
}