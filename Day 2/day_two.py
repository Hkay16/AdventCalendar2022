"""
Computes total score for a game of Rock, Paper, Scissors.
"""
import sys

def check_win_p1(col_1, col_2):
    """Compare hands to confirm if win, loss, or draw."""
    if col_1 == 'A':
        if col_2 == 'X':
            value = 3
        elif col_2 == 'Y':
            value = 6
        else:
            value = 0
    elif col_1 == 'B':
        if col_2 == 'X':
            value = 0
        elif col_2 == 'Y':
            value = 3
        else:
            value = 6
    else:
        if col_2 == 'X':
            value = 6
        elif col_2 == 'Y':
            value = 0
        else:
            value = 3

    return value

def check_myself_p1(col_2):
    """Check player's hand to determine value."""
    switcher = {
		'X': 1,
		'Y': 2,
		'Z': 3,
	}

    return switcher.get(col_2, 0)

def check_win_p2(col_2):
    """Check column 2 to determine if win, loss, or draw."""
    switcher = {
		'X': 0,
		'Y': 3,
		'Z': 6,
	}

    return switcher.get(col_2, 0)

def check_myself_p2(col_1, col_2):
    """Compare hands to determine what player's hand value should be."""
    if col_2 == 'X':
        if col_1 == 'A':
            value = 3
        elif col_1 == 'B':
            value = 1
        else:
            value = 2
    elif col_2 == 'Y':
        if col_1 == 'A':
            value = 1
        elif col_1 == 'B':
            value = 2
        else:
            value = 3
    else:
        if col_1 == 'A':
            value = 2
        elif col_1 == 'B':
            value = 3
        else:
            value = 1

    return value

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
        part1_score = 0
        part2_score = 0
        while True:
            col_1 = input_file.read(1)
            col_2 = input_file.read(1)
            col_2 = input_file.read(1)
            eof = input_file.readline()

            # Part 1:
            part1_score += check_myself_p1(col_2) + check_win_p1(col_1, col_2)

            # Part 2:
            part2_score += check_myself_p2(col_1, col_2) + check_win_p2(col_2)

            if eof == '':
                break

        input_file.close()

        print("Part 1: Total score is ", part1_score)
        print("Part 2: Total score is ", part2_score)


if __name__ == "__main__":
    main()
