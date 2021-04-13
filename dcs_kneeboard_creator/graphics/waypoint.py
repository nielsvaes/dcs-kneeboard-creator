import sys
import logging
logging.basicConfig(level=logging.INFO)

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from .core import CustomGraphicsItem
from ..constants import Colors

SIZE = 20
PEN_WIDTH = 5

class Waypoint(CustomGraphicsItem):
    def __init__(self, layer, x_pos=0, y_pos=0, number=15):
        super().__init__(layer, x_pos, y_pos)
        self.number = number

        self.set_fill_color(Colors.transparent)
        self.set_stroke_color(QColor(0, 255, 0, 255))
        self.set_stroke_width(5)

    def paint(self, painter: QPainter, option, widget):
        painter.setBrush(self.brush())
        painter.setPen(self.pen())
        painter.drawEllipse(self.boundingRect())

        font = QFont("Arial", 15)
        painter.setFont(font)
        painter.drawText(self.boundingRect().right(), self.boundingRect().bottom() + self.boundingRect().height() / 3, str(self.number))


        super().paint(painter, option, widget)


class WaypointConnection(QGraphicsLineItem):
    def __init__(self):
        super().__init__()

class WaypointNumber(QGraphicsItem):
    def __init__(self):
        super().__init__()
