
colors = ["red", "yellow", "green"]

print(colors)

# accessing elements: arr[index]

print(colors[2])


# we can also go backwards

print(colors[-1])



colors[0] = "purple"

print(colors)


# push == append()
# add to the end
colors.append("pink")

print(colors)


students = ["Sayed","Yusef","Israa"]
# append() only adds 1 value.
# if i want to add more than 1 value I use extend

students.extend(['nooreen','sara'])

print(students)


# we can also insert at an index with insert() method
# insert(): adds an element at an index
students.insert(0,"Ahmad")

print(students)


print(len(students))


# pop(): removes the last element

students.pop()

print(students)


# pop can take an arguement. the index
students.pop(3)

print(students)

print(students)


# removes an element
students.remove("Yusef")

print(students)

# clear(): clears my list
students.clear()
print(students)


students.extend(["sayed","sayed","Sayed","Yusef","Israa"])

students.remove("sayed")


print(students)



noSayeds = list(filter(lambda student : student.lower() != "sayed",students))

print(noSayeds)


for student in students:
    print(f"{student} is doing great")




for index, student in enumerate(students):
    print(f" {index}: {student}")

print(list(enumerate(students)))



my_student = {
    "name":"Aisha",
    "favorite_language":"Python"
}

print(my_student)


# accessing a value
print(my_student["favorite_language"])


# changing a value
my_student["name"] = "Mohammad"

print(my_student)


# add a new key value pair
my_student["course"] = "Software Engineering"

print(my_student)


# removing key value pairs
del my_student["course"]

print(my_student)




print(list(my_student.items()))



# looping through a dictionary
for key, value in my_student.items():
    print(f"{key}-----> {value}")


# only loops through the keys
for key in my_student:
    print(f"{key}: {my_student[key]}")







# tupples
colors = ("red","blue","green")

print(colors)


# 1 tupple
eligebile_students = ("Sayed",)

print(type(eligebile_students
))



for color in colors:
    print(color)

for index, color in enumerate(colors):
    print(f"{index}:{color}")




students = ["sayed","Yusef","Aisha","Israa","nooreen"]
# slicing
# [start,stop] (stop is not included)
print(colors[1:3])

print(students)

# [start,stop,step]
print(students[::-2])

print(students)

students[1:1] = ["NEW VALUE"]

print(students)


del students[1:3]

print(students)
