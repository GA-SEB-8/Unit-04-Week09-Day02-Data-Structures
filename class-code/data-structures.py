# Lists
# Dictionaries
# Tuples

my_students = ['Abdullah','Malak','Amna','Mohammad','Ali']




# access 1 value in my List
print(my_students[2])


# Changing value in array
my_students[1] = 'Yaqoob'


print(my_students)

# index in the negative
print(my_students[-2])


# push() == append(): adds to the end of the List
my_students.append("yusef")

print(my_students)



# extend(): adds multiple values to the List
my_students.extend(['Ayah','Mariam'])

print(my_students)


# len(): returns the length of the List
print(len(my_students))


# pop(): removes the last element from the List
my_students.pop()
print(my_students)



# pop(n): removes the nth indexed element
my_students.pop(0)

print(my_students)




# insert(): adds an element to our List at an index
my_students.insert(0,'Hesa')

print(my_students)


# remove(): removes an element from the array
my_students.remove("Ali")
print(my_students)



# clear(): empties the entire list
my_students.clear()

print(my_students)

my_students.extend(['Hesa', 'Yaqoob', 'Amna', 'Mohammad', 'yusef', 'Ayah'])
print(my_students)



# looping through a list

for index,student in enumerate(my_students):
    print(f"{index +1}: {student} is in Software Engineering")


# print(list(enumerate(my_students)))


print(my_students)

print(my_students[0:4:2])
# same thing as above
print(my_students[:2])

# my_students[start:stop:step]
print(my_students[::3])


print(my_students)

# removing from the list and adding in that position
my_students[0:2] = ["NEW VALUE","Sayed"]

print(my_students)


# adding to the middle of the List without removing
my_students[2:2] = ["Added Value","Mooza"]

print(my_students)


# deletes the values in the slice
del my_students[1:4]


print(my_students)


# Tuple: Emutable (Never Changing) List

colors = ('Red','Blue','Green')

print(colors)

print(colors[1])

# colors[1] = 'Purple'

print(colors[0:3])



# Dictionaries

ga_student = {
    "name":"Abdullah",
    "favorite_language":"Python"
}

print(ga_student)

# get a value from my dictionary
print(ga_student['name'])
print(ga_student['favorite_language'])


#