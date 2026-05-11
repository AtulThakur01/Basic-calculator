# simple calculator project

num1=int(input("enter first number"))
num2=int(input("enter second number"))
opr=input("enter the opr")

if opr=="+":
    print("addition",num1+num2)
elif opr=="-":
    print("subtraction",num1-num2) 
elif opr=="*":
    print("multiplication",num1*num2)
elif opr=="/":
    print("division",num1/num2)
else:     
    print("invalid operation")  