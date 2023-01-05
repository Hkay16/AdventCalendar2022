def checkValue(opponent, me):
    # Check value
    
    return value

def main():
    import sys

    # Check for correct command line usage
    if len(sys.argv) != 2:
        print("Error: Correct command line usage is 'python Day2.py [input.txt]'")
        quit()

    # Open input file
    filename = sys.argv[1]
    with open(filename, "r") as input:
        if input.closed:
            print("Error: Cannot open file with name '" + filename + "'")
            exit()

        # Read through input, adding values to compute final score.
        while True:
            opponent = input.read(1)
            buffer = input.read(1)
            me = input.read(1)
            eof = input.readline()

            print(opponent, buffer, me)

            sum += checkValue(opponent, me)

            if eof == '': 
                break

        input.close()

if __name__ == "__main__":
    main()