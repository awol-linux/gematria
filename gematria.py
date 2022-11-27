import sys
from hebrew_letters import HebrewLetters

"""
this is the part of the code that actually does the conversion
I know this is the hard way since these numbers will NEVER change
but it was still fun to write it in this way
"""


def get_num(x):
    num = str(x)
    if len(num) == 1:
        return x
    else:
        last_digit = int(num[-1])
        up_until_last_digit = int(num[:-1])
        amount_of_zeros = up_until_last_digit
        return int(str(last_digit + up_until_last_digit) + str("0" * amount_of_zeros))


if __name__ == "__main__":
    num = int(sys.argv[1])
    letter = HebrewLetters.get_english_letter_by_index(num)
    number = get_num(num)
    print(f"{number=},{letter=}")
