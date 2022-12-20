class Stack:
    def __init__(self, n) -> None:
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
        return print(f"Количество строк в стеке - {len(self.__li)}")

    # проверка пустой ли стек
    def isEmplyStack(self):
        if self.__li == []:
            print("Стек пустой")
        else:
            print(f"Стек не пустой, имеет {len(self.__li)} элемента")

    # проверка полный ли стек
    def isFullStack(self):
        if self.__li == self.n:
            print("Стек полный")
        else:
            print("False")

    # очистка стека
    def cleaning(self):
        return self.__li.clear()

    # получение значения без выталкивания верхней строки из стека. 
    def printStack(self):
        print(self.__li)

stack = Stack(4)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(5)
# stack.printStack()
# stack.pop()
# stack.printStack()
# stack.counting()
# stack.isEmplyStack()
# stack.isFullStack()
# stack.cleaning()
# stack.printStack()

while True:
    answer1 = input("Если желаете воспользоваться приложением работы со стеком нажмите 'Y', если нет, то - 'N': \n")
    if answer1.lower() == "n":
        break
    elif answer1.lower() == "y":
        answer2 = input("Веберите следующие действия: 1 - помещение строки в стек; 2 - выталкивание строки из стека; 3 - подсчет количества строк в стеке; 4 - проверка пустой ли стек; 5 - проверка полный ли стек; 6 - очистка стека: \n")
        if answer2 == "1":
            stack.push(input("Введите значение: "))
            stack.printStack()
        if answer2 == "2":
            stack.pop()
            stack.printStack()
        elif answer2 == "3":
            stack.counting()
        elif answer2 == "4":
            stack.isEmplyStack()
        elif answer2 == "5":
            stack.isFullStack()
        elif answer2 == "6":
            stack.cleaning()
            print("Стек очищен")