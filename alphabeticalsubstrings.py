longest_alpha_ord =''
length=''
for i in range(len(s)-1):
        if ord(s[i])<=ord(s[i+1]):
            length=length+(s[i])
        
        else:
            length=length+s[i]
            if len(length)>len(longest_alpha_ord):
                longest_alpha_ord=length
            length=""    
     
length=length+s[len(s)-1]
if len(length)>len(longest_alpha_ord):
                longest_alpha_ord=length

if len(longest_alpha_ord)==0:
        print 'Longest substring in alphabetical order is:' +length
else:
    print 'Longest substring in alphabetical order is:' +longest_alpha_ord        