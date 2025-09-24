# coding:utf-8
import weakref

from qtpy.QtCore import QObject, Signal
from qtpy.QtWidgets import QWidget

from .proxy import Proxy


class Ref(Proxy):

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

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return self.value != other

    def __add__(self, other):
        return self.value + other

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.value += other
        return self

    def __sub__(self, other):
        return self.value - other

    def __isub__(self, other):
        self.value -= other
        return self

    def __rsub__(self, other):
        return other - self.value

    def __mul__(self, other):
        return self.value * other

    def __truediv__(self, other):
        return self.value / other

    def __rtruediv__(self, other):
        return other / self.value

    def __itruediv__(self, other):
        self.value /= other
        return self

    def __floordiv__(self, other):
        return self.value // other

    def __rfloordiv__(self, other):
        return other // self.value

    def __ifloordiv__(self, other):
        self.value //= other
        return self

    def __gt__(self, other):
        return self.value > other

    def __lt__(self, other):
        return self.value < other

    def __ge__(self, other):
        return self.value >= other

    def __le__(self, other):
        return self.value <= other

    def __bool__(self):
        return bool(self.value)

    def __neg__(self):
        return -self.value

    def __abs__(self):
        return abs(self.value)

    def __pos__(self):
        return self.value