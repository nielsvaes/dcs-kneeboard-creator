from PySide6.QtWidgets import *
from PySide6.QtGui import *

import os

import ez_icons
from ez_icons import Icons, Color

from .ui.kneeboard_creator import Ui_kneeboard_creator_window
from .widgets.layer import LayerStackWidget
from .widgets.view import BoardView
from .widgets.scene import BoardScene
from .graphics.layer import Layer

class KneeboardCreatorWindow(QMainWindow, Ui_kneeboard_creator_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.build_ui()
        self.connect_signals()

        self.show()

    def build_ui(self):
        self.scene = BoardScene()
        self.scene.setObjectName('Scene')

        self.view = BoardView(self.scene, self)
        self.view_layout.addWidget(self.view)

        self.layer_stack_widget = LayerStackWidget()
        self.layer_layout.addWidget(self.layer_stack_widget)

        self.splt_view_tools.setSizes([800, 300])


        self.men_new_layer.setIcon(QIcon(ez_icons.get(Color.black, Icons.layers)))

    def connect_signals(self):
        self.men_new_layer.triggered.connect(self.add_layer)

    def add_layer(self):
        layer_item = self.layer_stack_widget.new_layer_item()
        layer = Layer()
        layer.set_list_widget_item(layer_item)
        layer_item.set_graphics_layer(layer)

        self.scene.addItem(layer)


        layer.add_pixmap(QPixmap(r"D:\PersonalCode\kneeboard_creator\kneeboard_creator\images\paper_test.jpg"))

