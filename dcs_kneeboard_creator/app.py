import os
# import ez_qt

from PySide6.QtWidgets import *
from PySide6.QtGui import *

from dcs_kneeboard_creator import kneeboard_creator_window

application = QApplication()

def main():
    # ez_qt.app_colors.set_dark_theme(qApp, accent_color=ez_qt.k.AccentColors.medium_blue)
    splash_pixmap = QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "ui", "icons", "splashscreen.png"))
    splash_screen = QSplashScreen(splash_pixmap)
    splash_screen.show()

    qApp.processEvents()

    window = kneeboard_creator_window.KneeboardCreatorWindow()

    # window.showMaximized()
    window.show()
    splash_screen.finish(window)

    qApp.exec_()

if __name__ == "__main__":
    main()