def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    s=0
    x=hand.copy()
    for key, value in x.items():
         s=s+int(value)
    return s