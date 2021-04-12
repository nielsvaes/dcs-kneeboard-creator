# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kneeboard_creator.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_kneeboard_creator_window(object):
    def setupUi(self, kneeboard_creator_window):
        if not kneeboard_creator_window.objectName():
            kneeboard_creator_window.setObjectName(u"kneeboard_creator_window")
        kneeboard_creator_window.resize(1098, 744)
        self.men_new_layer = QAction(kneeboard_creator_window)
        self.men_new_layer.setObjectName(u"men_new_layer")
        self.men_new_layer.setShortcutContext(Qt.ApplicationShortcut)
        self.centralwidget = QWidget(kneeboard_creator_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splt_view_tools = QSplitter(self.centralwidget)
        self.splt_view_tools.setObjectName(u"splt_view_tools")
        self.splt_view_tools.setOrientation(Qt.Horizontal)
        self.frm_view = QFrame(self.splt_view_tools)
        self.frm_view.setObjectName(u"frm_view")
        self.frm_view.setFrameShape(QFrame.StyledPanel)
        self.frm_view.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frm_view)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.view_layout = QVBoxLayout()
        self.view_layout.setObjectName(u"view_layout")

        self.verticalLayout_3.addLayout(self.view_layout)

        self.splt_view_tools.addWidget(self.frm_view)
        self.frm_tools_layers = QFrame(self.splt_view_tools)
        self.frm_tools_layers.setObjectName(u"frm_tools_layers")
        self.frm_tools_layers.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frm_tools_layers)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.splt_tools_layers = QSplitter(self.frm_tools_layers)
        self.splt_tools_layers.setObjectName(u"splt_tools_layers")
        self.splt_tools_layers.setOrientation(Qt.Vertical)
        self.frm_tools = QFrame(self.splt_tools_layers)
        self.frm_tools.setObjectName(u"frm_tools")
        self.frm_tools.setFrameShape(QFrame.StyledPanel)
        self.frm_tools.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frm_tools)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tools_layout = QVBoxLayout()
        self.tools_layout.setObjectName(u"tools_layout")

        self.verticalLayout_4.addLayout(self.tools_layout)

        self.splt_tools_layers.addWidget(self.frm_tools)
        self.frmlayers = QFrame(self.splt_tools_layers)
        self.frmlayers.setObjectName(u"frmlayers")
        self.frmlayers.setFrameShape(QFrame.StyledPanel)
        self.frmlayers.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frmlayers)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.layer_layout = QVBoxLayout()
        self.layer_layout.setObjectName(u"layer_layout")

        self.verticalLayout_6.addLayout(self.layer_layout)

        self.splt_tools_layers.addWidget(self.frmlayers)

        self.verticalLayout_7.addWidget(self.splt_tools_layers)

        self.splt_view_tools.addWidget(self.frm_tools_layers)

        self.gridLayout.addWidget(self.splt_view_tools, 0, 0, 1, 1)

        kneeboard_creator_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(kneeboard_creator_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1098, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuLayer = QMenu(self.menubar)
        self.menuLayer.setObjectName(u"menuLayer")
        kneeboard_creator_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(kneeboard_creator_window)
        self.statusbar.setObjectName(u"statusbar")
        kneeboard_creator_window.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuLayer.menuAction())
        self.menuLayer.addAction(self.men_new_layer)

        self.retranslateUi(kneeboard_creator_window)

        QMetaObject.connectSlotsByName(kneeboard_creator_window)
    # setupUi

    def retranslateUi(self, kneeboard_creator_window):
        kneeboard_creator_window.setWindowTitle(QCoreApplication.translate("kneeboard_creator_window", u"DCS World Kneeboard Creator by Coconut Cockpit", None))
        self.men_new_layer.setText(QCoreApplication.translate("kneeboard_creator_window", u"New layer", None))
#if QT_CONFIG(shortcut)
        self.men_new_layer.setShortcut(QCoreApplication.translate("kneeboard_creator_window", u"F3", None))
#endif // QT_CONFIG(shortcut)
        self.menuFile.setTitle(QCoreApplication.translate("kneeboard_creator_window", u"File", None))
        self.menuLayer.setTitle(QCoreApplication.translate("kneeboard_creator_window", u"Layer", None))
    # retranslateUi

