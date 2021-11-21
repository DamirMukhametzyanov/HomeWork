import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Generate_circle.ui', self)
        self.setWindowTitle('Git и желтые окружности')
        self.do_paint = False
        self.generate.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        num = random.randint(1, 10)
        qp.setBrush(QColor(255, 255, 0))
        for i in range(num):
            diam = random.randint(1, 200)
            x, y = random.randint(1, 700), random.randint(1, 500)
            qp.drawEllipse(x, y, diam // 2, diam // 2)
        self.do_paint = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
