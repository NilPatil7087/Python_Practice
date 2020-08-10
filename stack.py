class stack:
    def __init__(self):
        self.items = list()

    def is_empty(self):
        if len(self.items) == 0 :
            return True
        else:
            return False
    def peek(self):
        return  self.items[len(self.items)- 1]

    def push(self,word):
        return self.items.append(word)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print(self):
      print (self.items)