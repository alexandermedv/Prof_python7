

class Stack():
    """Класс, реализующий стек"""

    def __init__(self):
        """Инициализация класса"""
        self.stek = ''

    def isEmpty(self):
        """Проверка, пустой ли стек"""

        if self.stek == '':
            return True
        else:
            return False

    def push(self, element):
        """Добавление элемента в стек"""

        self.stek += element

    def pop(self):
        """Удаление последнего элемента из стека"""

        self.stek = self.stek[:-1]

    def peek(self):
        """Последний элемент стека"""

        if self.stek:
            return self.stek[-1]
        else:
            return None

    def size(self):
        """Количество элементов в стеке"""

        return len(self.stek)


if __name__ == '__main__':

    pairs = {'{': '}', '(': ')', '[': ']'}
    string = input('Введите строку\n')
    stack1 = Stack()
    stack2 = Stack()

    for symbol in string:
        stack1.push(symbol)

    while stack1.size() > 0:
        if stack1.peek() in pairs and pairs[stack1.peek()] == stack2.peek():
            stack1.pop()
            stack2.pop()
        else:
            stack2.push(stack1.peek())
            stack1.pop()

    if stack2.size() == 0:
        print('Сбалансированно')
    else:
        print('Несбалансированно')
