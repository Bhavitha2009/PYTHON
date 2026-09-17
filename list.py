#accessing elements in a list
#here index starts from 0 and ends at n-1
#length starts from 1 and ends at n

marks=[80,70,90,95]
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])


#list in python
#list is an ordered and changeable collection that can store multiple values
marks=[60,59,67,90]

print(marks)

#change elements in a list
marks=[80,90,75]

marks[1]=95

print(marks)

#add elements to a list
#append=it adds an element to the end of the list

marks=[80,90,75]

marks.append(85)

print(marks)

#remove elements from a list
marks=[70,60,80,90]

marks.remove(90)

print(marks)

#insert=it adds an element at a specific index in the list

numbers=[10,20,30,40]

numbers.insert(3,25)

print(numbers)

#example:-
numbers=[10,20,30,40]
numbers.insert(1,15)
numbers.insert(2,25)
print(numbers)

#extend method

a=[1,2,3]
b=[4,5,6]

a.extend(b)

print(a)

#clear method
numbers=[10,20,30]

numbers.clear()

print(numbers)

numbers=[10,30,20,40,60,79,80,50]

print(numbers.index(40))
print(numbers.index(80))
print(numbers.index(50))

#count method
numbers=[20,50,89,6,56,40.50,20,65,56]

print(numbers.count(50))
print(numbers.count(56))

#sort method:-

numbers=[10,20,40,50,70,30]

numbers.sort()

print(numbers)

numbers.sort(reverse=True)

print(numbers)

#reverse method

numbers=[30,60,70,80]

numbers.reverse()

print(numbers)

#copy method
a=[1,2,3,4,5,6]
b=a.copy()

print(b)

#:,:,-1 means slicing (start,stop,step)

numbers=[10,20,30,40,50,60,70,80]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])
print(numbers[1:7:2])
print(numbers[6:1:-2])

