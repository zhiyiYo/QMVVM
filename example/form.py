# coding:utf-8
import sys

from qmvvm import QMVVM

from qtpy.QtCore import Qt
from qtpy.QtWidgets import QLabel, QLineEdit, QPushButton, QCheckBox, QSpinBox, QWidget, QVBoxLayout, QApplication, QComboBox


class Demo(QWidget, QMVVM):

    def __init__(self):
        super().__init__()
        # create components
        self.vBoxLayout = QVBoxLayout(self)
        self.label = QLabel()
        self.lineEdit = QLineEdit()
        self.spinBox = QSpinBox()
        self.button = QPushButton()
        self.checkBox = QCheckBox()
        self.comboBox = QComboBox()

        self.comboBox.addItems(["Item 1", "Item 2", "Item 3"])

        # bind basic type
        self.labelText = self.bind("Label", self.label)
        self.lineEditText = self.bind("Line Edit", self.lineEdit)
        self.buttonText = self.bind("Click button", self.button)
        self.checked = self.bind(True, self.checkBox, "checked")
        self.spinValue = self.bind(1, self.spinBox, "value")
        self.comboBoxIndex = self.bind(1, self.comboBox, "currentIndex")

        # computed property
        self.checkBoxText = self.bind(lambda x=self.spinValue: f"Check Box {x}", self.checkBox)

        # initialize layout
        self.vBoxLayout.addWidget(self.label)
        self.vBoxLayout.addWidget(self.lineEdit)
        self.vBoxLayout.addWidget(self.spinBox)
        self.vBoxLayout.addWidget(self.comboBox)
        self.vBoxLayout.addWidget(self.checkBox)
        self.vBoxLayout.addWidget(self.button)

        self.button.clicked.connect(self.onButtonClicked)

    def onButtonClicked(self):
        # directly manipulate data rather than components
        self.buttonText.value = f"Click button {self.spinValue} times"
        self.spinValue += 1
        self.comboBoxIndex.value = (self.comboBoxIndex + 1) % self.comboBox.count()
        self.labelText.value = f"Label {self.spinValue}"
        self.checked.value = not self.checked
        self.lineEditText.value = f"Line Edit {self.spinValue}"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec()
