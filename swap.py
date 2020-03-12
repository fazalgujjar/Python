def swap(x,y):
    x = x+y
    y = x-y
    x = x-y
    print(f"\nafter swap first number{x} and second number{y}")
    
x = int(input("Please enter first number: "))
y = int(input("Please enter second number: "))
print(f"first number {x} and second number {y}")
swap(x,y)