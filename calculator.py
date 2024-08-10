value1=int(input("Enter first value\n"))
value2=int(input("Enter Second value\n"))
answer=0
sign=0
while sign !='e':
 print("+ for Addition")
 print("- for Subtraction")
 print("* for Multiplication")
 print("/ for Division")
 print("c for changing values")
 print("e for exit")
 sign=input("Enter the command you want to execute ")
 if sign=='e':
    exit()
 if sign=='+':
    answer=value1+value2
    print(answer)

 elif sign=='-':
    answer=value1-value2
    print (answer)
 elif sign=='*':
    answer=value1*value2
    print (answer)
 elif sign=='/':
    answer=value1/value2
    print (answer)
 elif sign=='c':
    value1=int(input("Enter first value\n"))
    value2=int(input("Enter Second value\n"))
 else :
    print("PLease write the from menu")