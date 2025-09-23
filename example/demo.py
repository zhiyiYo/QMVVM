# coding:utf-8
import sys

from qmvvm import QMVVM

from qtpy.QtCore import Qt
from qtpy.QtWidgets import QLabel, QLineEdit, QPushButton, QCheckBox, QSpinBox, QWidget, QVBoxLayout, QApplication


class Demo(QWidget, QMVVM):

    def __init__(self):
        super().__init__()
        # 创建组件
        self.vBoxLayout = QVBoxLayout(self)
        self.label = QLabel()
        self.lineEdit = QLineEdit()
        self.spinBox = QSpinBox()
        self.button = QPushButton()
        self.checkBox = QCheckBox()

        # 绑定基本数据类型
        self.labelText = self.bind("标签文本", self.label)
        self.lineEditText = self.bind("输入框文本", self.lineEdit)
        self.buttonText = self.bind("点击按钮", self.button)
        self.checked = self.bind(True, self.checkBox, "checked")
        self.spinValue = self.bind(1, self.spinBox, "value")

        # 绑定计算属性
        self.checkBoxText = self.bind(lambda x=self.spinValue: f"复选框文本 {x}", self.checkBox)

        # 初始化布局
        self.vBoxLayout.addWidget(self.label)
        self.vBoxLayout.addWidget(self.lineEdit)
        self.vBoxLayout.addWidget(self.spinBox)
        self.vBoxLayout.addWidget(self.checkBox)
        self.vBoxLayout.addWidget(self.button)

        self.button.clicked.connect(self.onButtonClicked)

    def onButtonClicked(self):
        self.buttonText.value = f"按钮点击 {self.spinValue} 次"
        self.spinValue.value += 1
        self.labelText.value = f"标签文本 {self.spinValue}"
        self.checked.value = not self.checked.value
        self.lineEditText.value = f"输入框文本 {self.spinValue}"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec()
