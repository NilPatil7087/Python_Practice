def insertion_sort(n):
    for i in range(1,len(n)):
        number = n[i]
        position = i-1
        while(number < n[position] and position >=0 ):
            n[position + 1] = n[position]
            position -= 1
        n[position + 1] = number
list = [2,4,6,8,0,1]
insertion_sort(list)
print(list)

list1 = [100000,10000,1000,100,10]
insertion_sort(list1)
print(list1)