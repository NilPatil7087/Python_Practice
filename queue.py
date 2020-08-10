class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self,item):
        return self.items.insert(0,item)

    def dequeue(self):
        if self.size() == 0:
            raise WindowsError("queue is empty")
        return self.items.pop()
q = Queue()
print("size =",q.size())
print("is_empty=",q.is_empty())

q.enqueue("Mumbai")
q.enqueue("delhi")
q.enqueue("pune")

print("size =",q.size())
print("is_empty=",q.is_empty())

q.dequeue()
print("size =",q.size())
q.dequeue()
print("size =",q.size())
q.dequeue()
print("size =",q.size())

print("size =",q.size())
print("is_empty=",q.is_empty())
