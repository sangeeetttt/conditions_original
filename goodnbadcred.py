'''
Price of a house is $1M. If the buyer has good credit, they need to put down 10% otherwise they need to put down 20%.
Print the down payment.
'''
price = 1000000
yourBank = int(input('The money that you have: '))
good_credit = False
if good_credit:
    down_payment = (10/100*price)
else:
    down_payment = (20/100*price)

print(f'downpayment is ${down_payment}')