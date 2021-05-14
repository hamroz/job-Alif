
# Author: Hamroz Gavharov
# Date: May 15 2021 1:00 AM


# Classes
class Calulator():

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            pass
        
        
class FileHandler():
    def read_file(self):
        input_file = open(file_name, "r")
        input_file_item = [[int(j) for j in i.split(" ")]
        for i in input_file.read().split('\n')]
        return input_file_item

    def save(self, result):
        if result < 0:
            file.negative(str(result))
        else:
            file.positive(str(result))

    def negative(self, result):
        try:
            f = open("negative.txt", "x")
            f.write(result)
            f.write("\n")
        except Exception:
            f = open("negative.txt", "a")
            f.write(result)
            f.write("\n")

    def positive(self, result):
        try:
            f = open("positive.txt", "x")
            f.write(result)
            f.write("\n")
        except Exception:
            f = open("positive.txt", "a")
            f.write(result)
            f.write("\n")



# Functions            
def Calculate():

    if operator == '+':
        for i in file.read_file():
            result = calc.add(i[0], i[1])
            file.save(result)

    if operator == '-':
        for i in file.read_file():
            result = calc.subtract(i[0], i[1])
            file.save(result)

    if operator == '*':
        for i in file.read_file():
            result = calc.multiply(i[0], i[1])
            file.save(result)

    if operator == '/':
        for i in file.read_file():
            if i[1] != 0:
                result = calc.divide(i[0], i[1])
                file.save(result)
            else:
                print("Can not be divided by zero")


# Instances
file = FileHandler()
calc = Calulator()
file_name = input("file name: ")
operator = input("choose operator (+, -, /, *): ")

Calculate()