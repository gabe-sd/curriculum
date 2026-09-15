"""
10 level 1 Python practice problems.
Fill in each function, then run this file to check your answers.
"""


def square_num(n):
    # return the number squared
    pass


def add_five(n):
    # return the number plus 5
    pass


def is_even(n):
    # return True if the number is even
    pass


def first_char(s):
    # return the first character of a string
    pass


def last_char(s):
    # return the last character of a string
    pass


def string_len(s):
    # return the length of a string
    pass


def max_of_two(a, b):
    # return the larger of two numbers
    pass


def is_positive(n):
    # return True if the number is greater than 0
    pass


def combine_strings(a, b):
    # return the two strings joined together
    pass


def half_num(n):
    # return half the number (as a float)
    pass


# ---- Tests ----
if __name__ == "__main__":
    tests = [
        (square_num, (4,), 16),
        (add_five, (10,), 15),
        (is_even, (6,), True),
        (first_char, ("hello",), "h"),
        (last_char, ("hello",), "o"),
        (string_len, ("cat",), 3),
        (max_of_two, (3, 7), 7),
        (is_positive, (-2,), False),
        (combine_strings, ("cod", "ing"), "coding"),
        (half_num, (10,), 5.0),
    ]

    passed = 0
    for func, args, expected in tests:
        try:
            result = func(*args)
            ok = result == expected
        except Exception as e:
            result = "ERROR: " + str(e)
            ok = False
        if ok:
            status = "PASS"
            passed += 1
        else:
            status = "FAIL"
        print(status + "  " + func.__name__ + str(args) + " -> " + str(result) + " (expected " + str(expected) + ")")

    print("")
    print(str(passed) + "/" + str(len(tests)) + " passed")