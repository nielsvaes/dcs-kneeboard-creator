from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


from ez_settings import EZSettings

class BoardView(QGraphicsView):
    def __init__(self, scene, parent):
        super().__init__(parent)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        self.setObjectName("View")
        self.setBackgroundBrush(QBrush(QColor(60, 60, 60)))
        self.setScene(scene)

        self.zoom = 0

        self.setDragMode(QGraphicsView.RubberBandDrag)

        self.scale(1, 1)

        font = QFont()
        font.setPointSize(8)
        font.setItalic(True)
        font.setFamily("sans-serif")
        self.title_label = QLabel("DCS World Kneeboard creator by Coconut Cockpit")
        self.title_label.setFont(font)
        self.title_label.setScaledContents(True)

        self.info_label = InfoLabel("")

        self.grid_layout = QGridLayout(self)
        self.grid_layout.setContentsMargins(30, 30, 30, 30)
        self.grid_layout.addWidget(self.info_label, 0, 0, 0, 0, Qt.AlignTop | Qt.AlignCenter)

    def mousePressEvent(self, event):
        if event.button() == Qt.MiddleButton:
            release_event = QMouseEvent(QEvent.MouseButtonRelease, event.localPos(), event.screenPos(),
                                        Qt.LeftButton, Qt.NoButton, event.modifiers())
            super().mouseReleaseEvent(release_event)
            self.setDragMode(QGraphicsView.ScrollHandDrag)
            fake_event = QMouseEvent(event.type(), event.localPos(), event.screenPos(),
                                     Qt.LeftButton, event.buttons() | Qt.LeftButton, event.modifiers())
            super().mousePressEvent(fake_event)
        else:
            event.accept()
            super(BoardView, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MiddleButton:
            fakeEvent = QMouseEvent(event.type(), event.localPos(), event.screenPos(),
                                    Qt.LeftButton, event.buttons() & ~Qt.LeftButton, event.modifiers())
            super().mouseReleaseEvent(fakeEvent)
            self.setDragMode(QGraphicsView.RubberBandDrag)
        else:
            event.accept()
            super(BoardView, self).mouseReleaseEvent(event)

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.zoom += 1
            self.scale(1.1, 1.1)
        else:
            self.zoom -= 1
            self.scale(0.9, 0.9)




class StyleSheets:
    normal = "background-color: rgb(76, 76, 76); border-radius: 10px; padding: 10px"
    error = "background-color: rgb(200, 76, 76); border-radius: 10px; padding: 10px"
    success = "background-color: rgb(76, 150, 76); border-radius: 10px; padding: 10px"
    warning = "background-color: rgb(191, 176, 59); border-radius: 10px; padding: 10px; color: rgb(0, 0, 0);"

class InfoLabel(QLabel):
    def __init__(self, text, fade_time=500, stay_time=2000):
        super().__init__(text)
        self.__fade_time = fade_time
        self.__fade_effect = QGraphicsOpacityEffect()
        self.__animation = QPropertyAnimation(self.__fade_effect, QByteArray(b"opacity"))
        self.__animation.setDuration(self.__fade_time)

        self.__stay_time = fade_time + stay_time

        self.__timer = QTimer()
        self.__timer.timeout.connect(self.__fade_out)
        self.__time_has_finished = True

        self.setGraphicsEffect(self.__fade_effect)

    def show_message(self, status, text):
        if status == "error":
            self.error(text)
        elif status == "success":
            self.success(text)
        elif status == "warning":
            self.warning(text)
        else:
            self.info(text)

    def info(self, text):
        self.setStyleSheet(StyleSheets.normal)
        self.setText(text)
        self.__fade_in()

    def error(self, text):
        self.setStyleSheet(StyleSheets.error)
        self.setText(text)
        self.__fade_in()

    def success(self, text):
        self.setStyleSheet(StyleSheets.success)
        self.setText(text)
        self.__fade_in()

    def warning(self, text):
        self.setStyleSheet(StyleSheets.warning)
        self.setText(text)
        self.__fade_in()

    def __fade_in(self):
        self.__animation.setStartValue(0.0)
        self.__animation.setEndValue(1.0)
        self.__animation.setEasingCurve(QEasingCurve.Linear)
        self.__animation.start()

        self.__timer.start(self.__stay_time)

    def __fade_out(self):
        self.__animation.setStartValue(1.0)
        self.__animation.setEndValue(0.0)
        self.__animation.setEasingCurve(QEasingCurve.Linear)
        self.__animation.start()
        self.__timer.stop()





