# -*- coding: utf-8 -*-

"""
Module implementing Shangke.
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtGui import *

from Ui_Shangke import Ui_Shangke
from Shangke_message import *
import cv2
from face.face_search import *
from excel.excelwrite import *
from stu_data_base.add_data import *
from stu_data_base.query_data import *


class Shangke(QMainWindow, Ui_Shangke):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Shangke, self).__init__(parent)
        self.setupUi(self)
        self.cam = cv2.VideoCapture(0)
        # self.cam.set(3,640)
        # self.cam.set(4,480)
        self.face_detector = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt.xml')
        self.CWA_Sno_List = []
        # Result ={'学号','姓名','科目','班级','是否出勤','节次','上课日期','时间戳'}
        self.Result ={}

        #Timer1
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)
        #Timer2
        self.timer2 = QTimer(self)
        self.timer2.start(10)
        self.timer2.stop()
        self.timer2.timeout.connect(self.time2out)

    
    @pyqtSlot()
    def on_Add_new_class_button_clicked(self):
        """
        Slot documentation goes here.
        """
        Add_new_class = Shangke_message()
        Add_new_class.exec_()
        result = Shangke_message.result
        # print(result)
        self.lineEdit.setText(result['Cname'])
        self.lineEdit_2.setText(result['Sclass'])
        self.lineEdit_3.setText(result['ClassTime'])
        self.lineEdit_4.setText(result['Tno'])
        self.lineEdit_6.setText(result['Date'])

    def timeout(self):
        # 获取当前系统时间
        self.timer.stop()
        sucess, img = self.cam.read()
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        show = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        self.Img_lable.setPixmap(QPixmap.fromImage(showImage))
        self.Img_lable.setScaledContents(True)
        self.timer.start(50)

    def time2out(self):
        self.timer2.stop()
        count = 0
        sucess, img = self.cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_detector.detectMultiScale(gray, 1.3, 5)
        print(faces)
        if len(faces):
            print(faces)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+w), (0, 255, 0))

            show = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
            self.rec_label_7.setPixmap(QPixmap.fromImage(showImage))
            self.rec_label_7.setScaledContents(True)
            cv2.imwrite('face_temp/face.jpg',img)
            #baidu AIP Seach
            result = face_search(self.lineEdit_2.text(),'face_temp/face.jpg')
            print(result)
            for i in result:
                if (i['score'] > 60):
                    print('list')
                    print(self.CWA_Sno_List)
                    if not (i['user_id'] in self.CWA_Sno_List):
                        self.CWA_Sno_List.append(i['user_id'])
                        self.stu_pic_label_7.setPixmap(QPixmap('./face_stu/'+i['user_id']+'.jpg'))
                        self.stu_pic_label_7.setScaledContents(True)
                        # Result ={'学号','姓名','科目','班级','是否出勤','节次','上课日期','时间戳'}
                        # DataBase = {Sno,Tno,Cname,Sclass,Cwa,ClassTime,Date}
                        self.textEdit.append('message: '+i['user_id']+' CWA Success!')
                        add_CWA(i['user_id'],self.lineEdit_4.text(),self.lineEdit.text(),self.lineEdit_2.text(),'是',self.lineEdit_3.text(),self.lineEdit_6.text())
        self.timer2.start(1000)


    @pyqtSlot()
    def on_Exit_button_clicked(self):
        """
        Slot documentation goes here.
        """
        self.cam.release()
        self.close()

    @pyqtSlot()
    def on_Output_CWA_excel_Now_button_clicked(self):
        """
        Slot documentation goes here.
        """
        # self.lineEdit.setText(result['Cname'])
        # self.lineEdit_2.setText(result['Sclass'])
        # self.lineEdit_3.setText(result['ClassTime'])
        # self.lineEdit_4.setText(result['Tno'])
        # self.lineEdit_6.setText(result['Date'])
        Result = CWA_Message_Query(self.lineEdit_2.text(),self.lineEdit_3.text(), self.lineEdit_6.text(), self.lineEdit.text())
        Create_Cwa_excel_table(self.lineEdit_2.text(),self.lineEdit.text(),Result)

    @pyqtSlot()
    def on_Off_class_button_clicked(self):
        """
        Slot documentation goes here.
        """
        self.timer2.stop()
        self.stu_pic_label_7.clear()
        self.rec_label_7.clear()
        self.CWA_Sno_List.clear()
        self.textEdit.clear()

    @pyqtSlot()
    def on_Start_CWA_button_clicked(self):
        """
        Slot documentation goes here.
        """
        self.timer2.start(500)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Shangke()
    ui.show()
    sys.exit(app.exec_())
    

