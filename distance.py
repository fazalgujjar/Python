def dif(number1,number2):
    total=(number1*12) + number2
    return total
    

number1 = int(input("Please enter feet of A value"))
number2 = int(input("Please enter inch of A value"))
first= dif(number1,number2)

number1 = int(input("Please enter feet of B value"))
number2 = int(input("Please enter inch of B value"))
second = dif(number1,number2)

if first > second:
    print(f" A is greater than B")
else:
     print(f"B is greater than A")
    
    