import sys

val = sys.argv[1]

try:
    assert len(sys.argv) <= 2, "more than one argument is provided"
    if len(sys.argv) == 2:
        assert val.lstrip("+-").isdigit(), "argument is not an integer"
        if int(val) % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
except AssertionError as e:
    print(f"AssertionError: {e}")
