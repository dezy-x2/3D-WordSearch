from english_words import english_words_lower_alpha_set as english


# this function sorts through all of the words and eliminates ones that couldn't work
def getEligibleWords(corpus):
    letters = ["p", "n", "l", "r", "k", "a", "m",
               "s", "t", "e", "u", "c", "h", "o", "v", "i"]
    actualList = [[] for _ in range(26)]
    for word in corpus:
        # `everyLetter()` is a helper function that checks if the word contains a letter that is not in the set
        if len(word) == 5 and everyLetter(word, letters):
            actualList[ord(word[0]) - 97].append(word)
    return actualList


# this is a helper function that checks if the word contains a letter that is not in the set
def everyLetter(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True


# 3D Array time!
puzzle = [[["l", "n"], ["a", "r"], ["p", "k"]], [["s", "m"], [
    "t", "e"], ["u", "c"]], [["h", "o"], ["c", "v"], ["h", "i"]]]


def binarySearch(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        midIdx = (left + right) // 2
        if midIdx + 97 == ord(target):
            return midIdx
        elif ord(target) < ord(arr[midIdx]):
            right = midIdx
        elif ord(target) > ord(arr[midIdx]):
            left = midIdx + 1
