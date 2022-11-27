import pytest
from hebrew_letters import HebrewLetters


def test_letters_by_english():
    assert HebrewLetters.letters_by_english == {
        v: k for k, v in HebrewLetters._letters.items()
    }

def test_letters_by_hebrew():
    assert HebrewLetters.letters_by_hebrew == HebrewLetters._letters


@pytest.mark.parametrize(
    "english_letter,hebrew_letter",
    [(v, k) for k, v in HebrewLetters._letters.items()],
)
def test_get_hebrew_letter(english_letter, hebrew_letter):
    assert HebrewLetters.get_hebrew_letter(english_letter) == hebrew_letter

@pytest.mark.parametrize(
    "hebrew_letter,english_letter",
    HebrewLetters._letters.items(),
)
def test_get_english_letter(hebrew_letter, english_letter):
    assert HebrewLetters.get_english_letter(hebrew_letter) == english_letter

@pytest.mark.parametrize(
    "letter,index",
    [(v, k) for k, v in enumerate(HebrewLetters.letters_by_english)],
)
def test_get_english_index(letter,index):
    assert HebrewLetters.get_english_index(letter) == index

@pytest.mark.parametrize(
    "index,letter",
    enumerate(HebrewLetters.letters_by_english),
)
def test_get_english_letter_by_index(index,letter):
    assert HebrewLetters.get_english_letter_by_index(index) == letter

