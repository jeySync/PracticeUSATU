from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QOpenGLWidget, QWidget, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QFont, QPixmap
from PyQt5.QtCore import Qt, QPoint, QRect
import Resources.Icons


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.window_width, self.window_height = 800, 480
        MainWindow.setMinimumSize(self.window_width, self.window_height)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionEllips = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ToolBar/ellips.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEllips.setIcon(icon)
        self.actionEllips.setObjectName("actionEllips")

        self.actionRectangle = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ToolBar/rect.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRectangle.setIcon(icon1)
        self.actionRectangle.setObjectName("actionRectangle")

        icon_pix = QPixmap(MainWindow.rect().size())
        self.actionPaletteLine = QtWidgets.QAction(MainWindow)
        self.icon2 = QtGui.QIcon()
        self.icon2.addPixmap(QtGui.QPixmap(icon_pix), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaletteLine.setIcon(self.icon2)
        self.actionPaletteLine.setObjectName("actionPalette")

        self.actionPaletteBrush = QtWidgets.QAction(MainWindow)
        self.icon3 = QtGui.QIcon()
        self.icon3.addPixmap(QtGui.QPixmap(icon_pix), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaletteBrush.setIcon(self.icon3)
        self.actionPaletteBrush.setObjectName("highlight")


        self.actionChooseShape = QtWidgets.QAction(MainWindow)
        self.chooseIcon = QtGui.QIcon()
        self.chooseIcon.addPixmap(QtGui.QPixmap(":/ToolBar/choose.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionChooseShape.setIcon(self.chooseIcon)
        self.actionChooseShape.setObjectName("chooseShape")

        self.actionCleanWindow = QtWidgets.QAction(MainWindow)
        self.cleanIcon = QtGui.QIcon()
        self.cleanIcon.addPixmap(QtGui.QPixmap(":/ToolBar/clean.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCleanWindow.setIcon(self.cleanIcon)
        self.actionCleanWindow.setObjectName("chooseShape")

        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.actionEllips)
        self.toolBar.addAction(self.actionRectangle)
        self.toolBar.addAction(self.actionPaletteLine)
        self.toolBar.addAction(self.actionPaletteBrush)
        self.toolBar.addAction(self.actionChooseShape)
        self.toolBar.addAction(self.actionCleanWindow)
        layout = QVBoxLayout()
        MainWindow.setLayout(layout)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
       # self.actionRectangle.setText(_translate("MainWindow", "Rectangle"))
      #  self.actionRectangle.setText(_translate("MainWindow", "Rectangle"))
       # self.actionEllips.setText(_translate("MainWindow", "Ellips"))
       # self.actionEllips.setToolTip(_translate("MainWindow", "Ellips"))
       # self.actionChangeColor.setText(_translate("MainWindow", "ChangeColor"))
       # self.actionChangeColor.setToolTip(_translate("MainWindow", "ChangeColor"))