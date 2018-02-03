# -*- coding: utf-8 -*-

import datetime
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(803, 518)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 771, 475))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.dateExit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.dateExit.setDateTime(QtCore.QDateTime(QtCore.QDate(2017, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateExit.setObjectName("dateExit")
        self.gridLayout.addWidget(self.dateExit, 0, 3, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2017, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 0, 9, 1, 1, QtCore.Qt.AlignLeft)
        self.dateEntry = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.dateEntry.setDateTime(QtCore.QDateTime(QtCore.QDate(2017, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEntry.setObjectName("dateEntry")
        self.gridLayout.addWidget(self.dateEntry, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.addStay = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.addStay.setObjectName("addStay")
        self.gridLayout.addWidget(self.addStay, 0, 4, 1, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 5, 1, 1)
        self.calculate = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.calculate.setObjectName("calculate")
        self.gridLayout.addWidget(self.calculate, 2, 0, 1, 5)
        self.removeStay = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.removeStay.setObjectName("removeStay")
        self.gridLayout.addWidget(self.removeStay, 1, 9, 1, 1, QtCore.Qt.AlignTop)
        self.listWidget_2 = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout.addWidget(self.listWidget_2, 3, 0, 1, 5)
        self.listWidget = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 9)
        self.listWidget_3 = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listWidget_3.setObjectName("listWidget_3")
        self.gridLayout.addWidget(self.listWidget_3, 3, 6, 1, 4)
        self.forecastEntry = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.forecastEntry.setObjectName("forecastEntry")
        self.gridLayout.addWidget(self.forecastEntry, 2, 6, 1, 4)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 5, 1, 4, QtCore.Qt.AlignRight)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.dateEntry, self.dateExit)
        MainWindow.setTabOrder(self.dateExit, self.addStay)
        MainWindow.setTabOrder(self.addStay, self.dateEdit)
        MainWindow.setTabOrder(self.dateEdit, self.listWidget)
        MainWindow.setTabOrder(self.listWidget, self.removeStay)
        MainWindow.setTabOrder(self.removeStay, self.calculate)
        MainWindow.setTabOrder(self.calculate, self.listWidget_2)
        MainWindow.setTabOrder(self.listWidget_2, self.forecastEntry)
        MainWindow.setTabOrder(self.forecastEntry, self.listWidget_3)

        self.dates = []
        self.dateEntry.setFocus()
        self.addStay.clicked.connect(self.printToList)
        self.removeStay.clicked.connect(self.removeStayAction)
        self.calculate.clicked.connect(self.calculateStay)
        self.forecastEntry.clicked.connect(self.nextPossibleEntry)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Schengen stay calculator"))
        self.label_2.setText(_translate("MainWindow", "Exit:"))
        self.label.setText(_translate("MainWindow", "Entry:"))
        self.addStay.setText(_translate("MainWindow", "Add stay"))
        self.calculate.setText(_translate("MainWindow", "Calculate duration of stay since first entry"))
        self.removeStay.setText(_translate("MainWindow", "Remove stay"))
        self.forecastEntry.setText(_translate("MainWindow", "Date of the next possible entry"))
        self.label_3.setText(_translate("MainWindow", "Visa valid until:"))


    def getDates(self):

        self.dateOfEntry = self.dateEntry.date()
        self.dateIn = self.dateOfEntry.toString()
        self.dateOfEntryPy = self.dateOfEntry.toPyDate()

        self.dateOfExit = self.dateExit.date()  # for doing the if below

        self.dateOut = self.dateOfExit.toString()
        self.dateOfExitPy = self.dateOfExit.toPyDate()

        if self.dateOfExit < self.dateOfEntry:
            # Error box for condition Entry > Exit
            msgbox = QtWidgets.QMessageBox()
            msgbox.setText('Date of exit must be after date of entry.')
            msgbox.exec_()
            return False  # To be picked up by def printToList
        elif self.dateOfExitPy > datetime.date.today():
            msgbox = QtWidgets.QMessageBox()
            msgbox.setText('Date of exit cannot be later than today.')
            msgbox.exec_()
        else:
            days_overlapping = 0
            for stay in self.dates:
                range_of_stay = pd.date_range(start=stay[0], end=stay[1])
                range_new_item = pd.date_range(start=self.dateOfEntryPy, end=self.dateOfExitPy)
                for day in range_new_item:
                    if day in range_of_stay:
                        days_overlapping += 1
            if days_overlapping >= 1:
                msgbox = QtWidgets.QMessageBox()
                msgbox.setText('Durations of stay cannot overlap.')
                msgbox.exec_()
                return False
        # Add dates to the list
        self.dates.append([self.dateOfEntryPy, self.dateOfExitPy])
        self.dates.sort()
        return True

    def printToList(self):
        if self.getDates() is True:
            self.listWidget.addItem('Entry on {} and exit on {}.\t\t({} -> {})'
                                    .format(self.dateIn, self.dateOut, self.dateOfEntryPy, self.dateOfExitPy))
            self.listWidget.sortItems()

    def removeStayAction(self):
        # Error handling for when there are no items on the list
        try:
            self.listWidget.takeItem(self.listWidget.currentRow())
            self.dates.remove(self.dates[self.listWidget.currentRow()])
        except IndexError:
            pass

    #  Create ranges out of the entry and exit dates

    def createRange(self, list):
        rangeofdates = pd.date_range(start=list[0], end=list[1])
        return rangeofdates

    def calculateStay(self):
        self.total_days = 0
        self.total_days_ill = 0
        try:
            range_allowed = pd.date_range(start=self.dates[0][0], end=self.dates[0][0]+datetime.timedelta(180))
            for stay in self.dates:
                rangeofdates = self.createRange(stay)  # create a range from dateOfEntry and dateOfExit
                for item in rangeofdates:
                    if item in range_allowed:
                        self.total_days += 1
                    else:
                        self.total_days_ill += 1
                    total_of_days = self.total_days + self.total_days_ill
                if (total_of_days) > 90:
                    self.listWidget_2.clear()
                    self.listWidget_2.addItem('You stayed {} days in the Schengen area out of 90 days possible, \n'
                                              'since your first entry.\n\nATTENTION YOU EXCEEDED THE LEGAL PERIOD '
                                              'OF STAY in:\n{} days.'.format(total_of_days, total_of_days - 90))
                else:
                    self.listWidget_2.clear()
                    self.listWidget_2.addItem('You stayed {} days in the Schengen area out of 90 days possible, \n'
                                              'since your first entry.\n\nYou are allowed to stay {} days until'
                                              ' {}.'.format(total_of_days, 90-total_of_days,
                                                            self.dates[0][0]+datetime.timedelta(180)))
        except:
            self.listWidget_2.clear()


    def nextPossibleEntry(self):
        self.calculateStay()
        self.listWidget_3.clear()
        number_loops = 0
        for stay in self.dates:
            number_loops += 1
            range_forecast = pd.date_range(start=stay[1], end=stay[1] + datetime.timedelta(180))
            try:
                range_next = self.createRange(self.dates[number_loops])
                total_days_forecast = 0
                for item in range_forecast:
                    if item in range_next:
                        total_days_forecast += 1
                if total_days_forecast > 90:
                    pass
                else:
                    self.listWidget_3.addItem('From the {} you have a total \nof {} days of stay allowed\n'
                                              .format(str(stay[1]+datetime.timedelta(180)), 91-total_days_forecast))
            except IndexError:
                pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

