# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\zhou\Desktop\Client\Shangke.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Shangke(object):
    def setupUi(self, Shangke):
        Shangke.setObjectName("Shangke")
        Shangke.resize(923, 568)
        self.centralWidget = QtWidgets.QWidget(Shangke)
        self.centralWidget.setObjectName("centralWidget")
        self.Img_lable = QtWidgets.QLabel(self.centralWidget)
        self.Img_lable.setGeometry(QtCore.QRect(249, 40, 371, 271))
        self.Img_lable.setObjectName("Img_lable")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(33, 50, 61, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(33, 150, 61, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(33, 200, 61, 20))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(33, 100, 61, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(33, 250, 61, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 50, 113, 20))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 100, 113, 20))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 150, 113, 20))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 200, 113, 20))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(100, 250, 113, 20))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.Add_new_class_button = QtWidgets.QPushButton(self.centralWidget)
        self.Add_new_class_button.setGeometry(QtCore.QRect(20, 320, 191, 51))
        self.Add_new_class_button.setObjectName("Add_new_class_button")
        self.Output_CWA_excel_Now_button = QtWidgets.QPushButton(self.centralWidget)
        self.Output_CWA_excel_Now_button.setGeometry(QtCore.QRect(20, 390, 191, 51))
        self.Output_CWA_excel_Now_button.setObjectName("Output_CWA_excel_Now_button")
        self.Exit_button = QtWidgets.QPushButton(self.centralWidget)
        self.Exit_button.setGeometry(QtCore.QRect(20, 460, 191, 51))
        self.Exit_button.setObjectName("Exit_button")
        self.Off_class_button = QtWidgets.QPushButton(self.centralWidget)
        self.Off_class_button.setGeometry(QtCore.QRect(690, 460, 191, 51))
        self.Off_class_button.setObjectName("Off_class_button")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(240, 350, 421, 161))
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(240, 320, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Start_CWA_button = QtWidgets.QPushButton(self.centralWidget)
        self.Start_CWA_button.setGeometry(QtCore.QRect(690, 380, 191, 51))
        self.Start_CWA_button.setObjectName("Start_CWA_button")
        self.rec_label_7 = QtWidgets.QLabel(self.centralWidget)
        self.rec_label_7.setGeometry(QtCore.QRect(660, 20, 211, 161))
        self.rec_label_7.setObjectName("rec_label_7")
        self.stu_pic_label_7 = QtWidgets.QLabel(self.centralWidget)
        self.stu_pic_label_7.setGeometry(QtCore.QRect(710, 200, 121, 151))
        self.stu_pic_label_7.setObjectName("stu_pic_label_7")
        Shangke.setCentralWidget(self.centralWidget)

        self.retranslateUi(Shangke)
        QtCore.QMetaObject.connectSlotsByName(Shangke)

    def retranslateUi(self, Shangke):
        _translate = QtCore.QCoreApplication.translate
        Shangke.setWindowTitle(_translate("Shangke", "Shangke"))
        self.Img_lable.setText(_translate("Shangke", "Img"))
        self.label.setText(_translate("Shangke", "科    目："))
        self.label_2.setText(_translate("Shangke", "节    次："))
        self.label_3.setText(_translate("Shangke", "教师工号："))
        self.label_5.setText(_translate("Shangke", "班    级:"))
        self.label_6.setText(_translate("Shangke", "上课日期："))
        self.Add_new_class_button.setText(_translate("Shangke", "新增上课信息"))
        self.Output_CWA_excel_Now_button.setText(_translate("Shangke", "打印当前节次考勤报表"))
        self.Exit_button.setText(_translate("Shangke", "退出"))
        self.Off_class_button.setText(_translate("Shangke", "下课"))
        self.label_4.setText(_translate("Shangke", "签到情况："))
        self.Start_CWA_button.setText(_translate("Shangke", "开始考勤"))
        self.rec_label_7.setText(_translate("Shangke", "TextLabel"))
        self.stu_pic_label_7.setText(_translate("Shangke", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Shangke = QtWidgets.QMainWindow()
    ui = Ui_Shangke()
    ui.setupUi(Shangke)
    Shangke.show()
    sys.exit(app.exec_())

