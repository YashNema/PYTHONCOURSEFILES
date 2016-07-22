def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    maxValidWords = 0
    bestShift = 0
    for shift in range(26):
        newWord = applyShift(text, shift)
        newWord = newWord.split()
        count = 0
        for word in newWord:
            
            if isWord(wordList, word):
                count += 1
        if count > maxValidWords:
            maxValidWords = count
            bestShift = shift
    return bestShift 
def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    ### TODO
    shift=findBestShift(loadWords(),getStoryString())
    return applyShift(getStoryString(),shift)