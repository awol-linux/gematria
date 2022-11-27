class HebrewLetters:
    """All the letters in the hebrew alphabet using hebrew letters
    This isn't needed but would make the code much more readable"""

    _letters = {
        "א": "alef",
        "ב": "bet",
        "ג": "gimel",
        "ד": "dalet",
        "ה": "he",
        "ו": "vav",
        "ז": "zayin",
        "ח": "het",
        "ט": "tet",
        "י": "yod",
        "כ": "kaf",
        "ך": "kaf-final",
        "ל": "lamed",
        "מ": "mem",
        "ם": "mem-final",
        "נ": "nun",
        "ן": "nun-final",
        "ס": "samekh",
        "ע": "ayin",
        "פ": "pe",
        "ף": "pe-final",
        "צ": "tsadi",
        "ץ": "tsadi-final",
        "ק": "qof",
        "ר": "resh",
        "ש": "shin",
        "ת": "tav",
    }

    @classmethod
    @property
    def letters_by_english(cls):
        return {v: k for k, v in cls._letters.items()}

    @classmethod
    @property
    def letters_by_hebrew(cls):
        return cls._letters

    @classmethod
    def get_hebrew_letter(cls, english_letter):
        return cls.letters_by_english[english_letter]

    @classmethod
    def get_english_letter(cls, hebrew_letter):
        return cls.letters_by_hebrew[hebrew_letter]

    @classmethod
    def get_english_index(cls, english_letter):
        return list(cls.letters_by_english.keys()).index(english_letter)

    @classmethod
    def get_english_letter_by_index(cls, index, final=False):
        letters = {
            k: v
            for k, v in cls.letters_by_english.items()
            if (not k.endswith("final") and not final)
        }
        return list(letters)[index - 1]

    @classmethod
    def get_hebrew_index(cls, hebrew_letter):
        return list(cls.letters_by_hebrew.keys()).index(hebrew_letter)

    @classmethod
    def get_hebrew_letter_by_index(cls, index, final=False):
        letters = {
            k: v
            for k, v in cls.letters_by_hebrew.items()
            if (not k.endswith("final") and not final)
        }
        return list(letters)[index - 1]
