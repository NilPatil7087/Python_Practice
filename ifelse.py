bikes = ["pulser","Fz","kawasaki","harley","r15"]
for bikes in bikes:
    if bikes =='harley':
        print(bikes.upper())
    else:
        print(bikes.title())

print("__"*30)
bikes = ["pulser","Fz","kawasaki","harley","r15"]
if 'pulser' in bikes:
    print("i have a pulser in list")
else:
    print("no pulser in the list")


print("__"*30)

#admission fee for a park
#age<4:free
#4-18=25$
#>18=40$

age =45
if age < 4:
    print("admission fee is 4$")
elif age < 18:
    print("admission fee is 25$")
else:
    print("admission fee is 40$")

print("__"*30)

marks = int(input("Type a number:"))
if marks > 90: 
     print("A grade")
elif marks > 80 and marks <89:
     print("B Grade")
elif marks >60 and marks <79:
     print("c Grade")
elif marks >33 and marks <59:
     print("D Grade")
else:
     print("fail")
