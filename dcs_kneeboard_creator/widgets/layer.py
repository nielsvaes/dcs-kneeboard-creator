from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from ez_settings import EZSettings
import ez_icons
from ez_icons import i, c

from .. import utils

class Roles:
    DISPLAY = Qt.DisplayRole
    WIDGET  = Qt.UserRole + 1
    GRAPHICS_LAYER  = Qt.UserRole + 2


class LayerStackWidget(QListWidget):
    def __init__(self):
        super().__init__()
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setDefaultDropAction(Qt.MoveAction)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_menu)

    def new_layer_item(self, layer_text=False):
        if layer_text is False:
            index = self.count() + 1
            layer_text = "New Layer %s" % index

        item_widget = LayerWidget(layer_text)
        layer_widget_item = LayerWidgetItem(item_widget)

        self.addItem(layer_widget_item)
        self.setItemWidget(layer_widget_item, item_widget)

        self.set_z_depths()

        return layer_widget_item

    def get_selected_layer(self):
        return self.selectedItems()[0]

    def get_selected_widget(self):
        return self.get_selected_layer().data(Roles.WIDGET)

    def set_z_depths(self):
        try:
            for index, row in enumerate(reversed(range(self.count()))):
                self.item(row).graphics_layer().setZValue(index)
        except:
            pass

    def show_menu(self):
        menu = QMenu()
        menu.addAction(utils.action("Delete", self.delete_layer, self, icon=ez_icons.get(c.black, i.delete)))

        menu.exec_(QCursor.pos())

    def delete_layer(self, *args, **kwargs):
        for selected_layer_item in self.selectedItems():
            selected_layer_item.destroy_graphics_layer()
            self.takeItem(self.row(selected_layer_item))

    def dropEvent(self, event):
        super().dropEvent(event)
        self.set_z_depths()


class LayerWidgetItem(QListWidgetItem):
    def __init__(self, widget=None):
        super().__init__()
        self.__widget = None
        self.__graphics_layer = None

        if widget is not None:
            self.__widget = widget

        self.setSizeHint(widget.sizeHint())

    def widget(self):
        return self.__widget

    def set_widget(self, widget):
        self.__widget = widget

    def graphics_layer(self):
        return self.__graphics_layer

    def set_graphics_layer(self, layer):
        self.__graphics_layer = layer

    def destroy_graphics_layer(self):
        self.graphics_layer().destroy()
        del self.__graphics_layer


class LayerWidget(QWidget):
    def __init__(self, text):
        super().__init__()
        self.layout = QHBoxLayout()

        self.chk_visible = QCheckBox()
        self.chk_visible.setChecked(True)
        self.txt_name = CustomLineEdit(text)

        self.layout.addWidget(self.chk_visible)
        self.layout.addWidget(self.txt_name)

        self.setLayout(self.layout)

        self.layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.layout.setContentsMargins(5, 3, 5, 3)

        self.text = text

    def mouseDoubleClickEvent(self, event):
        self.txt_name.setEnabled(True)
        self.txt_name.setFocus()
        self.txt_name.selectAll()


class CustomLineEdit(QLineEdit):
    def __init__(self, text):
        super().__init__()
        self.setEnabled(False)
        self.setText(text)
        self.previous_text = text
        self.editingFinished.connect(self.accepted_editing)

    def accepted_editing(self):
        self.previous_text = self.text()
        self.setEnabled(False)

    def cancelled_editing(self):
        self.setText(self.previous_text)
        self.setEnabled(False)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.accepted_editing()

        if event.key() == Qt.Key_Escape:
            self.cancelled_editing()

        super().keyPressEvent(event)
