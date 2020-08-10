from stack import stack

A = stack()

A.print()

print("Empty?", A.is_empty())
print("Size of the stack = ", A.size())

A.push(10)
A.push(11)
A.push(12)

A.print()


print("Empty?", A.is_empty())
print("Size of the stack = ",A.size())

item = A.pop()
A.print()

print("item popped = ", item)
print("Size of the stack = ", A.size())

print("Top element = ",A.peek())
A.print()