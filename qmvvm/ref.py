# coding:utf-8
import weakref

from qtpy.QtCore import QObject, Signal
from qtpy.QtWidgets import QWidget


class Ref(QObject):

    valueChanged = Signal()

    def __init__(self, widget: QWidget, property: str):
        super().__init__()
        self.watchedProperty = property
        self.widgetRef = weakref.ref(widget)

    @property
    def widget(self):
        return self.widgetRef()

    @property
    def value(self):
        if self.widget is None:
            return None

        return self.widget.property(self.watchedProperty)

    @value.setter
    def value(self, value):
        if value == self.value:
            return

        self.widget.setProperty(self.watchedProperty, value)
        self.valueChanged.emit()

    def __repr__(self):
        return str(self.value)
