from timeit import timeit

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QTextEdit, QFileDialog, QTableWidgetItem, QHeaderView
import numpy as np
from src.sorter import Sorter
import re


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
        self.pushButton_3.setGeometry(QtCore.QRect(0, 360, 521, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.insert)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 400, 519, 211))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tabWidget.addTab(self.insert, "")
        self.shell = QtWidgets.QWidget()
        self.shell.setObjectName("shell")
        self.lineEdit = QtWidgets.QLineEdit(self.shell)
        self.lineEdit.setGeometry(QtCore.QRect(0, 330, 521, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_4 = QtWidgets.QPushButton(self.shell)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 360, 521, 31))
        self.pushButton_4.setObjectName("pushButton_4")
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.insert), _translate("MainWindow", "Insert Sort"))
        self.pushButton_4.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_2.setText(_translate("MainWindow", "Выбрать файл"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shell), _translate("MainWindow", "Shell Sort"))
        self.pushButton.clicked.connect(self.file_open)
        self.pushButton_2.clicked.connect(self.file_open2)

    def file_open(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        sorter = Sorter()
        matrix = sorter.readArrayFromFile(path)
        rows = len(matrix)
        columns = len(matrix[0])
        print(matrix)
        print(rows, columns)
        header = self.tableWidget.horizontalHeader()
        self.tableWidget.setRowCount(rows)
        self.tableWidget.setColumnCount(columns)
        unsortedArray = []
        for i in range(0, rows):
            unsortedArray.append(matrix[i][0])
        print(unsortedArray)
        sortedArray = sorter.insertionSort(unsortedArray)
        shifts = sortedArray[len(sortedArray) - 1]
        sortedArray = sortedArray[:-1]
        steps = sortedArray[len(sortedArray) - 1]
        sortedArray = sortedArray[:-1]

        print(sortedArray)
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

        return matrix

    def file_open2(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        sorter = Sorter()
        matrix = sorter.readArrayFromFile(path)
        rows = len(matrix)
        columns = len(matrix[0])
        print(matrix)
        print(rows, columns)
        header = self.tableWidget_3.horizontalHeader()
        self.tableWidget_3.setRowCount(rows)
        self.tableWidget_3.setColumnCount(columns)
        unsortedArray = []
        for i in range(0, rows):
            unsortedArray.append(matrix[i][0])
        print(unsortedArray)
        sortedArray = sorter.shellSort(unsortedArray)
        shifts = sortedArray[len(sortedArray) - 1]
        sortedArray = sortedArray[:-1]
        steps = sortedArray[len(sortedArray) - 1]
        sortedArray = sortedArray[:-1]

        print(sortedArray)
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

    def newWindow(self):
        self.winTable = Ui_MainWindow()
        self.winTable.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
