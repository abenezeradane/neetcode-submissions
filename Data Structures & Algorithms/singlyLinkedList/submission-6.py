from dataclasses import dataclass

class LinkedList:
    @dataclass
    class Node:
        value: int
        next: Node | None = None
    
    def __init__(self):
        self.length: int = 0
        self.root: self.Node = None
    
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1

        node: self.Node = self.root
        for _ in range(index):
            node = node.next
        
        return node.value

    def insertHead(self, val: int) -> None:
        self.root = self.Node(val, self.root)
        self.length += 1

    def insertTail(self, val: int) -> None:
        if self.root == None:
            self.root = self.Node(val)
        else:
            node: self.Node = self.root
            for _ in range(self.length - 1):
                node = node.next

            node.next = self.Node(val)

        self.length += 1

    def remove(self, index: int) -> bool:
        if index >= self.length:
            return False

        if index == 0:
            self.root = self.root.next
        else:
            node: self.Node = self.root
            for _ in range(index - 1):
                node = node.next

            node.next = node.next.next

        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        values: List[int] = list()

        node: self.Node = self.root
        for _ in range(self.length):
            values.append(node.value)
            node = node.next

        return values
