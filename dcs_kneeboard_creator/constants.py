from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class SettingsConstants:
    hide_selection_outline = "hide_selection_outline"

class Colors:
    transparent = QColor(0, 0, 0, 0)

class WidgetSizes:
    __button_width = 50
    __buton_height = 50
    __icon_modifier = __button_width / 5
    toolbox_button = QSize(__button_width, __buton_height)
    toolbox_button_icon = QSize(__button_width - __icon_modifier, __buton_height - __icon_modifier)