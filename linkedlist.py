class Node:

    def __init__(self, value):
        self.data = value
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, value):
        self.data = value

    def set_next(self, next_node):
        self.next = next_node

class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    # adds new node to the head of the list
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def display(self):
        current = self.head
        print("List contents : ", end='')
        while current is not None:
            print(current.get_data(), " ", end='')
            current = current.get_next()
        print("\n")

    def search(self, item):
        current = self.head

        while current is not None:
            if current.get_data() == item:
                return True
            else:
                current = current.get_next()

        return False

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if found:
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

my_list = LinkedList()
print("size =", my_list.size())
my_list.display()

my_list.add(10)
print("size =", my_list.size())
my_list.display()

my_list.add(20)
my_list.add(30)
my_list.add(40)
print("size =", my_list.size())
my_list.display()

print("Is 30 present ? ", my_list.search(30))

print("Is 50 present ? ", my_list.search(50))

print("Before removing")
my_list.display()

my_list.remove(20)

print("After removing")
my_list.display()

my_list.remove(30)
my_list.display()

my_list.add(70)
my_list.display()

my_list.remove(40)
my_list.display()
print("size=", my_list.size())