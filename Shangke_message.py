# -*- coding: utf-8 -*-

"""
Module implementing Shangke_message.
"""
from PyQt5.QtCore import pyqtSlot,QDate,QDateTime
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

from Ui_Shangke_message import Ui_Shangke_message
from stu_data_base.query_data import *


class Shangke_message(QDialog, Ui_Shangke_message):
    """
    Class documentation goes here.
    """
    result = {'Cname': '', 'Sclass': '', 'ClassTime': '', 'Tno': '', 'Date': ''}

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Shangke_message, self).__init__(parent)
        self.setupUi(self)
        Cname = Course_Cname_Query()
        self.Cname_comboBox.clear()
        self.Cname_comboBox.addItems(Cname)
        self.dateEdit.setDate(QDate.currentDate())

    
    @pyqtSlot()
    def on_submit_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """

        self.result['Cname'] = self.Cname_comboBox.currentText()
        self.result['Sclass'] = self.Class_comboBox_2.currentText()
        self.result['ClassTime'] = self.ClassTime_comboBox_3.currentText()
        self.result['Tno'] = self.Tno_comboBox_4.currentText()
        self.result['Date'] = self.dateEdit.text()
        print(self.result)
        self.close()
    
    @pyqtSlot()
    def on_Cancel_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        self.close()

    @pyqtSlot(str)
    def on_Cname_comboBox_currentTextChanged(self, p0):
        """
        Slot documentation goes here.

        @param p0 DESCRIPTION
        @type str
        """
        Class = SC_Student_Class_Query()
        self.Class_comboBox_2.clear()
        self.Class_comboBox_2.addItems(Class)
        ClassTime = ['1-2节','3-4节','5-6节','7-8节','9-10节']
        self.ClassTime_comboBox_3.clear()
        self.ClassTime_comboBox_3.addItems(ClassTime)
        Tno = Teacher_Tno_Query()
        self.Tno_comboBox_4.clear()
        self.Tno_comboBox_4.addItems(Tno)
        
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Shangke_message()
    ui.show()
    sys.exit(app.exec_())
    

