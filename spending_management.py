import sys
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import datetime
import os

class Ui_Dialog(QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()

        loadUi('main.ui', self)
        self.Sum = 0

        self.timer = QTimer(self) #create timer

        self.sumBtn.clicked.connect(self.sumClicked)
        self.cloneBtn.clicked.connect(self.cloneClicked)

    @pyqtSlot()
    def sumClicked(self):
        
        eat = self.eatTxt.toPlainText()
        sun = self.sunTxt.toPlainText()
        self.Sum = (int)(eat)+(int)(sun)
        self.label.setText('Tổng số tiền hôm nay Đạt tiêu là: '+(str)(self.Sum)+'.000 VND')

    def cloneClicked(self):
        with open('Management.csv', 'a') as f:
            date_time_string = datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S")
            f.writelines(f'\n{self.Sum},{date_time_string}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_Dialog()
    window.show()
    try:
        sys.exit(app.exec_())
    except:
        print('Exiting')