import sys
from mask_api import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QDateTimeEdit, QVBoxLayout, QLabel, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
form_class = uic.loadUiType("untitled.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_show_mask.clicked.connect(self.get_image)
        self.pm10, self.pm25 = get_masknum()
        self.pm10_label.setText(f"미세먼지 농도:")
        self.pm25_label.setText(f"초 미세먼지 농도:")
    def get_image(self):
        #미세먼지와 초미세먼지 평균치를 가지고 와서 이미지 순번을 만듬
        avg = self.get_avg(self.pm10, self.pm25)
        print(self.pm10, self.pm25, avg)
        #QPixmap 클래스를 통해 qPuxmapVar 객체를 만들고  load메서드로 이미지를 불러옴
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load(f"mask_{avg}.png")
        #가져온 이미지의 크기가 각각 다를 수 있으므로 사이즈 조절
        self.qPixmaoVar = self.qPixmapVar.scaledToWidth(250)
        #미리 만들어놓은 mask_label에 이미지 적용
        self.mask_label.setPixmap(self.qPixmapVar)
        #미세먼지 초미세먼지 수치 표시
        self.pm10_label.setText(f"미세먼지 농도: {self.pm10}")
        self.pm25_label.setText(f"초 미세먼지 농도: {self.pm25}")
    def get_avg(self,pm10,pm25):
        p10, p25 = 4,4
        pm10_std = [80,150,300]
        pm25_std = [40,75,150]
        for i in range(3):
            if pm10 < pm10_std[i]:
                p10 = i+1
                break
        for i in range(3):
            if pm25 < pm25_std[i]:
                p25 = i+1
                break
        return (p10+ p25) // 2

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WindowClass()
    window.show()
    app.exec_()