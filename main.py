import sys
import random
from PyQt5 import QtWidgets, QtGui, QtCore, uic


class Circles(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.f = False
        self.pushButton.clicked.connect(self.click)

    def click(self):
        self.f = True
        self.repaint()

    def paintEvent(self, event):
        if self.f:
            qp = QtGui.QPainter()
            qp.begin(self)
            qp.setBrush(QtGui.QColor(255, 255, 0))
            qp.setPen(QtGui.QColor(255, 255, 0))
            r = random.randint(1, 400)
            qp.drawEllipse(QtCore.QPointF(random.randint(0, 800), random.randint(0, 600)), r, r)
            qp.end()
            self.f = False


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    circles = Circles()
    circles.show()
    sys.exit(app.exec())
