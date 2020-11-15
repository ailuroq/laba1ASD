import codecs
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
from pip._vendor.msgpack.fallback import xrange


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 773)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.insert = QtWidgets.QWidget()
        self.insert.setObjectName("insert")
        self.textEdit_2 = QtWidgets.QTextEdit(self.insert)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 620, 519, 91))
        self.textEdit_2.setObjectName("textEdit_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.insert)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 330, 521, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setInputMask('A')
        self.tableWidget = QtWidgets.QTableWidget(self.insert)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(1, 39, 519, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.insert)
        self.pushButton.setGeometry(QtCore.QRect(1, 1, 521, 31))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.insert)
        self.textEdit.setGeometry(QtCore.QRect(0, 230, 519, 91))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.insert)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 360, 251, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.insert)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 400, 519, 211))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.pushButton_9 = QtWidgets.QPushButton(self.insert)
        self.pushButton_9.setGeometry(QtCore.QRect(270, 360, 251, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.tabWidget.addTab(self.insert, "")
        self.shell = QtWidgets.QWidget()
        self.shell.setObjectName("shell")
        self.lineEdit = QtWidgets.QLineEdit(self.shell)
        self.lineEdit.setGeometry(QtCore.QRect(0, 330, 521, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setInputMask('A')
        self.tableWidget_4 = QtWidgets.QTableWidget(self.shell)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 400, 519, 211))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.pushButton_2 = QtWidgets.QPushButton(self.shell)
        self.pushButton_2.setGeometry(QtCore.QRect(1, 1, 521, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.shell)
        self.tableWidget_3.setGeometry(QtCore.QRect(1, 39, 519, 181))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.textEdit_4 = QtWidgets.QTextEdit(self.shell)
        self.textEdit_4.setGeometry(QtCore.QRect(0, 620, 519, 91))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_3 = QtWidgets.QTextEdit(self.shell)
        self.textEdit_3.setGeometry(QtCore.QRect(0, 229, 519, 91))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.shell)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 360, 261, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_10 = QtWidgets.QPushButton(self.shell)
        self.pushButton_10.setGeometry(QtCore.QRect(270, 360, 251, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.tabWidget.addTab(self.shell, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Выбрать файл"))
        self.pushButton_3.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_9.setText(_translate("MainWindow", "Сортировать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.insert), _translate("MainWindow", "Insert Sort"))
        self.pushButton_2.setText(_translate("MainWindow", "Выбрать файл"))
        self.pushButton_7.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_10.setText(_translate("MainWindow", "Сортировать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shell), _translate("MainWindow", "Shell Sort"))
        self.pushButton.clicked.connect(self.file_open)
        self.pushButton_2.clicked.connect(self.file_open2)
        self.pushButton_3.clicked.connect(self.add1)
        self.pushButton_9.clicked.connect(self.sort1)
        self.pushButton_7.clicked.connect(self.add2)
        self.pushButton_10.clicked.connect(self.sort2)

    def file_open(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        matrix = self.readArrayFromFile(path)
        rows = len(matrix)
        columns = len(matrix[0])
        header = self.tableWidget.horizontalHeader()
        self.tableWidget.setRowCount(rows)
        self.tableWidget.setColumnCount(columns)
        unsortedArray = []
        for i in range(0, rows):
            unsortedArray.append(matrix[i][0])
        start_time = time.time()
        sortedArray = self.insertionSort(unsortedArray, self.textEdit)
        end_time = time.time() - start_time
        shifts = sortedArray[len(sortedArray) - 1]
        sortedArray = sortedArray[:-1]
        steps = sortedArray[len(sortedArray) - 1]
        sortedArray = sortedArray[:-1]

        for i in range(0, rows):
            for j in range(0, columns):
                header.setSectionResizeMode(j, QtWidgets.QHeaderView.Stretch)
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(matrix[i][j])))
        self.tableWidget.sortItems(0, Qt.AscendingOrder)
        self.textEdit.append(str(sortedArray))
        self.textEdit.append(str("Количество шагов: "))
        self.textEdit.append(str(steps))
        self.textEdit.append(str("Количество перестановок: "))
        self.textEdit.append(str(shifts))
        self.textEdit.append(str("Затраченное время"))
        self.textEdit.append(str("--- %s секунд ---" % (end_time)))

        return matrix

    def file_open2(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        matrix = self.readArrayFromFile(path)
        rows = len(matrix)
        columns = len(matrix[0])
        header = self.tableWidget_3.horizontalHeader()
        self.tableWidget_3.setRowCount(rows)
        self.tableWidget_3.setColumnCount(columns)
        unsortedArray = []
        for i in range(0, rows):
            unsortedArray.append(matrix[i][0])
        start_time = time.time()
        sortedArray = self.shellSort(unsortedArray, self.textEdit_3)
        end_time = time.time() - start_time
        shifts = sortedArray[len(sortedArray) - 1]
        sortedArray = sortedArray[:-1]
        steps = sortedArray[len(sortedArray) - 1]
        sortedArray = sortedArray[:-1]
        for i in range(0, rows):
            for j in range(0, columns):
                header.setSectionResizeMode(j, QtWidgets.QHeaderView.Stretch)
                self.tableWidget_3.setItem(i, j, QTableWidgetItem(str(matrix[i][j])))
        self.tableWidget_3.sortItems(0, Qt.AscendingOrder)
        self.textEdit_3.append(str(sortedArray))
        self.textEdit_3.append(str("Количество шагов: "))
        self.textEdit_3.append(str(steps))
        self.textEdit_3.append(str("Количество перестановок: "))
        self.textEdit_3.append(str(shifts))
        self.textEdit_3.append(str("Затраченное время"))
        self.textEdit_3.append(str("--- %s секунд ---" % (end_time)))

    def add1(self):
        text = [self.lineEdit_2.text().split()]
        columns = len(text[0])
        counter = self.tableWidget_2.rowCount()
        self.tableWidget_2.setRowCount(counter + 1)
        self.tableWidget_2.setColumnCount(columns)
        for i in range(0, columns):
            self.tableWidget_2.setItem(counter, i, QTableWidgetItem(text[0][i]))

    def add2(self):
        text = [self.lineEdit.text().split()]
        columns = len(text[0])
        counter = self.tableWidget_4.rowCount()
        self.tableWidget_4.setRowCount(counter + 1)
        self.tableWidget_4.setColumnCount(columns)
        for i in range(0, columns):
            self.tableWidget_4.setItem(counter, i, QTableWidgetItem(text[0][i]))

    def sort1(self):
        rows = self.tableWidget_2.rowCount()
        unsorted = []
        for i in range(0, rows):
            unsorted.append(self.tableWidget_2.item(i, 0).text())
        start_time = time.time()
        sorted = self.insertionSort(unsorted, self.textEdit_2)
        end_time = time.time() - start_time
        shifts = sorted[len(sorted) - 1]
        sorted = sorted[:-1]
        steps = sorted[len(sorted) - 1]
        sorted = sorted[:-1]
        self.tableWidget_2.sortItems(0, Qt.AscendingOrder)
        self.textEdit_2.append(str("Отсортированный массив:"))
        self.textEdit_2.append(str(sorted))
        self.textEdit_2.append(str("Количество шагов:"))
        self.textEdit_2.append(str(steps))
        self.textEdit_2.append(str("Количество перестановок"))
        self.textEdit_2.append(str(shifts))
        self.textEdit_2.append(str("Затраченное время"))
        self.textEdit_2.append(str("--- %s секунд ---" % (end_time)))

    def sort2(self):
        rows = self.tableWidget_4.rowCount()
        unsorted = []
        for i in range(0, rows):
            unsorted.append(self.tableWidget_4.item(i, 0).text())
        start_time = time.time()
        sorted = self.shellSort(unsorted, self.textEdit_4)
        end_time = time.time() - start_time
        shifts = sorted[len(sorted) - 1]
        sorted = sorted[:-1]
        steps = sorted[len(sorted) - 1]
        sorted = sorted[:-1]
        self.tableWidget_4.sortItems(0, Qt.AscendingOrder)
        self.textEdit_4.append(str("Отсортированный массив:"))
        self.textEdit_4.append(str(sorted))
        self.textEdit_4.append(str("Количество шагов:"))
        self.textEdit_4.append(str(steps))
        self.textEdit_4.append(str("Количество перестановок"))
        self.textEdit_4.append(str(shifts))
        self.textEdit_4.append(str("Затраченное время"))
        self.textEdit_4.append(str("--- %s секунд ---" % (end_time)))

    def readArrayFromFile(self, fileName):
        file = codecs.open(fileName, 'r')
        array = [line.split() for line in file]
        return array

    def insertionSort(self, array, model):
        counter = 0
        shift = 0
        unsortedArray = array
        model.append(str("Изначальный массив:"))
        model.append(str(unsortedArray))
        model.append(str("Сортировка:"))

        for i in xrange(1, len(array)):
            j = i - 1
            value = array.pop(i)
            model.append(str(array))
            shift += 1
            while (j >= 0) and (array[j] > value):
                j -= 1
                counter += 1
            array.insert(j + 1, value)
            counter += 1
        array.insert(len(array), counter)
        array.insert(len(array), shift)
        return array

    def shellSort(self, array, model):
        inc = len(array) // 2
        counter = 0
        shift = 0
        unsortedArray = array
        model.append(str("Изначальный массив:"))
        model.append(str(unsortedArray))
        model.append(str("Сортировка:"))
        while inc:
            for i, el in enumerate(array):
                while i >= inc and array[i - inc] > el:
                    array[i] = array[i - inc]
                    i -= inc
                    counter += 1
                array[i] = el
                counter += 1
                model.append(str(array))
                shift += 1
            inc = 1 if inc == 2 else int(inc * 5.0 / 11)
            counter += 1
        array.insert(len(array), counter)
        array.insert(len(array), shift)
        return array


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
