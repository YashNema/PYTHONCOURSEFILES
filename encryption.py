def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.
    coder={}    
    for i in string.ascii_lowercase:
        coder[i] = i  
    for i in string.ascii_uppercase:
        coder[i] = i  
              
    for ch in coder.keys():
            if ch.isalpha():
                if ord(ch)<91:
                    stayInAlphabet = ord(ch) + shift 
                    if stayInAlphabet > ord('Z'):
                        stayInAlphabet -= 26
                    coder[ch] = chr(stayInAlphabet)
                else:
                    stayInAlphabet = ord(ch) + shift 
                    if stayInAlphabet > ord('z'):
                        stayInAlphabet -= 26
                    coder[ch] = chr(stayInAlphabet)
            
    return coder
def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
    cipherText = ""                          
    for ch in text:
        if ch.isalpha():
            cipherText +=coder[ch]
        else:
            cipherText+=ch
    return cipherText
def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    return applyCoder(text,buildCoder(shift))

