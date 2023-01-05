#include <string.h>
#include <iostream>
using namespace std;

int main (int argc, char *argv[]) {
    // Checking for correct command line usage
    if (argc != 2) {
        cout << "Error: Correct command line usage is './a.out [input.txt]'" << endl;
        return -1;
    }
    string filename = argv[2];

    // Open input file
    istream *fp;
    if (!fp.open(filename)) {
        cout << "Error: Cannot open file named '" << filename << ".'" << endl;
        return -1;
    }

    // Read input file
    string input;
    int sum;
    int max = -1;
    while (!fp.eof()) {
        if (getline(fp, input)) != "") {
            sum += stoi(line);
        }
        else {
            if (sum > max) {
                max = sum;
            }
            sum = 0;
        }
    }

    // Print max
    cout << "The elf with the most calories holds " << max << " calories." << endl;

    return 0;
}