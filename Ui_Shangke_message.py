# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\zhou\Desktop\Client\Shangke_message.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Shangke_message(object):
    def setupUi(self, Shangke_message):
        Shangke_message.setObjectName("Shangke_message")
        Shangke_message.resize(299, 406)
        Shangke_message.setSizeGripEnabled(True)
        self.label = QtWidgets.QLabel(Shangke_message)
        self.label.setGeometry(QtCore.QRect(33, 30, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Shangke_message)
        self.label_2.setGeometry(QtCore.QRect(33, 80, 61, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Shangke_message)
        self.label_3.setGeometry(QtCore.QRect(33, 130, 61, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Shangke_message)
        self.label_4.setGeometry(QtCore.QRect(33, 180, 61, 20))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Shangke_message)
        self.label_6.setGeometry(QtCore.QRect(33, 230, 61, 20))
        self.label_6.setObjectName("label_6")
        self.dateEdit = QtWidgets.QDateEdit(Shangke_message)
        self.dateEdit.setGeometry(QtCore.QRect(100, 230, 151, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.Cname_comboBox = QtWidgets.QComboBox(Shangke_message)
        self.Cname_comboBox.setGeometry(QtCore.QRect(100, 30, 151, 22))
        self.Cname_comboBox.setObjectName("Cname_comboBox")
        self.Class_comboBox_2 = QtWidgets.QComboBox(Shangke_message)
        self.Class_comboBox_2.setGeometry(QtCore.QRect(100, 80, 151, 22))
        self.Class_comboBox_2.setObjectName("Class_comboBox_2")
        self.ClassTime_comboBox_3 = QtWidgets.QComboBox(Shangke_message)
        self.ClassTime_comboBox_3.setGeometry(QtCore.QRect(100, 130, 151, 22))
        self.ClassTime_comboBox_3.setObjectName("ClassTime_comboBox_3")
        self.Tno_comboBox_4 = QtWidgets.QComboBox(Shangke_message)
        self.Tno_comboBox_4.setGeometry(QtCore.QRect(100, 180, 151, 22))
        self.Tno_comboBox_4.setObjectName("Tno_comboBox_4")
        self.submit_pushButton = QtWidgets.QPushButton(Shangke_message)
        self.submit_pushButton.setGeometry(QtCore.QRect(30, 330, 111, 51))
        self.submit_pushButton.setObjectName("submit_pushButton")
        self.Cancel_pushButton_2 = QtWidgets.QPushButton(Shangke_message)
        self.Cancel_pushButton_2.setGeometry(QtCore.QRect(160, 330, 111, 51))
        self.Cancel_pushButton_2.setObjectName("Cancel_pushButton_2")

        self.retranslateUi(Shangke_message)
        QtCore.QMetaObject.connectSlotsByName(Shangke_message)

    def retranslateUi(self, Shangke_message):
        _translate = QtCore.QCoreApplication.translate
        Shangke_message.setWindowTitle(_translate("Shangke_message", "Shangke_message"))
        self.label.setText(_translate("Shangke_message", "科    目："))
        self.label_2.setText(_translate("Shangke_message", "班    级："))
        self.label_3.setText(_translate("Shangke_message", "节    次："))
        self.label_4.setText(_translate("Shangke_message", "教师工号："))
        self.label_6.setText(_translate("Shangke_message", "上课日期："))
        self.submit_pushButton.setText(_translate("Shangke_message", "提交"))
        self.Cancel_pushButton_2.setText(_translate("Shangke_message", "取消"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Shangke_message = QtWidgets.QDialog()
    ui = Ui_Shangke_message()
    ui.setupUi(Shangke_message)
    Shangke_message.show()
    sys.exit(app.exec_())

