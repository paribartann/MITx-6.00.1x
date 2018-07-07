

# © Paribartan Dhakal
# July 6, 2018 

#Problem 1

monthlyInterestRate=annualInterestRate/12.0        
for i in range(12):
    minimumMonthlyPayment=monthlyPaymentRate*balance
    monthlyUnpaidBalance=balance-minimumMonthlyPayment 
    balance=monthlyUnpaidBalance+monthlyInterestRate*monthlyUnpaidBalance
    i=i+1
        
print('Remaining balance: {}'.format(round(balance,2)))


#problem 2

minimumFixedPayment=0
monthlyInterestRate=annualInterestRate/12.0

tempBalance=balance
   
while tempBalance>0:
   minimumFixedPayment +=10
   
   for month in range(12):
       tempBalance-=minimumFixedPayment
       tempBalance+=monthlyInterestRate*tempBalance
       
   if tempBalance>0:
       tempBalance=balance
       
print('Minimum fixed payment: {}'.format(round(minimumFixedPayment,2)))

#Problem 3

monthlyInterestRate=annualInterestRate/12.0

lowerBound=balance/12
upperBound=(balance*(1+monthlyInterestRate)**12)/12.0


tempBalance=balance

while balance!=0.00:
    minimumFixedPayment=(lowerBound+upperBound)/2
    balance=tempBalance
    
    for month in range(12):
       balance = ((balance - minimumFixedPayment) * (1 + monthlyInterestRate))
    
    if balance>0:
        lowerBound=minimumFixedPayment
    elif balance<0:
        upperBound=minimumFixedPayment
        
    balance=round(balance,2)
    
print('Lowest payment: {}'.format(round(minimumFixedPayment,2)))