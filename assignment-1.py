#personal details
name=input("enter name")
age=int(input("enter age"))
height=float(input("enter height"))

print(name)
print(age)
print(height)

#personalized greeting
name=input("enter name")
print("hello ,{name}!")

#add two num read as string into integer
a=input("enter a num")
b=input("enter a num")
x=int(a)
y=int(b)
total=x+y
print(total)

#float to integer 
n=float(input("enter number"))
print(n)

new=int(n)
print(new)

#sum using arthematic operator
a=int(input("enter a number:"))
b=int(input("enter a number:"))

print(a+b)

#area of a rectangle
length=float(input("enter length:"))
breadth=float(input("enter breadth:"))

area = length * breadth
print("length:",length)
print("breadth:",breadth)
print(area)

#quotient and remainder
a=int(input("enter number:"))
b=int(input("enter number:"))

q=a/b
r=a%b
print(q)
print(r)

#power calculation
base=int(input("enter base number"))
exponent=int(input("enter exponent number "))
power=base**exponent

print("base:",base)
print("exponent:",exponent)
print("power:",power)

#average of 3 num
n1=int(input("enter n1:"))
n2=int(input("enter n2:"))
n3=int(input("enter n3:"))

total=n1+n2+n3
average=total/3

print(average)

#greater than the comparision

n1=int(input("enter n1:"))
n2=int(input("enter n2:"))
print(n1>n2)

#equality check
n1=int(input("enter n1:"))
n2=int(input("enter n2:"))
print(n1==n2)

#both numbers positive check
a=int(input("enter number1:"))
b=int(input("enter number 2:"))

print(a>0 and b>0)

#atleast one is even number
a=int(input("enter a number"))
b=int(input("enetr a number"))

print(a%2==0 or b%2==0)

#logical not operator

a=int(input("enter number"))
b=int(input("enter number"))

print(not(a==b))

#assignment operators

a=23
b=90

print(a+b)
print(a*b)
print(a%b)

n1=int(input("enter a number"))
n2=int(input("enter a number"))

a=n1+6
b=n2*4
c=n1-56
d=n2%4

print(a)
print(b)
print(c)
print(d)

#exchange values of two variables

a=int(input("enter a value:"))
b=int(input("enter a value:"))

#calculate simple interrest
principle=float(input("enter principle:"))
time=float(input("enter time:"))
rate=float(input("enter rate:"))

si=principle*rate*time/100

print(si)

#temparature conversion
c=float(input("enter c:"))
f=(c*9/5)+32
print(f)

#check divisibility by 3 and5
n=int(input("enter a number:"))
print(n%3==0 and n%5==0)

#sum of digits of a two digit number
num=int(input("enter num:"))
tens=num//10
units=num%10
total=tens+units
print(total)




