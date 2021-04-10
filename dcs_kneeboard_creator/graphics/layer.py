import sys
import logging
logging.basicConfig(level=logging.INFO)

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class Layer(QGraphicsItemGroup):
    def __init__(self):
        super().__init__()
        self.__list_widget_item = None

    def add_pixmap(self, pixmap):
        pixmap_item = QGraphicsPixmapItem(pixmap)
        self.addToGroup(pixmap_item)

    def list_widget_item(self):
        return self.__list_widget_item

    def set_list_widget_item(self, value):
        self.__list_widget_item = value

    def destroy(self):
        self.scene().removeItem(self)
