import sys
import string

def str_len(str):
    print(f"The text contains {len(str)} characters:")
def n_upper_letters(str):
    print(sum(1 for c in str if c.isupper()), "upper letters")
def n_lower_letters(str):
    print(sum(1 for c in str if c.islower()), "lower letters")
def n_punct_marks(str):
    print(sum(1 for p in str if p in string.punctuation), "punctuation marks")
def n_spaces(str):
    print(f"{str.count(" ")} spaces")
def n_digits(str):
    print(sum(1 for d in str if d.isdigit()), "digits")

def main():

    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 2:
            str = sys.argv[1]
            str_len(str)
            n_upper_letters(str)
            n_lower_letters(str)
            n_punct_marks(str)
            n_spaces(str)
            n_digits(str)
        else:
            string = input("What is the text to count?\n")
            str_len(string)
            n_upper_letters(string)
            n_lower_letters(string)
            n_punct_marks(string)
            n_spaces(string)
            n_digits(string)
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()
