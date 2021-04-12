import sys
import logging
logging.basicConfig(level=logging.INFO)

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from ez_settings import EZSettings
from ..constants import SettingsConstants as sk

class CustomGraphicsItem(QGraphicsItem):
    DEFAULT_RECTF = QRectF(0, 0, 50, 50)

    def __init__(self, layer, x_pos=0, y_pos=0, rectf=DEFAULT_RECTF):
        super().__init__()
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
        self.setFlag(QGraphicsItem.ItemSendsScenePositionChanges)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setAcceptHoverEvents(True)

        self.__layer = layer

        self.__brush = QBrush()
        self.__brush.setColor(QColor(255, 0, 0))
        self.__pen = QPen()
        self.__pen.setColor(QColor(255, 0, 0))
        self.__pen.setWidthF(3)

        self.__rectf = rectf
        self.__mouse_over = False

        self.setTransformOriginPoint(self.__rectf.center())
        self.setPos(x_pos, y_pos)

    def layer(self):
        return self.__layer

    def set_layer(self, value):
        self.__layer = value

    def set_fill_color(self, q_color):
        self.__brush.setColor(q_color)
        self.update()

    def set_stroke_color(self, q_color):
        self.__pen.setColor(q_color)
        self.update()

    def set_stroke_width(self, width):
        self.__pen.setWidthF(float(width))
        self.update()

    def set_bounding_rect(self, rectf):
        self.__rectf = rectf

    def brush(self):
        return self.__brush

    def pen(self):
        return self.__pen

    def mouseReleaseEvent(self, event):
        self.update()
        super().mouseReleaseEvent(event)

    def boundingRect(self):
        return self.__rectf

    def paint(self, painter, option, widget):
        if EZSettings().get(sk.hide_selection_outline, True):
            option.state = QStyle.State_NoChange

