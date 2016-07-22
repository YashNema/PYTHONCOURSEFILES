def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    # Your code here
    s = []
    for i in aList:
        if len(i)<4:
            s.append(i)
    return s
            
        
        