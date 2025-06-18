class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            return "stack is empty"
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self._items[-1]

    def size(self):
        return len(self._items)

    def display(self):
        return self._items

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print("Stack:", s.display())
    print("Popping item:", s.pop())
    print("Stack after pop:", s.display())
    print("Stack size:", s.size())
    print("Top item:", s.peek())
