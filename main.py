class Stack:
    def __init__(self) -> None:
        self.__li = []
    
    # помещение строки в стек
    def push(self, value):
        self.__li.append(value)

    # выталкивание строки из стека
    def pop(self):
        if len(self.__li):
            return self.__li.pop()

    # подсчет количества строк в стеке
    def counting(self):
        return print(len(self.__li))

    # проверка пустой ли стек
    def isEmplyStack(self):
        if self.__li == []:
            print("True")
        else:
            print("False")

    # проверка полный ли стек
    def isFullStack(self):
        pass

    # очистка стека
    def cleaning(self):
        pass

    # ■ получение значения без выталкивания верхней строки из стека. 
    def printStack(self):
        print(self.__li)

stack = Stack()
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.printStack()
stack.counting()
stack.isEmplyStack()