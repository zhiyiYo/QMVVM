# coding:utf-8
import sys

from qmvvm import QMVVM

from qtpy.QtCore import Qt
from qtpy.QtWidgets import QLabel, QLineEdit, QHBoxLayout, QSpinBox, QWidget, QVBoxLayout, QApplication


class Demo(QWidget, QMVVM):

    def __init__(self):
        super().__init__()
        # create components
        self.hBoxLayout = QHBoxLayout(self)
        self.celsiusLineEdit = QSpinBox()
        self.celsiusLabel = QLabel("Celsius=")
        self.fahrenheitLineEdit = QLineEdit()
        self.fahrenheitLabel = QLabel("Fahrenheit")

        # bind basic type
        self.celText = self.bind(0, self.celsiusLineEdit, "value")
        self.fahText = self.bind(lambda cel=self.celText: str(
            cel * 9 / 5 + 32), self.fahrenheitLineEdit)

        # initialize layout
        self.hBoxLayout.addWidget(self.celsiusLineEdit)
        self.hBoxLayout.addWidget(self.celsiusLabel)
        self.hBoxLayout.addWidget(self.fahrenheitLineEdit)
        self.hBoxLayout.addWidget(self.fahrenheitLabel)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec()
