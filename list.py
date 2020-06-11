#List orderd collection of object
cars =[]
print(cars)
cars=["hondacity","swift","Audi","alto","innova","scorpio","fortuner","iconford","ferrari","verna"]
print(cars)


bikes=["pulser","fz","r15","pulserNS","pulser220"]

#append
cars.append("porshe")
cars.append("mini")



#concat another list of bike
cars.append(bikes)
print(cars)

#remove
cars.remove("alto")
print(cars)
bikes.remove("pulser")
print(bikes)

#if
if"porshe"in cars:
    print("porshe is there")

#extend
    fruits = ["mango","orange","pineapple","apple"]
    fruits.extend(cars)
    print(fruits)

    a = ["1","2","3"]
    b =["a","b","c"]
    a.extend(b)
    print(a)
    
#index
    x = cars.index("porshe")
    print(x)

#insert
    fruits.insert(0,"strawberry")
    print(fruits)

    cars.insert(10,"volkswagen")
    print(cars)

#pop
    cars.pop(1)
    print(cars)

#reverse
    cars.reverse()
    print(cars)




    
