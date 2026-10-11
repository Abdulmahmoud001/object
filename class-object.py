class student:
    grade = 10
    print("Hi, i am a student of grade", grade)

ob = student()



class fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def intro(self):
        print("hello, i am", self.name)

apple = fruit("apple", "red")
apple.intro()



class people:
    grade = 10
    name = "Penguin"

    def introduction(self):
        print("Hi, i am a student")

    def details(self):
        print("My name is", self.name)
        print("I study in grade", self.grade)

ob = people()
ob.introduction()
ob.details()




class parrot:

    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

blue = parrot("Blu", 10)
wood = parrot("Woo", 15)

print("Blu is a {}".format(blue.species))
print("Woo is also a {}".format(wood.species))

print("{} is {} years old".format(blue.name, blue.age))
print("{} is {} years old".format(wood.name, wood.age))


class parrot:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

blue = parrot("Blu", 10)
print(blue.sing("'Happy'"))
print(blue.dance())