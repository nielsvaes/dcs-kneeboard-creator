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

class LayerControlWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setLayout(QVBoxLayout())

        self.spacer = QSpacerItem(300, 10)
        self.btn_new_layer = QPushButton()
        self.btn_new_layer.setIcon(QIcon(ez_icons.get(c.black, i.add)))
        self.btn_new_layer.clicked.connect(self.parent().add_layer)

        self.btn_remove_layer = QPushButton()
        self.btn_remove_layer.setIcon(QIcon(ez_icons.get(c.black, i.remove)))

        self.btn_move_up = QPushButton()
        self.btn_move_up.setIcon(QIcon(ez_icons.get(c.black, i.arrow_upward)))

        self.btn_move_down = QPushButton()
        self.btn_move_down.setIcon(QIcon(ez_icons.get(c.black, i.arrow_downward)))

        self.layer_controls_layout = QHBoxLayout()
        self.layer_controls_layout.addItem(self.spacer)
        self.layer_controls_layout.addWidget(self.btn_new_layer)
        self.layer_controls_layout.addWidget(self.btn_remove_layer)
        self.layer_controls_layout.addWidget(self.btn_move_up)
        self.layer_controls_layout.addWidget(self.btn_move_down)

        self.layer_stack_widget = LayerStackWidget()
        self.layout().addWidget(self.layer_stack_widget)
        self.layout().addLayout(self.layer_controls_layout)

        print(self.parent())


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

        item_widget = CustomWidget(layer_text)
        layer_widget_item = CustomListWidgetItem(item_widget)
        item_widget.set_parent_list_widget_item(layer_widget_item)

        row = 0
        try:
            row = self.row(self.selectedItems()[0])
        except:
            pass

        self.insertItem(row, layer_widget_item)
        self.setItemWidget(layer_widget_item, item_widget)

        self.set_z_depths()

        self.clearSelection()
        self.setCurrentRow(row)

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
        menu.addAction(utils.action("Delete", self.delete_selected_layers, self, icon=ez_icons.get(c.black, i.delete)))
        menu.addAction(utils.action("Toggle visibility", self.toggle_selected_layers_visibility, self, icon=ez_icons.get(c.black, i.visibility)))

        menu.exec_(QCursor.pos())

    def toggle_selected_layers_visibility(self, *args, **kwargs):
        for selected_layer_item in self.selectedItems():
            selected_layer_item.toggle_visibility()

    def delete_selected_layers(self, *args, **kwargs):
        for selected_layer_item in self.selectedItems():
            self.delete_layer(selected_layer_item)

    def delete_layer(self, item_to_delete):
        deleted_item = self.takeItem(self.row(item_to_delete))
        deleted_item.destroy_graphics_layer()
        del deleted_item

    def dropEvent(self, event):
        super().dropEvent(event)
        self.set_z_depths()


class CustomListWidgetItem(QListWidgetItem):
    def __init__(self, widget=None):
        super().__init__()
        self.__widget = None
        self.__graphics_layer = None

        if widget is not None:
            self.__widget = widget


        self.__visible = True
        self.setSizeHint(widget.sizeHint())

    def visible(self):
        return self.__visible

    def set_visible(self, value):
        self.__visible = value

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

    def toggle_visibility(self):
        self.set_visible(not self.visible())
        if self.visible():
            self.widget().btn_visible.setIcon(QIcon(ez_icons.get(c.black, i.visibility)))
        else:
            self.widget().btn_visible.setIcon(QIcon(ez_icons.get(c.black, i.visibility_off)))

    def destroy_self(self):
        self.listWidget().delete_layer(self)


class CustomWidget(QWidget):
    def __init__(self, text, parent=None):
        super().__init__(parent=parent)
        self.layout = QHBoxLayout()

        self.btn_visible = QPushButton()
        self.btn_visible.setIcon(QIcon(ez_icons.get(c.black, i.visibility)))
        self.btn_visible.clicked.connect(self.set_visibility)
        self.btn_visible.setFlat(True)
        self.txt_name = CustomLineEdit(text)
        self.btn_delete = QPushButton()
        self.btn_delete.setIcon(QIcon(ez_icons.get(c.black, i.delete_forever)))
        self.btn_delete.clicked.connect(self.delete_parent_item)

        self.layout.addWidget(self.btn_visible)
        self.layout.addWidget(self.txt_name)
        self.layout.addWidget(self.btn_delete)

        self.setLayout(self.layout)

        self.layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.layout.setContentsMargins(5, 3, 5, 3)

        self.text = text
        self.__parent_list_widget_item = None

    def parent_list_widget_item(self):
        return self.__parent_list_widget_item

    def set_parent_list_widget_item(self, value):
        self.__parent_list_widget_item = value

    def delete_parent_item(self):
        self.parent_list_widget_item().destroy_self()

    def set_visibility(self):
        self.parent_list_widget_item().toggle_visibility()

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
