#logical operators
#AND operator
age=25
citizen=True

print(age>=18 and citizen==True)


#OR operator
has_card=False
has_cash=True

print(has_card or has_cash)

#NOT operator
is_logged_in= False

print(not is_logged_in)
#atm aligibility checker
balance=10000
withdraw=5000

print(withdraw>0 and withdraw>=balance)

#student scholarship eligibility checker
marks=float(input("enter marks:"))
attendence=float(input("enter attendence:"))

eligible=marks>=85 and attendence>=67

print("scholarship eligible:",eligible)

#identity operator
a=None

print(a is None)
print(a is not None)

#bitwise operator ,code=8421
#
a=5
b=3

print(a & b)
print(a | b)
print(a ^ b)
print(a << b)
print(a >> b)

#electric bill calculator
units=int(input("enter electicity units:"))

rate=6

bill=units*rate

print("electricity bill:",bill)

#travel expense calculator
travel=float(input("travel expense:"))
food=float(input("food expense:"))
hotel=float(input("hotel expense:"))

total=travel+food+hotel

print("total expense:",total)

