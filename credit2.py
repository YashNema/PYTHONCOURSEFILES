minimum=10
balance=4787
annualInterestRate=0.2
temp=balance
remainingBalance=1
monthlyInterestRate=annualInterestRate/12.0
while(remainingBalance>0):
    previousBalance=balance
    for i in range(0,12):
      monthlyUnpaidBalance=previousBalance-minimum
      remainingBalance=monthlyUnpaidBalance+(monthlyInterestRate*monthlyUnpaidBalance)
      previousBalance=remainingBalance
    if(remainingBalance>0):
          minimum+=10
    else:
          break

print "Lowest Payment"+str(minimum) 