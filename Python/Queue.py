class Queue:
    def __init__(self, size=10):
        self.size = size
        self.data = [0 for i in range(self.size)]
        self.front_pointer = 0
        self.back_pointer = 0
       
    def enqueue(self, value):
        if  -1 <= self.back_pointer - self.front_pointer < 0 :
            self.data[self.back_pointer] = value
        elif self.back_pointer < self.size:
            self.data[self.back_pointer] = value
            self.back_pointer += 1
        elif self.back_pointer - self.front_pointer < self.size \
             and self.back_pointer >= self.size:
            self.back_pointer %= self.size
            self.data[self.back_pointer] = value
       
    def dequeue(self):
        if self.back_pointer - self.front_pointer < 0:
            if self.back_pointer > 0:
                self.back_pointer -= 1
            else:
                self.back_pointer = self.size - 1
        elif self.front_pointer < self.size \
           and self.front_pointer < self.back_pointer:
            self.front_pointer += 1
        # if empty queue shift back to start
        if self.back_pointer - self.front_pointer == 0:
            self.front_pointer = 0
            self.back_pointer = 0
           
    def __add__(self, value):
        self.enqueue(value)
        return self

    def __str__(self):
        str_form = ''
        for c in range(self.size):
            extra = ''
            if self.back_pointer == c:
                extra += "[  BP] "
            if self.front_pointer == c:
                extra += "[  FP] "
            if not extra:
                extra += "[%4d] " % c
           
            extra += str(self.data[c])
            extra += '\n'
            str_form += extra

        if self.back_pointer == self.front_pointer == self.size:
            str_form += "[  FP] [  BP] [%4d] NULL\n" % self.size  
        elif self.back_pointer == self.size:
            str_form += "[  BP] [%4d] NULL\n" % self.size
        elif self.front_pointer == self.size:
            str_form += "[  FP] [%4d] NULL\n" % self.size
           
        return str_form

def main():
  # General testing of functions
  q = Queue()
  print(q)
  q.enqueue(0)
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)
  q.enqueue(4)
  q.enqueue(5)
  q.enqueue(6)
  print(q)
  q.dequeue()
  q.dequeue()
  q.dequeue()
  print(q)
  q.enqueue(7)
  q.enqueue(8)
  q.enqueue(9)
  q.enqueue(10)
  q.enqueue(11)
  q.enqueue(12)
  q.enqueue(13)
  q.enqueue(14)
  q.dequeue()
  q.dequeue()
  q.dequeue()
  q.dequeue()
  q.dequeue()
  q.dequeue()
  q.dequeue()
  q.dequeue()
  q.dequeue()

  print(f"Normal: FP {q.front_pointer}; BP {q.back_pointer}; diff {q.back_pointer - q.front_pointer}")
  print(q)
  q.enqueue(69696969)
  print(q)
  
