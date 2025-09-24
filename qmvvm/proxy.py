# coding:utf-8
import weakref

from qtpy.QtCore import QObject, Signal
from qtpy.QtWidgets import QWidget


class Proxy(QObject):

    valueChanged = Signal()

    def __init__(self):
        super().__init__()

    @property
    def value(self):
        return None

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

    def __rmul__(self, other):
        return other * self.value

    def __imul__(self, other):
        self.value *= other
        return self

    def __mod__(self, other):
        return self.value % other

    def __rmod__(self, other):
        return other % self.value

    def __imod__(self, other):
        self.value %= other
        return self

    def __pow__(self, other):
        return self.value ** other

    def __rpow__(self, other):
        return other ** self.value

    def __ipow__(self, other):
        self.value **= other
        return self

    def __truediv__(self, other):
        return self.value / other

    def __floordiv__(self, other):
        return self.value // other

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

    def __len__(self):
        return len(self.value)

    def __or__(self, other):
        return self.value | other

    def __and__(self, other):
        return self.value & other

    def __rand__(self, other):
        return other & self.value

    def __iand__(self, other):
        self.value &= other
        return self

    def __xor__(self, other):
        return self.value ^ other

    def __rxor__(self, other):
        return other ^ self.value

    def __ixor__(self, other):
        self.value ^= other
        return self

    def __ror__(self, other):
        return other | self.value

    def __ior__(self, other):
        self.value |= other
        return self

    def __lshift__(self, other):
        return self.value << other

    def __rlshift__(self, other):
        return other << self.value

    def __ilshift__(self, other):
        self.value <<= other
        return self

    def __rshift__(self, other):
        return self.value >> other

    def __rrshift__(self, other):
        return other >> self.value

    def __irshift__(self, other):
        self.value >>= other
        return self

    def __round__(self, n=None):
        return round(self.value, n) if n is not None else round(self.value)

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __complex__(self):
        return complex(self.value)

    def __index__(self):
        return int(self.value)

    def __invert__(self):
        return ~self.value
