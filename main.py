class Stack:
    def __init__(self,n) -> None:
        self.__li = []
        self.n = n
    
    # помещение строки в стек
    def push(self, value):
        if len(self.__li) < self.n:
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
        if self.__li == self.n:
            print("True")
        else:
            print("False")

    # очистка стека
    def cleaning(self):
        return self.__li.clear()

    # ■ получение значения без выталкивания верхней строки из стека. 
    def printStack(self):
        print(self.__li)

stack = Stack(3)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.printStack()
stack.counting()
stack.isEmplyStack()
stack.isFullStack()
# stack.cleaning()
# stack.printStack()