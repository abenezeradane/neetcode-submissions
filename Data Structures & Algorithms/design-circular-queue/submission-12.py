class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.queue = [None] * k
        self.head, self.tail, self.contained = 0, 0, 0


    def enQueue(self, value: int) -> bool:
        if self.contained == self.capacity:
            return False

        if self.queue[self.tail] != None:
            while self.queue[self.tail] != None:
                self.tail = (self.tail + 1) % self.capacity

        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.contained += 1
        
        return True


    def deQueue(self) -> bool:
        if self.contained == 0:
            return False
        
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.contained -= 1

        return True


    def Front(self) -> int:
        if self.contained == 0:
            return -1
        
        return self.queue[self.head]


    def Rear(self) -> int:
        if self.contained == 0:
            return -1
        
        rear = (self.tail + (self.capacity - 1)) % self.capacity
        return self.queue[rear]


    def isEmpty(self) -> bool:
        return self.contained == 0


    def isFull(self) -> bool:
        return self.contained == self.capacity        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()