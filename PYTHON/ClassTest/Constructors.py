class Point:
    # def __init__(self, x, y):
    #     self.x = x
    #     self.y = y
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")

    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


# point = Point(10, 20)
# point.x = 11
# print(point.x)

john = Point("Sourav Roy")
# print(john.name)
john.talk()

don = Point('DON')
don.talk()
