#dictionery:key value pairs,unordered,muteable and represented by{}
#key(name,marks)
#values(bhavitha,98)
#item(both
student={
    "name":"bhavitha",
    "age":17,
    "course":"python"
}
print(student)

#accessing elements in dictionery
print(student["name"])
print(student["age"])
print(student["course"])

#change values in a dictionery

student["age"]=16

print(student["age"])

#add new data toa dictionery
student["city"]="tirupati"
print(student)

#remove data
#pop()removes the specified key and its value
student.pop("city")

print(student)

print(student.keys())
#keys()returns all key in the dictionery
print(student.values())
# value()returns all values in the dictionery
print(student.items())
#items()returns all key value pairs
print(student.get("name"))
#get ()returns the value of the specified key
student.update({"age":18})
#update()updates the value of the specified key

print(student)

#popitem() removes the last inserted key value pair
student={
    "name":"bhavitha",
    "age":17,
    "course":"python"
}
student.popitem()
print(student)

#set default :if we want add then we  use set default
student={
    "name":"bhavitha"
}
student.setdefault("age",17)

print(student)

#clear method
student.clear()

print(student)

#copy method
student={
    "name":"bhavitha",
    "age":17
}

new_student=student.copy()

print(new_student)

#order of evaluation(BODMASS)

result=2+13*2

print(result)

result=(10+5)*2

print(result)
