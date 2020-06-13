print("-------------------Program--------------------------------------")
car =['bmw', 'audi', 'porshe']
print(car)
print("------------------Reverse-----------------------------------------")
car.reverse()
print(car)

#sorted
print(sorted(car))
print(car)

#length
print(len(car))

for car in car:
    print(car.title())

for value in range(1,1):
    print(value)

for number in [1,2,4,2]:
    print(number)

numbers =[11,155,266,677,8]
smallest_number =min(numbers)
print(smallest_number)


numbers =[111,2222,4567,5678,11111]
biggest_number = max(numbers)
print(biggest_number)


print("sum of all numbers:",sum(numbers))

#LIst Comprehension allows you to generate a list using some code:
#**exponent

squares =[x**2 for x in range(1,11)]
print(squares)

print("----------------------------------------")
for x in range(11,20):
    print(x**2)
print("-----------------------------")

cubes=[x**3 for x in range(1,11)]

#slice of list
print("cubes of first 4 numbers:",cubes[0:5])

print("squares of first 2 numbers:",squares[0:3])

print("cubes of 10 numbers:",cubes[0:11])

start =0
end= 10
print(cubes[:end])
print(cubes[start:5])

#list in python mutable(changeable)
#tuple : you cant change values

x = (2,4) #using a round bracket is a tuples
print(x)
print(x[0]) #accessing the value

for i in x :
    print(i)

x=(3,9) #types are dynamic
print(x[0])

