x=56
eps=.01
step=eps**2
num=0
ans=0.0
while (abs(ans**2-x))>=eps and ans<=x:
    ans=ans +step
    num=num+1
print 'numguesses = '+str(num)
if (abs(ans**2-x))>=eps:
    print ('Failed to get square room of '+str(x))
else:
    print (str(ans) +' is close to the square root of '+str(x))