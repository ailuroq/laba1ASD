import random
import numpy as np
import codecs


class Sorter:
    def randomFillFile(self, numberOfDigits):
        file = open("../files/input.txt", 'w')
        array = [random.randint(0, 20) for i in range(numberOfDigits)]
        for elements in array:
            file.write(str(elements) + " ")
        file.close()

    def readArrayFromFile(self, fileName):
        file = codecs.open(fileName, 'r')
        array = [line.split() for line in file]
        return array

    def insertionSort(self, array):
        counter = 0
        shift = 0
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
                counter += 1
                shift += 1
            array[j + 1] = key
            counter += 1
        counter += 1
        array.insert(len(array), counter)
        array.insert(len(array), shift)
        return array

    def shellSort(self, array):
        inc = len(array) // 2
        counter = 0
        shift = 0
        while inc:
            for i, el in enumerate(array):
                while i >= inc and array[i - inc] > el:
                    array[i] = array[i - inc]
                    i -= inc
                    counter += 1
                    shift += 1
                array[i] = el
                counter += 1
            inc = 1 if inc == 2 else int(inc * 5.0 / 11)
            counter += 1
        array.insert(len(array), counter)
        array.insert(len(array), shift)
        return array
