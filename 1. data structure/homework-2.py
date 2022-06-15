"""ID: 68889825"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError('pop from empty stack')


def calculate(expression):

    stack = Stack()

    operations = {
        '/': lambda x, y: x // y,
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
    }

    for item in expression:
        if item[-1].isdigit():
            stack.push(int(item))
        else:
            operand_1 = stack.pop()
            operand_2 = stack.pop()
            result = operations[item](operand_2, operand_1)
            stack.push(result)

    return stack.pop()


if __name__ == "__main__":

    expression = input().split()
    result = calculate(expression)
    print(result)
