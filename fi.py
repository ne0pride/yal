import random, sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor, QPainter


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(511, 369)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 451, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "КРУГ"))

class TMyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.press)
        self.Flag = False

    def paintEvent(self, event):
        if self.Flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def press(self):
        self.Flag = True
        self.repaint()

    def draw_flag(self, qp):
        x = random.randint(0, 180)
        col, col1, col2 = random.randint(0, 250), random.randint(0, 250), random.randint(0, 250)
        qp.setBrush(QColor(col, col1, col2))
        qp.drawEllipse(x, x, x, x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win1 = TMyWindow()
    win1.show()
    sys.exit(app.exec())
