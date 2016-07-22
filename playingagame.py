def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    count =False
    while True:
        gamestart = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if gamestart == 'n':
            newhand = dealHand(HAND_SIZE)
            prevhand = newhand.copy()
        
            playHand(newhand, wordList, HAND_SIZE)
            count=True
        elif gamestart == 'r':
            if count==False:
                print 'You have not played a hand yet. Please play a new hand first!'
                
            else :
                playHand(prevhand, wordList, HAND_SIZE)
        
        elif gamestart == 'e':
             
             break

        else:
             print 'Invalid command.'
             playGame(wordList)
             break
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    # BEGIN PSEUDOCODE (available within ps4b.py)
    maxScore = 0
    bestWord = None
    for word in wordList:
        if isValidWord(word, hand, word):
            wordScore = getWordScore(word, n)
            if wordScore > maxScore:
                maxScore = wordScore
                bestWord = word
    return bestWord
def compChooseWord(hand, wordList, n):    
    maxScore = 0
    bestWord = None
    for word in wordList:
        if isValidWord(word, hand, word):
            wordScore = getWordScore(word, n)
            if wordScore > maxScore:
                maxScore = wordScore
                bestWord = word
    return bestWord


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    
    tot_score = 0

    # As long as there are still letters left in the hand:

    while True:
        # Display the hand
        displayHand(hand) 

        # Ask user for input

        inp =compChooseWord(hand, wordList, n)
        if inp==None :
            return None 


        # If the input is a single period:
        
        # Otherwise (the input is not a single period):

            # If the word is not valid:
        elif not isValidWord(inp,hand,wordList):

            # Reject invalid word (print a message followed by a blank line)

            print ("Invalid word, please try again.")

            # Otherwise (the word is valid):

        else:
            curr_score= getWordScore(inp, n)
            tot_score += curr_score
            
            print ('"'+inp + '" earned ' + str(curr_score) + ' points. Total: ' + str(tot_score) + ' points')
            hand= updateHand(hand, inp)
            if len(inp)!=0:
                displayHand(hand)
               
                break
        