elements = [1,2,"3",4]

#print(elements[2]+str(elements[3]))

#print(elements[-2])

elements = list(range(5))
#print(elements)

d = {"banana":2} #dictionary

d["bob"] = "alice"
d["bob"] = "steve"

#print(d.keys())

pair = (1,2,3,4,5,6,7,8)
pair = (1,2)
#pair[0] = 3
#print(pair)


x = 5

def set_x(num):
    x=num
    print(x)

def global_set_x(num):
    global x
    print(x)
    x=num
    print(x)

#set_x(4)
#global_set_x(7)
#print(x)

class Human:
    spec = "H. Sapiens"

    def __init__(self, name):
        self.name = name
        self.age = 0

    def grunt(self):
        return self.name

    @staticmethod
    def grunt2():
        return "grunt"

    def printHuman(self):
        print(self.name)

class MetaHuman(Human):
    def __init__(self, power, name):
        self.power = power
        Human.__init__(self,name)

    def printHuman(self):
        print(str(self.name) + " has " + str(self.power) + " power")

    class Power:
        def __init__(self, power):
            self.power = power

aHuman = Human("Tracey")
mHuman = MetaHuman(5,"Rio")
aHuman.printHuman()
mHuman.printHuman()
#print(aHuman.grunt())

from math import sqrt
print(sqrt(5))
