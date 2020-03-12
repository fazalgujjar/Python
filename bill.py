first_bill = int(input("please Enter 1st month bill amount"))
bill_paid = input('Please inter Y if bill paid or N if not paid')
if bill_paid == 'y' or bill_paid == 'Y':
    print('Thanks for payment')
elif bill_paid == 'n' or bill_paid == 'N':
    for i in range(0,5):
        first_bill = first_bill + (first_bill*0.12)
    
else:
    print("Please enter y or n")
print(first_bill)