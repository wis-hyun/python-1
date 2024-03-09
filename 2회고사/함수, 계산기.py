def calculator(op, num1, num2):
    if op=='+': result=num1+num2
    elif op=='-': result=num1-num2
    elif op=='*': result=num1*num2
    elif op=='/': result=num1/num2

    return result

op=input('계산입력(+,-,*,/) :')
n1 = int(input('숫자 1 입력 : '))
n2 = int(input('숫자 2 입력 : '))
res=calculator(op, n1, n2)
print(n1,op,n2,'=',res)
