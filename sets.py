#sets in python
#set is a collection of unique values that is unordered and muteable or changeable
numbers={10,20,30,20,10}

print(numbers)

#why we use set?

#suppose students have selected subjects
subjects={"python","java","sql","java"}

print(subjects)

#add values to a set
subjects={"python","java"}

subjects.add("sql")
print(subjects)

#remove values from a set
subjects={"python","sql","java"}
subjects.remove("java")

print(subjects)

#sets do not allow duplicate values
numbers={1,2,2,3,4,5,5,6,7}

print(numbers)

#average of 3 numbers
n1=int(input("enter number 1:"))
n2=int(input("enter number 2:"))
n3=int(input("enter number 3:"))
total=n1+n2+n3
average=n1+n2+n3/3
print(total)
print(average)

#greater than comparison

a=int(input("enter a number:"))
b=int(input("enter a number:"))
print(a>b)

#equality check
n1=int(input("enter a number:"))
n2=int(input("enter a number:"))

print(n1==n2)