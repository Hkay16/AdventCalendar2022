"""
Computes total score for a game of Rock, Paper, Scissors.
"""
import sys

def check_win(opponent, myself):
    """Compare hands to confirm if win, loss, or draw"""
    if opponent == 'A':
        if myself == 'X':
            value = 3
        elif myself == 'Y':
            value = 6
        else:
            value = 0
    elif opponent == 'B':
        if myself == 'X':
            value = 0
        elif myself == 'Y':
            value = 3
        else:
            value = 6
    else:
        if myself == 'X':
            value = 6
        elif myself == 'Y':
            value = 0
        else:
            value = 3

    return value

def check_myself(myself):
    """Check player's hand to determine value."""
    switcher = {
		'X': 1,
		'Y': 2,
		'Z': 3,
	}

    return switcher.get(myself, 0)

def main():
    """Main Program"""

    # Check for correct command line usage
    if len(sys.argv) != 2:
        print("Error: Correct command line usage is 'python Day2.py [input.txt]'")
        sys.exit()

    # Open input file
    filename = sys.argv[1]
    with open(filename, "r", encoding="utf-8") as input_file:
        if input_file.closed:
            print("Error: Cannot open file with name '" + filename + "'")
            sys.exit()

        # Read through input, adding values to compute final score.
        score = 0
        while True:
            opponent = input_file.read(1)
            myself = input_file.read(1)
            myself = input_file.read(1)
            eof = input_file.readline()

            score += check_myself(myself) + check_win(opponent, myself)

            if eof == '':
                break

        input_file.close()

        print("Part 1: Total score is ", score)

if __name__ == "__main__":
    main()
