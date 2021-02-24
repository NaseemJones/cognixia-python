name = "world"
print("Hello", name + "!")
print(5**2)
print(7//3)

print("enter 1st number")
x = int(input())
print("enter 2nd number")
y = int(input())
print ("Sum: ", x + y )
print ("Difference: ", x - y )

def greeting(intro,name):
    print(intro, name + "!")

greeting("hello","josh")

def area_of_cir(radius):
    return (3.14 * (radius**2))

c_area = area_of_cir(4)

def c_vol(radvalue):
    print(radvalue * 10)

print("Volume ")
c_vol(c_area)

