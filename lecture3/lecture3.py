print("Hello World")

#dynamic typing
variable = 4.0
var2 = "string"
var3 = 3 # int
intfraction = int(3/4) #casting to an int

#type cast & string concat
print(var2 + " " + str(variable))

boolean = True
#print(boolean)

def isBoolean(value):
    if value:
        print("True")
    elif not value:
        print("False")
    else:
        print("How did you get here?")

isBoolean(boolean)
isBoolean(not boolean)

listofNums = [1,2,3]

# for value in listofNums:
#     print(value, end=",")

print(listofNums[-1])

#print(listofNums)
