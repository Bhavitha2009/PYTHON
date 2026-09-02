#simple calculator
a=int(input("enter first number:"))
b=int(input("enter second number:"))

print("addition :",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)

#student marks calculator
name=input("enter student name:")

m1=int(input("enter marks of python:"))
m2=int(input("enter marks of java:"))
m3=int(input("enter marks ofc++:"))

total=m1+m2+m3
average=total/3

print("/n------------student report------------")
print("name:",name)
print("total",total)
print("average",average)

#shopping bill calculator
price1=float(input("enter product 1 price"))
price2=float(input("enter product 2 price"))
price3=float(input("enter product 3 price"))

total =price1+price2+price3
print("total",total)
discount=total*0.10
final_amount=total-discount
print("discount:",discount)
print("final_amount",final_amount)

#salary calculator
basic=float(input("enter basic salary:"))

hra=basic*0.20
da=basic*0.10

gross_salary=basic+hra+da

print("basic salary:",basic)
print("hra:",hra)
print("da:",da)
print("gross_salary:",gross_salary)