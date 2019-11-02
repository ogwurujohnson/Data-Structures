class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = []

    def push(self, value):
        self.storage.append(value)
        self.size +=1

    def pop(self):
        if len(self.storage) == 0:
            return None
        self.size -=1
        return self.storage.pop()

    def len(self):
        return self.size
