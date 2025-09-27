# coding:utf-8
import sys

from qmvvm import QMVVM

from qtpy.QtCore import Qt
from qtpy.QtWidgets import QLabel, QPushButton, QWidget, QVBoxLayout, QApplication


class Demo(QWidget, QMVVM):

    def __init__(self):
        super().__init__()
        # create components
        self.vBoxLayout = QVBoxLayout(self)
        self.label = QLabel()
        self.button = QPushButton("Click Me")

        # bind basic type
        self.labelText = self.bind("0", self.label)

        # initialize layout
        self.vBoxLayout.addWidget(self.button)
        self.vBoxLayout.addWidget(self.label)

        self.button.clicked.connect(self.onButtonClicked)

    def onButtonClicked(self):
        # directly manipulate data rather than components
        self.labelText.value = str(int(self.labelText) + 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec()
