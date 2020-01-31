class Stack:
    def __init__(self, size=10):
        self.size = size
        self.data = [0 for i in range(self.size)]
        self.stack_pointer = 0

    def push(self, value):
        if self.stack_pointer < self.size:
            self.data[self.stack_pointer] = value
            self.stack_pointer += 1
            return True
        return False
       
    def pop(self):
        if self.stack_pointer > 0:
            self.stack_pointer -= 1
            return True
        return False

    def __add__(self, value):
        self.push(value)
        return self

    def __str__(self):
        str_form = ''
        for c in range(self.size):
            if self.stack_pointer == c:
                str_form += "[  SP] "
            else:
                str_form += "[%4d] " % c
            str_form += str(self.data[c])
            str_form += '\n'

        if self.stack_pointer == self.size:
            str_form += "[  SP] [%4d] NULL\n" % self.size
       
        return str_form

def main():
  # General testing of functions
  s = Stack()
  s += 20
  s += 2
  s += 10
  s += 22
  s += 25
  s += 28
  s += 233
  s += 211
  s += 233
  s += 211
  s += 233
  s += 211
  print(s)
  s.pop()
  s.pop()
  s.pop()
