number_1=float(input("enter first number: "))
operand=input("enter the type of operand for operation that you want to perform(+,-,*,/,%): ")
number_2=float(input("enter second number: "))
if operand=='+':
    result=number_1+number_2
elif operand=='-':
    result=number_1-number_2
elif operand=='*':
    result=number_1*number_2
elif operand=='/':
    result=number_1/number_2
elif operand=='%':
    result=number_1%number_2
else:
    print("invalid input")
print(result)
