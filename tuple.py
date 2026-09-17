#tuples in python
#tuple is a collection of multiple values that is ordered and not changeable after creation
student=("bhavitha",89,"python")

print(student[0])

#access values in a tuple
student=("Bhavitha",34,67.4)

print(student[0])
print(student[1])
print(student[2])

#immutable nature of tuples
#student=("Bhavitha",76,90)

#student[2]=23

#print(student)
#it returns an error because it is not changeable

#tuples are immuttable
numbers=(10,20,30,40,20)

print(numbers.count(20))

#index tuple
numbers=(10,20,30,40,50,60)
print(numbers.index(60))

numbers=(10,20,30,40,50)

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

