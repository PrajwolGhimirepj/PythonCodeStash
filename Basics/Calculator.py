def calculate(a,b,Operator):
    result=0
    if Operator=="+":
        result=a+b
    elif Operator=="-":
        result=a-b
    elif Operator=="*": 
        result=a*b
    elif Operator=="/":
        result=a/b
    return result

input1=int(input("Enter first number: "))
input2=int(input("Enter second number: "))
operator=input("Enter operator: ")

print(calculate(input1,input2,operator))