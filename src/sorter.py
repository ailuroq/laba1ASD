import random


class Sorter():
    def randomFillFile(self, numberOfDigits):
        file = open("../files/input.txt", 'w')
        array = [random.randint(0, 20) for i in range(numberOfDigits)]
        for elements in array:
            file.write(str(elements) + " ")
        file.close()

    def readArrayFromFile(self, fileName):
        file = open(fileName, 'r')
        array = [int(x) for x in file.read().split()]
        return array

    def insertionSort(self, array):
        counter = 0
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
                counter += 1
            array[j + 1] = key
            counter += 1
        array.insert(len(array), counter)
        return array

    def shellSort(self, array):
        inc = len(array) // 2
        counter = 0
        while inc:
            for i, el in enumerate(array):
                while i >= inc and array[i - inc] > el:
                    array[i] = array[i - inc]
                    i -= inc
                    counter += 1
                array[i] = el
                counter += 1
            inc = 1 if inc == 2 else int(inc * 5.0 / 11)
            counter += 1
        array.insert(len(array), counter)
        return array
