import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer
from exemple import*
import time

class Chrono(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.m, self.s, self.t = 0, 0, 0

        def tick():
        
            self.t +=1
            if self.t == 100:
                self.t =0
                self.s += 1
            if self.s == 60:
                self.s = 0
                self.m += 1
            self.ui.compteur.display(f"{self.m:02}:{self.s:02}:{self.t:02}")

        self.timer = QTimer(self)
        self.timer.timeout.connect(tick)
        self.timer.start(10)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Chrono()
    w.show()
    sys.exit(app.exec_())
