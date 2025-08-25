cat1 = {
    'name':'zoro',
    'age':2
}

cat2 = {
    'name':'luffy',
    'age':7
}


# creating a new class
class Cat():
    # rule 1: every clas has an __init__() method
    # rule 2: ALL class methods first argument is self
    def __init__(self, name, age, fur_color='white'):
        print("__init__ method called")
        self.name = name
        self.age = age
        self.fur_color = fur_color
        self.is_alive = True
    
    # method
    def speak(self):
        print("Meow " + self.name)






# creating a new object instance of a cat class
cat3 = Cat('luffy',10, 'red')
cat4 = Cat('zoro',4)


# calling a method on cat3
cat3.speak()


print(cat3.name)



# exercise 1: create a class called Student
# this class should have the following properties: name and country
# this class should have 1 method introduce_self(): which should print
# my name is {name} and I am from {country}

class Student():

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def introduce_self(self):
        print(f"my name is {self.name} and I am from {self.country}")

    def __str__(self):
        return f'name={self.name}, country={self.country}'

mohammad = Student('Mohammad','Bahrian')
yusef = Student('yusef','Bahrian')

# changing the value of a property for the object
mohammad.country='Saudi'

print(mohammad)
