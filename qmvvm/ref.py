# coding:utf-8
import weakref
import warnings

from qtpy.QtCore import QObject, Signal, QMetaProperty
from qtpy.QtWidgets import QWidget

from .proxy import Proxy


class Ref(Proxy):

    def __init__(self, widget: QWidget, property: str):
        super().__init__()
        self.watchedProperty = property
        self.widgetRef = weakref.ref(widget)
        self._connectSignal(widget)

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

    def _connectSignal(self, widget):
        metaObject = widget.metaObject()
        property = self.watchedProperty
        index = metaObject.indexOfProperty(property)

        if index == -1:
            return

        metaProperty = metaObject.property(index)

        if not metaProperty.hasNotifySignal():
            warnings.warn(f"'{property}' doesn't have NOTIFY signal")
            return

        notifySignal = metaProperty.notifySignal()
        signal = getattr(widget, notifySignal.name().data().decode('utf-8'))
        signal.connect(lambda: self.valueChanged.emit())
