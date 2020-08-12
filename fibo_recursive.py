def fibonacci_series(n):
    if (n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return (fibonacci_series(n-2) + fibonacci_series(n-1))
n = int(input("enter the value : "))
print("fibonacci series : ")
for n in range (0,n):
     print(fibonacci_series(n))
fibonacci_series()