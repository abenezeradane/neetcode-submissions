class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = max(1, capacity)
        self.array = [0] * self.capacity
        self.contains = 0

    def get(self, i: int) -> int:
        if i > self.contains:
            raise Exception

        return self.array[i]

    def set(self, i: int, n: int) -> None:
        if i > self.contains:
            raise Exception

        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.contains == self.capacity:
            self.resize()

        self.array[self.contains] = n
        self.contains += 1

    def popback(self) -> int:
        self.contains -= 1
        return self.array[self.contains]

    def resize(self) -> None:
        self.array = self.array + ([0] * self.capacity)
        self.capacity *= 2

    def getSize(self) -> int:
        return self.contains
    
    def getCapacity(self) -> int:
        return self.capacity
