from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from ez_settings import EZSettings
import ez_icons
from ez_icons import c, i

from .. import utils
from ..constants import WidgetSizes

class ToolBox(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(FlowLayout())

        for index in range(25):
            button = ToolBoxButton(icon=ez_icons.get(c.black, i.my_location), text="Waypoint")
            self.layout().addWidget(button)

class ToolBoxButton(QToolButton):
    def __init__(self, text=None, icon=None):
        super().__init__()
        self.setMinimumSize(WidgetSizes.toolbox_button)
        self.setMaximumSize(WidgetSizes.toolbox_button)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        if text is not None:
            self.setText(text)
        if icon is not None:
            if isinstance(icon, str):
                icon = QIcon(icon)
            self.setIcon(icon)
            self.setIconSize(WidgetSizes.toolbox_button_icon)


class FlowLayout(QLayout):
    def __init__(self, parent=None, margin=0, spacing=-1):
        super(FlowLayout, self).__init__(parent)

        if parent is not None:
            self.setMargin(margin)

        self.setSpacing(spacing)
        self.margin = margin
        # self.spacing = spacing

        self.itemList = []

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item):
        self.itemList.append(item)

    def count(self):
        return len(self.itemList)

    def itemAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList[index]

        return None

    def takeAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList.pop(index)

        return None

    def expandingDirections(self):
        return Qt.Orientations(Qt.Orientation(0))

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height = self._doLayout(QRect(0, 0, width, 0), True)
        return height

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self._doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()

        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())

        size += QSize(2 * self.margin, 2 * self.margin)
        return size

    def _doLayout(self, rect, testOnly):
        x = rect.x()
        y = rect.y()
        lineHeight = 0

        for item in self.itemList:
            if not item.widget().isHidden():
                wid = item.widget()
                spaceX = self.spacing() + wid.style().layoutSpacing(
                    QSizePolicy.PushButton,
                    QSizePolicy.PushButton,
                    Qt.Horizontal)

                spaceY = self.spacing() + wid.style().layoutSpacing(
                    QSizePolicy.PushButton,
                    QSizePolicy.PushButton,
                    Qt.Vertical)

                nextX = x + item.sizeHint().width() + spaceX
                if nextX - spaceX > rect.right() and lineHeight > 0:
                    x = rect.x()
                    y = y + lineHeight + spaceY
                    nextX = x + item.sizeHint().width() + spaceX
                    lineHeight = 0

                if not testOnly:
                    item.setGeometry(
                        QRect(QPoint(x, y), item.sizeHint()))

                x = nextX
                lineHeight = max(lineHeight, item.sizeHint().height())

        return y + lineHeight - rect.y()

