print('''
+ ADD
- SUBTRACT
* MULTIPLY
/ DIVIDE
''')
num1=int(input("enter the value : 1"))
num2=int(input("enter the value : 2"))
num3=int(input("enter the value : 3"))
num4=int(input("enter the value : 4"))
opr=input("enter the opr")
if opr=="+":
  print(num1+num2)
elif opr=="-":
  print(num1-num2)
elif opr=="*":
  print(num1*num2)
elif opr=="/":
  print(num1/num2) 
else:
  print("invalid")