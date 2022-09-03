class EmptyStackException(Exception):
    pass

class Contract(object):
    def __init__(self):
        self.contracts = []
    
    def size(self):
        return len(self.contracts)
    
    def push(self, number):
        self.contracts.append(number)
    
    def pop(self):
        return self.contracts.pop()
    
    def peek(self):
        if(self.size() == 0):
            raise EmptyStackException

        return self.contracts[-1]

    def empty(self):
        return True if self.size() == 0 else False
    
