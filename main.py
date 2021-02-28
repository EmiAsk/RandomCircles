from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QColor, QPainter
from random import randint
from UI import Ui_Form
import sys


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Circles(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Желтые окружности')
        self.w, self.h = self.width(), self.height()
        self.pushButton.clicked.connect(self.paint)
        self.ok_draw = False

    def paint(self):
        self.ok_draw = True
        self.repaint()

    def draw_circle(self, qp: QPainter):
        qp.setBrush(QColor('#' + hex(randint(0, 16777215))[2:]))

        diameter = randint(1, min(self.w, self.h - 200))
        x, y = randint(0, self.w - diameter), randint(0, self.h - 200 - diameter)
        qp.drawEllipse(x, y, diameter, diameter)

    def paintEvent(self, a0):
        if self.ok_draw:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
            self.ok_draw = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Circles()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
