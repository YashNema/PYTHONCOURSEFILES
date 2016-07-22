balance=32000000000
annualInterestRate=0.2
interest = annualInterestRate / 12
monthlyinterest = 0
low = balance / 12
high = (balance * (1 + interest)**12) / 12.0
newBalance = balance
month = 0
epsilon = 0.00001
while abs(newBalance) > epsilon:
    pay = (high + low) / 2
    newBalance = balance
    month = 0
    while month < 12:
        newBalance -= pay
        monthlyinterest = interest * newBalance
        newBalance += monthlyinterest
        month += 1
    if newBalance > 0:
        low = pay
    else:
        high = pay
print str(round(pay,2))
