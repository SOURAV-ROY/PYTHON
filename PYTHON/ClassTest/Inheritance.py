class Animal():
    def walk(self):
        print("Walk")


class Dog(Animal):
    pass
    # def bark(self):
    #     print("Bark")


class Cat(Animal):
    # pass
    def sound(self):
        print("MEU MEU")


dog1 = Dog()
print("*****DOG*****")
dog1.walk()
# dog1.bark()

cat1 = Cat()
print("*****CAT*****")
cat1.walk()
cat1.sound()
