from english_words import english_words_lower_alpha_set as english


# this function sorts through all of the words and eliminates ones that couldn't work
def getEligibleWords(corpus):
    letters = ["p", "n", "l", "r", "k", "a", "m", "s", "t", "e", "u", "c", "h", "o", "v", "i"]
    actualList = []
    for word in corpus:
        #`everyLetter()` is a helper function that checks if the word contains a letter that is not in the set
        if len(word) == 5 and everyLetter(word, letters):
            actualList.append(word)
    return actualList

#`everyLetter()` is a helper function that checks if the word contains a letter that is not in the set
def everyLetter(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True

#python doesn't actually allow you to change a char by indexing (ex: word[0] = "h")
#so we have to do it by spliting up the string and inserting the char
def replaceInString(string, index, char):
    return string[:index] + char + string[index+1:]

#this takes a list of mixed strings and turns it back into something readable
def translator(startArr):
    #this makes a copy of the list so that we don't edit the original
    arr = startArr.copy()
    for i in range(len(arr)):
        if "#" in arr[i] or "@" in arr[i]:
            if "#" in arr[i]:
                for j in range(len(arr[i])):
                    if arr[i][j] == "#":
                        arr[i] = replaceInString(arr[i], j, "h")
            if "@" in arr[i]:
                for j in range(len(arr[i])):
                    if arr[i][j] == "@":
                        arr[i] = replaceInString(arr[i], j, "c")
        
    return list(set(arr))

p = "p"
n = "n"
l = "l"
r = "r"
k = "k"
a = "a"
s = "s"
m = "m"
t = "t"
e = "e"
u = "u"
c1 = "c"
h1 = "h"
o = "o"
#these extra chars are because we need a way for the computer to tell the diference between
#letters that are in the puzzle twice
c2 = "@"
v = "v"
i = "i"
h2 = "#"

puzzleDict = {p: [k, a, u], n: [l, r, m], l: [n, a, s], r: [n, a, k, e], k: [r, p, c1], a: [t, l, r, p],
          s: [l, m, t, h1], m: [n, s, e, o], t: [s, e, u, a, c2], e: [m, o, t, r, v], u: [c1, t, p, h2],
          c1: [u, e, k, i], h1: [s, o, c2], o: [m, h1, v], c2: [h1, v, t, h2], v: [o, i, c2, e], i: [h2, v, c1],
          h2: [c2, u, i]}


#this function takes normal words and inserts chars to be able to distinguish from repeat chars
#! this function scrambles the word fully we need it to scramble it in every way possible
def mixer(startArr):
    #this makes a copy of the list so that we don't edit the original
    arr = startArr.copy()
    for i in range(len(arr)):
        if "h" in arr[i] or "c" in arr[i]:
            if "h" in arr[i]:
                for j in range(len(arr[i])):
                    if arr[i][j] == "h":
                        arr[i] = replaceInString(arr[i], j, "#")
            if "c" in arr[i]:
                for j in range(len(arr[i])):
                    if arr[i][j] == "c":
                        arr[i] = replaceInString(arr[i], j, "@")
        
    return list(set(arr))

#this function compares two lists together just a helper for debuging will probably be deleted soon
def compareLists(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True


#this function is just to do some of the work that `solve()` would do but this keeps things looking cleaner
def solveWord(word, puzzle):
    #the first letter of the word is the key of the options that that letter leads to
    key = word[0]
    #we don't need to look at the first letter bc `solve` already did that
    word = word[1:]
    letter = key
    #we use this to keep track of the previous letter so we know if anything changed
    prevLetter = key
    for i in range(len(word)):
        for value in puzzle[key]:
            if word[i] == value:
                letter = value
                #break out of the loop cause theres no point in going further
                break 
        if letter == prevLetter:
            #if we never changed the letter then the word is not possible
            return False
    return True


#this is where the magic happens
def solve(corpus, puzzle):
    foundWords = []
    for i in range(len(corpus)):
        for key in puzzle.keys():
            #just checking if the first letter matches cause that should speed things along
            if corpus[i][0] == key:
                #expidites the hard work to `solveWord()`
                if(solveWord(corpus[i], puzzle)):
                    foundWords.append(corpus[i])
    return foundWords

#! catching words that shouldn't be possible here!! need to check this out
possibleWords = getEligibleWords(english)
possibleWordsMixed = mixer(possibleWords)


print(translator(solve(possibleWordsMixed, puzzleDict)))