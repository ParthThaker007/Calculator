# m=10
# n=5
# print("Add=",m+n)
# print("sub=",m-n)
# print("Div=",m/n)
# print("mul=",m*n)
# print("expo=",m**n)
# def calculator():
print("Calculator")
print("-----------")
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

result = None
if operator == '+':
        result = num1 + num2
elif operator == '-':
        result = num1 - num2
elif operator == '*':
        result = num1 * num2
elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Cannot divide by zero!") 
    
    

if result is not None:
        print("Result:", result)
else:
        print("Invalid operator!")

# calculator()
