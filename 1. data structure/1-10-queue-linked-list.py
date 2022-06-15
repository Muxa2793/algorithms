class LinkedList():

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class MyQueueLinkedList():
    def __init__(self):
        self.tail = None
        self.head = None
        self.size_queue = 0

    def get(self):
        if self.size_queue == 0:
            return 'error'

        x = self.head.value

        if self.size_queue == 1:
            self.head = LinkedList()
            self.tail = LinkedList()
        elif self.size_queue == 2:
            self.head = self.tail
        else:
            self.head = self.tail.next.next
            self.tail.next = self.head
        self.size_queue -= 1
        return x

    def put(self, item):
        if self.size_queue == 0:
            self.head = LinkedList(item)
            self.tail = self.head
        else:
            self.tail.next = LinkedList(item)
            self.tail.next.next = self.head
            self.tail = self.tail.next

        self.size_queue += 1

    def size(self):
        print(self.size_queue)

    def __str__(self):
        return str(self.head)

n = int(input())

queue = MyQueueLinkedList()


for i in range(0, n):
    commands = input().split()

    if commands[0] == 'put':
        queue.put(commands[1])
    elif commands[0] == 'get':
        print(queue.get())
    elif commands[0] == 'size':
        queue.size()
