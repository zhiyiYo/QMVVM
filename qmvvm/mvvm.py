# coding: utf-8
from typing import Union
from qtpy.QtWidgets import QWidget

from .ref import Ref
from .computed import Computed


class QMVVM:

    def __init__(self, *args, **kwargs):
        pass

    def bind(self, value, widget: QWidget, property="text") -> Union[Ref, Computed]:
        if callable(value):
            reactive = Computed(widget, property, value)
            reactive.update()
        else:
            reactive = Ref(widget, property)
            reactive.value = value

        return reactive
