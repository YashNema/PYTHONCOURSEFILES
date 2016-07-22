def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    sup = 0

    handCopy = hand.copy ()

    for char in word:

        if char in handCopy:

            if handCopy [char] != 0:

                handCopy [char] -= 1

                sup += 1

    if sup == len(word) and (word in wordList):
        return True

    else:
        return False
