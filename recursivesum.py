def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    if N==0:
        return 0
    else:
        return N%10+sumDigits(N/10)
 