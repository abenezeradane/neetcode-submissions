from dataclasses import dataclass

class MyCircularQueue:
    @dataclass
    class Node:
        value: int
        next: Node
        prev: Node

    def __init__(self, k: int):
        self.queue = None
        self.capacity = k
        self.contained = 0

    def enQueue(self, value: int) -> bool:
        if self.contained == self.capacity:
            return False

        if self.queue == None:
            self.queue = self.Node(value, None, None)
            self.queue.next = self.queue
            self.queue.prev = self.queue
            self.contained = 1

            return True

        iterator = self.queue.next
        while iterator.next != self.queue:
            iterator = iterator.next

        iterator.next = self.Node(value, self.queue, iterator)
        self.queue.prev = iterator.next
        self.contained += 1
        
        return True

    def deQueue(self) -> bool:
        if self.queue == None:
            return False

        if self.contained == 1:
            self.queue = None
            self.contained = 0
            return True

        previous = self.queue.prev
        self.queue = self.queue.next
        previous.next = self.queue
        self.queue.prev = previous
        self.contained -= 1

        return True

    def Front(self) -> int:
        if self.queue == None:
            return -1

        return self.queue.value

    def Rear(self) -> int:
        if self.queue == None:
            return -1

        return self.queue.prev.value

    def isEmpty(self) -> bool:
        return self.contained == 0
        
    def isFull(self) -> bool:
        return self.contained == self.capacity
        
    def _tag(self, node) -> str:
        if node is None:
            return "None"
        return f"#{id(node) % 10000:04d}(v={node.value})"

    def dump(self, label: str = "") -> None:
        print(f"--- DUMP {label} | contained={self.contained} "
              f"capacity={self.capacity} head={self._tag(self.queue)}")

        if self.queue is None:
            print("    (empty)")
            print("--- END DUMP")
            return

        declared = {"value", "next", "prev"}
        seen = {}
        node = self.queue
        steps = 0
        limit = max(self.capacity, self.contained) + 5

        while True:
            if node is None:
                print(f"    [{steps}] -> None   (chain ends here)")
                break
            if id(node) in seen:
                print(f"    [{steps}] -> {self._tag(node)}   "
                      f"(cycle back to step {seen[id(node)]})")
                break
            if steps >= limit:
                print(f"    ... stopped after {limit} steps, no cycle found")
                break

            seen[id(node)] = steps
            stray = "".join(
                f"  {k}={self._tag(v) if isinstance(v, self.Node) else v!r}"
                for k, v in vars(node).items() if k not in declared
            )
            print(f"    [{steps}] {self._tag(node)}"
                  f"  next={self._tag(node.next)}"
                  f"  prev={self._tag(node.prev)}{stray}")

            node = node.next
            steps += 1

        print("--- END DUMP")

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()