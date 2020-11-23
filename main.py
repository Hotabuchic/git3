import sys
from random import choice

from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.setWindowTitle("Git и случайные окружности")
        self.btn = QPushButton("Нарисовать", self)
        self.btn.move(360, 280)


class Window(Window2):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(choice(range(256)), choice(range(256)), choice(range(256))))
            qp.drawEllipse(choice(range(100, 700)), choice(range(100, 500)),
                           choice(range(20, 200)), choice(range(20, 200)))
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
