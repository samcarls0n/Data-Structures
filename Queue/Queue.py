class Queue(object):
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def display(self):
        return self._items

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Queue:", q.display())
    print("Dequeing item:", q.dequeue())
    print("Queue after dequeue:", q.display())
    print("Queue size:", q.size())
