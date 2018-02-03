# -*- coding: utf-8 -*-

import datetime
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.dateExit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateExit.setDateTime(QtCore.QDateTime(QtCore.QDate(2017, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateExit.setObjectName("dateExit")
        self.gridLayout.addWidget(self.dateExit, 0, 5, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 6, 8, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)
        self.resetAllEntries = QtWidgets.QPushButton(self.centralwidget)
        self.resetAllEntries.setObjectName("resetAllEntries")
        self.gridLayout.addWidget(self.resetAllEntries, 0, 11, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 11)
        self.removeStay = QtWidgets.QPushButton(self.centralwidget)
        self.removeStay.setObjectName("removeStay")
        self.gridLayout.addWidget(self.removeStay, 2, 11, 1, 1, QtCore.Qt.AlignTop)
        self.calculate = QtWidgets.QPushButton(self.centralwidget)
        self.calculate.setObjectName("calculate")
        self.gridLayout.addWidget(self.calculate, 5, 0, 1, 8)
        self.addStay = QtWidgets.QPushButton(self.centralwidget)
        self.addStay.setObjectName("addStay")
        self.gridLayout.addWidget(self.addStay, 0, 7, 1, 1)
        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_3.setObjectName("listWidget_3")
        self.gridLayout.addWidget(self.listWidget_3, 6, 9, 1, 3)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout.addWidget(self.listWidget_2, 6, 0, 1, 8)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.dateEntry = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEntry.setDateTime(QtCore.QDateTime(QtCore.QDate(2017, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEntry.setObjectName("dateEntry")
        self.gridLayout.addWidget(self.dateEntry, 0, 1, 1, 1)
        self.forecastEntry = QtWidgets.QPushButton(self.centralwidget)
        self.forecastEntry.setObjectName("forecastEntry")
        self.gridLayout.addWidget(self.forecastEntry, 5, 9, 1, 2)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setDate(QtCore.QDate(2018, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 5, 11, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.dateEntry, self.dateExit)
        MainWindow.setTabOrder(self.dateExit, self.addStay)
        MainWindow.setTabOrder(self.addStay, self.listWidget)
        MainWindow.setTabOrder(self.listWidget, self.removeStay)
        MainWindow.setTabOrder(self.removeStay, self.calculate)
        MainWindow.setTabOrder(self.calculate, self.listWidget_2)
        MainWindow.setTabOrder(self.listWidget_2, self.forecastEntry)
        MainWindow.setTabOrder(self.forecastEntry, self.dateEdit)
        MainWindow.setTabOrder(self.dateEdit, self.listWidget_3)
        MainWindow.setTabOrder(self.listWidget_3, self.resetAllEntries)

        self.dates = []  # list for periods of stay
        self.dateEntry.setFocus()
        self.addStay.clicked.connect(self.printToList)  # add stay to list widget
        self.removeStay.clicked.connect(self.removeStayAction)  # remove stay from list widget and list of stays
        self.calculate.clicked.connect(self.calculateStay)
        self.forecastEntry.clicked.connect(self.entry_possible)
        self.resetAllEntries.clicked.connect(self.reset_all_entries)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Schengen short-stay calculator [NON OFFICIAL]"))
        self.label_2.setText(_translate("MainWindow", "Exit:"))
        self.resetAllEntries.setText(_translate("MainWindow", "Reset all entries"))
        self.removeStay.setText(_translate("MainWindow", "Remove stay"))
        self.calculate.setText(_translate("MainWindow", "Calculate total duration of stay in the Schenge area"))
        self.addStay.setText(_translate("MainWindow", "Add stay"))
        self.label.setText(_translate("MainWindow", "Entry:"))
        self.forecastEntry.setText(_translate("MainWindow", "Entry possible?"))


    def getDates(self):

        self.dateOfEntry = self.dateEntry.date()
        self.dateIn = self.dateOfEntry.toString()  # for printing str in list widget
        self.dateOfEntryPy = self.dateOfEntry.toPyDate()  # for creating date range with pandas

        self.dateOfExit = self.dateExit.date()  # for doing the if below

        self.dateOut = self.dateOfExit.toString()
        self.dateOfExitPy = self.dateOfExit.toPyDate()

        if self.dateOfExit < self.dateOfEntry:
            # error box for condition Entry > Exit
            msgbox = QtWidgets.QMessageBox()
            msgbox.setText('Date of exit must be after date of entry.')
            msgbox.exec_()
            return False  # To be picked up by def printToList
        elif self.dateOfExitPy > datetime.date.today():
            # error box for condition Exit > today
            msgbox = QtWidgets.QMessageBox()
            msgbox.setText('Date of exit cannot be later than today.')
            msgbox.exec_()
        else:  # check possible periods of stay overlapping and adding stay to list of periods of stay (dates)
            days_overlapping = 0
            for stay in self.dates:
                range_of_stay = pd.date_range(start=stay[0], end=stay[1])
                range_new_item = pd.date_range(start=self.dateOfEntryPy, end=self.dateOfExitPy)
                for day in range_new_item:
                    if day in range_of_stay:
                        days_overlapping += 1
            if days_overlapping > 1:
                msgbox = QtWidgets.QMessageBox()
                msgbox.setText('Durations of stay cannot overlap.')
                msgbox.exec_()
                return False
        # add period of stay to the dates list
        self.dates.append([self.dateOfEntryPy, self.dateOfExitPy])
        self.dates.sort()
        return True

    def printToList(self):
        if self.getDates() is True:
            self.listWidget.addItem('Entry on {} and exit on {}'.format(self.dateIn, self.dateOut))
            self.listWidget.sortItems()

    def removeStayAction(self):
        # error index range handling for when there are no items on the list
        try:
            self.listWidget.takeItem(self.listWidget.currentRow())
            self.dates.remove(self.dates[self.listWidget.currentRow()])
        except IndexError:
            pass

    def createRange(self, list):  # create ranges out of the entry and exit dates
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
                    self.listWidget_2.addItem('You stayed {} days in the Schengen area out of 90 days possible, '
                                              'since your first entry.\n\nATTENTION YOU EXCEEDED THE LEGAL PERIOD '
                                              'OF STAY IN: {} days.'.format(total_of_days, total_of_days - 90))
                else:
                    self.listWidget_2.clear()
                    self.listWidget_2.addItem('You stayed {} days in the Schengen area out of 90 days possible, '
                                              'since your first entry.\n\nYou are allowed to stay {} days until'
                                              ' {}.'.format(total_of_days, 90-total_of_days,
                                                            self.dates[0][0]+datetime.timedelta(180)))
            self.nextPossibleEntry()
        except:
            self.listWidget_2.clear()

    def nextPossibleEntry(self):
        self.listWidget_2.addItem('\nForecast of possible entries and remaining days based on past entries:\n')
        number_loops = 0  # for selecting position in the list dates
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
                    self.listWidget_2.addItem('- From the {} you have a total of {} days of stay allowed\n'
                                              .format(str(stay[1]+datetime.timedelta(180)), 91-total_days_forecast))
            except IndexError:
                self.listWidget_2.addItem('- From the {} you have a total of {} days of stay allowed\n'
                                          .format(str(stay[1] + datetime.timedelta(180)), 90))

    def entry_possible(self):
        entry_test = self.dateEdit.date()
        self.listWidget_3.clear()
        if entry_test < datetime.date.today():
            msgbox = QtWidgets.QMessageBox()
            msgbox.setText('Please use a date greater than today')
            msgbox.exec_()
        elif self.dates == []:
            self.listWidget_3.clear()
        else:
            try:
                range_to_check = pd.date_range(start=entry_test.toPyDate()-datetime.timedelta(180),
                                               end=entry_test.toPyDate())
                total_stay_in_range = 0
                for stay in self.dates:
                    rangeofdates = self.createRange(stay)  # create a range from dateOfEntry and dateOfExit
                    for item in rangeofdates:
                        if item in range_to_check:
                            total_stay_in_range += 1
                if total_stay_in_range > 90:
                    self.listWidget_3.addItem('NOT ALLOWED to enter!\n\nOn {} you have already stayed {} \nin the '
                                              'Schengen area.'.format(entry_test.toPyDate(), total_stay_in_range))
                else:
                    self.listWidget_3.addItem('ALLOWED to enter.\n\nOn the {} you would have spent a \ntotal of {} days'
                                              ' in Schengen.'.format(entry_test.toPyDate()-datetime.timedelta(180),
                                                                     91 - total_stay_in_range))
            except IndexError:
                print(IndexError)
                pass


    def reset_all_entries(self):
        self.dates = []
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.listWidget_3.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

