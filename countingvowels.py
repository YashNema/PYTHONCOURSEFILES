count = 0
s="aeaafr"
for i in range(len(s)):
  if s[i].lower() in 'aeiou':
      count+=1 
print count