"""ID: 68885121"""


class DequeError(Exception):
    def __str__(self):
        return 'error'


class Deque:
    def __init__(self, length):
        self.dec = [None] * length
        self.max_n = length
        self.head = 0
        self.tail = 0
        self.dec_size = 0

    def is_full(self):
        return self.dec_size == self.max_n

    def is_empty(self):
        return self.dec_size == 0

    def push_back(self, value):
        if self.is_full():
            raise DequeError

        self.dec[self.tail] = value
        self.tail = (self.tail + 1) % self.max_n
        self.dec_size += 1

    def push_front(self, value):
        if self.is_full():
            raise DequeError

        new_head = self.head - 1

        self.dec[new_head] = value
        self.head = new_head % self.max_n
        self.dec_size += 1

    def pop_front(self):
        if self.is_empty():
            raise DequeError

        item = self.dec[self.head]
        self.dec[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.dec_size -= 1
        return item

    def pop_back(self):
        if self.is_empty():
            raise DequeError

        new_tail = self.tail - 1

        item = self.dec[new_tail]
        self.dec[new_tail] = None
        self.tail = new_tail % self.max_n
        self.dec_size -= 1
        return item

    def __str__(self):
        return f'\nDEC: {self.dec}\nHEAD: {self.head}\nTAIL: {self.tail}\n'


if __name__ == "__main__":

    n = int(input())
    m = int(input())

    deque = Deque(m)

    for i in range(0, n):

        method, *args = input().split()

        if hasattr(deque, method):
            try:
                result = getattr(deque, method)(*list(map(int, args)))
                if result is not None:
                    print(result)
            except DequeError as err:
                print(err)
