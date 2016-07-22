balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
total_paid=0
month = 1
while month < 13:
    minimum_monthly_payement=balance*monthlyPaymentRate
    unpaid_balance=balance-minimum_monthly_payement
    interest=unpaid_balance*(annualInterestRate/12) 
    updated_balance=unpaid_balance+interest
    print "Month: " + str(month)
    print "Minimum monthly payment: "+str(round(minimum_monthly_payement,2))
    print "Remaining balance: "+str(round(updated_balance,2))
    balance=updated_balance
    month=month + 1
    total_paid=total_paid + minimum_monthly_payement

print "Total paid : " +str(round(total_paid, 2))
print "Remaining balance: " + str(round(updated_balance, 2))