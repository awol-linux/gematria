import pytest

from gematria import get_num
from hebrew_letters import HebrewLetters

list_of_numbers = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
]
list_of_output = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100,
    200,
    300,
    400,
]


@pytest.mark.parametrize(
    "x,result",
    zip(list_of_numbers, list_of_output),
    ids=[
        f"{HebrewLetters.get_english_letter_by_index(x)}={y}"
        for x, y in zip(list_of_numbers, list_of_output)
    ],
)
def test_get_num(x, result):
    assert get_num(x) == result
