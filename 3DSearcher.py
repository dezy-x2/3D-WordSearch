from english_words import english_words_lower_alpha_set as english


# this function sorts through all of the words and eliminates ones that couldn't work
def getEligibleWords(corpus):
    letters = ["p", "n", "l", "r", "k", "a", "m",
               "s", "t", "e", "u", "c", "h", "o", "v", "i"]
    actualList = []
    for word in corpus:
        # `everyLetter()` is a helper function that checks if the word contains a letter that is not in the set
        if len(word) == 5 and everyLetter(word, letters):
            actualList.append(word)
    return actualList

# `everyLetter()` is a helper function that checks if the word contains a letter that is not in the set


def everyLetter(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True
