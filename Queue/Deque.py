class Deque(object):
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def add_front(self, item):
        self._items.append(item)

    def add_back(self, item):
        self._items.insert(0, item)

    def remove_front(self):
        return self._items.pop()

    def remove_back(self):
        return self._items.pop(0)

    def size(self):
        return len(self._items)

    def display(self):
        return self._items

if __name__ == "__main__":
    d = Deque()
    d.add_front(1)
    d.add_back(2)
    d.add_back(3)
    print("Deque:", d.display())
    print("Removing front item:", d.remove_front())
    print("Deque after remove_front:", d.display())
    print("Deque size:", d.size())
