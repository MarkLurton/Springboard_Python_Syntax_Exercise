# pylint: disable-all

def print_upper_words(words, must_start_with = ["h", "y"]):
    for word in words:
        if word[0].lower() in must_start_with or word[0].upper() in must_start_with:
            print(word.upper())
