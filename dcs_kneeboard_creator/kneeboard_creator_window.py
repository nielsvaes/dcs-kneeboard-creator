from PySide6.QtWidgets import *
from PySide6.QtGui import *

import os

import ez_icons
from ez_icons import Icons, Color

from .ui.kneeboard_creator import Ui_kneeboard_creator_window
from .widgets.layer import LayerControlWidget
from .widgets.view import BoardView
from .widgets.scene import BoardScene
from .widgets.toolbox import ToolBox
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

        self.layer_control_widget = LayerControlWidget(self)
        self.layer_layout.addWidget(self.layer_control_widget)

        self.tool_box = ToolBox(parent=self)
        self.tools_layout.addWidget(self.tool_box)

        self.splt_view_tools.setSizes([800, 300])


        self.men_new_layer.setIcon(QIcon(ez_icons.get(Color.black, Icons.add)))
        self.men_duplicate_layer.setIcon(QIcon(ez_icons.get(Color.black, Icons.layers)))
        self.men_del_layer.setIcon(QIcon(ez_icons.get(Color.black, Icons.remove)))

        self.men_copy.setIcon(QIcon(ez_icons.get(Color.black, Icons.content_copy)))
        self.men_paste.setIcon(QIcon(ez_icons.get(Color.black, Icons.content_paste)))

    def connect_signals(self):
        self.men_new_layer.triggered.connect(self.add_layer)

    def add_layer(self):
        layer_item = self.layer_control_widget.layer_stack_widget.new_layer_item()
        layer = Layer()
        layer.set_list_widget_item(layer_item)
        layer_item.set_graphics_layer(layer)

        self.scene.addItem(layer)
        return layer_item

    def get_active_layer(self):
        try:
            return self.layer_control_widget.layer_stack_widget.selectedItems()[0]
        except:
            print("No active layer selected")
            return None