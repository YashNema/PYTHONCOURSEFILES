countBob = 0
for n in range(0, len(s)):
    if s[n:n+3] == 'bob':
        countBob += 1
print('Number of Bob is: ' + str(countBob))