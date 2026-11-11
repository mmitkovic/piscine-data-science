import sys

NESTED_MORSE = {" ": "/ ",
                "A": ".- ",
                "B": "-... ",
                "C": "-.-. ",
                "D": "-.. ",
                "E": ". ",
                "F": "..-. ",
                "G": "--. ",
                "H": ".... ",
                "I": ".. ",
                "J": ".--- ",
                "K": "-.- ",
                "L": ".-.. ",
                "M": "-- ",
                "N": "-. ",
                "O": "--- ",
                "P": ".--. ",
                "Q": "--.- ",
                "R": ".-. ",
                "S": "... ",
                "T": "- ",
                "U": "..- ",
                "V": "...- ",
                "W": ".-- ",
                "X": "-..- ",
                "Y": "-.-- ",
                "Z": "--.. ",
                "0": "----- ",
                "1": ".---- ",
                "2": "..--- ",
                "3": "...-- ",
                "4": "....- ",
                "5": "..... ",
                "6": "-.... ",
                "7": "--... ",
                "8": "---.. ",
                "9": "----. ", }


def main():
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 2:
            text = sys.argv[1]
            assert all(
                c.upper() in NESTED_MORSE for c in text), "the arguments are bad"
            for c in text:
                print(NESTED_MORSE[c.upper()], end="")
            print()
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
