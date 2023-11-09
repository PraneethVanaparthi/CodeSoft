def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def divide(x,y):
    if y==0:
        return "cannot divide by zero"
    return x/y
def multiply(x,y):
    return x*y

print("select an operation:")
print("1.ADDITION")
print("2.SUBTRACT")
print("3.DIVIDE")
print("4.MULTIPLY")

choice = input("Enter the operation:")

if choice in ['1','2','3','4',]:
    num1=float(input("enter the first number:"))
    num2=float(input("enter the second number:"))

    if choice =='1':
        result=add(num1,num2)
    elif choice =='2':
        result=subtract(num1,num2)
    elif choice =='3':
        result=divide(num1,num2)
    elif choice =='4':
        result=multiply(num1,num2)
    
    print("Result:",result)
else:
    print("enter the valid operation")