import sys
import logging
logging.basicConfig(level=logging.INFO)

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

import ez_utils.general as utils
import ez_utils.io_utils as io_utils

from ..graphics.waypoint import Waypoint

class BoardScene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.setBackgroundBrush(QColor(20, 20, 20))
        self.setSceneRect(0, 0, 768, 1024)

        self.TEST_DELETEME()


        self.add_boundary()

    def TEST_DELETEME(self):
        test = QGraphicsRectItem(0, 0, 50, 60)
        test.setBrush(QBrush(QColor(255, 0, 255)))

        test.setFlag(QGraphicsRectItem.ItemIsSelectable)
        test.setFlag(QGraphicsRectItem.ItemIsMovable)
        test.setFlag(QGraphicsRectItem.ItemSendsGeometryChanges)

        test2 = QGraphicsRectItem(0, 60, 50, 60)
        test2.setBrush(QBrush(QColor(255, 0, 0)))

        test2.setFlag(QGraphicsRectItem.ItemIsSelectable)
        test2.setFlag(QGraphicsRectItem.ItemIsMovable)
        test2.setFlag(QGraphicsRectItem.ItemSendsGeometryChanges)


        self.addItem(test)
        self.addItem(test2)

        waypoint = Waypoint(200, 400)
        self.addItem(waypoint)

    def add_boundary(self):
        self.boundary = QGraphicsRectItem(0, 0, 768, 1024)
        self.boundary.setPen(QPen(QColor(0, 0, 0)))
        self.boundary.setZValue(10000)

        self.addItem(self.boundary)

    def render_scene(self):
        self.setSceneRect(0, 0, 768, 1024)
        image = QImage(self.sceneRect().size().toSize(), QImage.Format_ARGB32)
        image.fill(Qt.transparent)

        painter = QPainter(image)
        self.render(painter)
        image.save(r"D:/test_image.png")
        painter.end()

    def dragMoveEvent(self, event):
        event.accept()

    # def dropEvent(self, event):
    #     try:
    #         class_name = event.source().selectedItems()[0].file_name_no_ext
    #         module = event.source().selectedItems()[0].folder_name
    #
    #         x = event.scenePos().x()
    #         y = event.scenePos().y()
    #
    #         dropped_node = self.add_node_to_view(class_name, module, x, y)
    #     except Exception as err:
    #         utils.trace(err)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_R and event.modifiers() == Qt.ControlModifier:
            print("rendering")
            self.render_scene()
            # self.delete_nodes()
