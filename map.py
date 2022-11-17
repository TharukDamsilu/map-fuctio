ary = []
l = True

while l == True:
    name = input("Student name: ")
    age  = (input("Student age: "))

    if (age == '18'):
        l = False

    ary.append([name, age])

def func(x):
    x.append("Ananda College")
    return x

print(list(map(func, ary)))