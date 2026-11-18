def welcome():
    print(" welcome to pthon programming")

welcome()

def person(name,age):
    print(name)
    print(age)


name = input("what is your name\n")
age = input("what is your age\n")
person(name,age)

def sum(a,b):
    return a+b

s= int(input ("enter first number\n"))
v= int(input ("enter second number\n"))
result = sum(s,v)
print(result)

def sum(t,y):
    return t+y

def dif(t,y):
    return t- y

def mul(t,y):
    return t*y

def div(t,y):
    return t/y

t = int(input ("enter first number\n"))
y= int(input ("enter second number\n"))
operation = input("what should be performed\n 1.sum \n 2.diffrence \n 3.multiplication \n 4.division \n")
if operation == "+":
   result = sum(t,y)
   print("Sum is",result)
elif operation == "-":
   result = dif(t,y)
   print("diffrence is",result)
elif operation == "*":
   result = mul(t,y)
   print("multiplication is",result)
else :
   result = div(t,y)
   print("division is",result)