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

# Now we need to traverse through the puzzle and find words that match the letters in the puzzle
# This will probably best be executed via BFS checking all of the letters around the current letter
# From there we will just check until we find all of the words
# gonna be tricky


def indexesToCheck(x, y, z):
    indexes = [[x, y, z-1]]
    if x > 0:
        indexes.append([x-1, y, z])
    if x < 2:
        indexes.append([x+1, y, z])
    if y > 0:
        indexes.append([x, y-1, z])
    if y < 2:
        indexes.append([x, y+1, z])
    return indexes


possibleWords = getEligibleWords(english)


def findWords(puzzle, wordList):
    foundWords = []
    for x in range(3):
        for y in range(3):
            for z in range(2):
                results = None
                words = wordList[binarySearch(wordList, puzzle[x][y][z])]
                idxToCheck = indexesToCheck(x, y, z)
                for word in words:
                    for _x, _y, _z in idxToCheck:
                        # TODO: need to figure out a solution for moving to the next letter and
                        for i in range(len(word)):
                            # TODO: if it does we have to generate the new indexes to check and repeat
                            # this kinda sucks
                            results = pokeAround(
                                [_x, _y, _z], word[i:], puzzle)
                            if not results:
                                break
                        if not results:
                            break
                        foundWords.append(word)


def pokeAround(coords, word, puzzle):
    x, y, z = coords
    if puzzle[x][y][z] == word[0]:
        return True
    return False
