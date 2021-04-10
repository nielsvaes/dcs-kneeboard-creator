from functools import partial

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

def action(text, function, parent, *args, **kwargs):
    icon = kwargs.get("icon", None)

    action = QAction(text, parent=parent)
    if icon is not None:
        action.setIcon(QIcon(icon))

    action.triggered.connect(partial(function, *args, **kwargs))
    return action