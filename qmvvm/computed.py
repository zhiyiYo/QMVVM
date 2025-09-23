# coding: utf-8
import inspect
import weakref

from qtpy.QtCore import QObject
from qtpy.QtWidgets import QWidget

from .ref import Ref

class Computed(QObject):

    def __init__(self, widget: QWidget, property: str, func: callable):
        super().__init__()
        self.func = func
        self.watchedProperty = property
        self.widgetRef = weakref.ref(widget)
        self._register()

    @property
    def widget(self):
        return self.widgetRef()

    @property
    def value(self):
        return self.func()

    def update(self):
        self.widget.setProperty(self.watchedProperty, self.value)

    def _register(self):
        signature = inspect.signature(self.func)
        for arg in signature.parameters.values():
            if isinstance(arg.default, Ref):
                arg.default.valueChanged.connect(self.update)
