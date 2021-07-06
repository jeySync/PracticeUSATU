import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QOpenGLWidget, QWidget, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QColorDialog, \
    QMainWindow, QFormLayout, QGroupBox, QLabel, QScrollArea, QFileDialog
from PyQt5.QtGui import QPainter, QColor, QFont, QPixmap, QPen
from PyQt5.QtCore import Qt, QPoint, QRect, QLineF, pyqtSignal
from Form import Ui_MainWindow


class Communicate():
    updateWidget = pyqtSignal(int)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.widget = DrawingScene()
        self.widget.add_functions(self.ui)
        #self.setCentralWidget(self.widget)
        scroll = QtWidgets.QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.widget)
        self.setCentralWidget(scroll)


class DrawingScene(QWidget):
    def __init__(self):
        super().__init__()
        self.tools = {}
        # self.tools["fill"]=ControllerFill(self)
        # self.tools["change_color"]=ControllerChangeColor(self)
        self.brush_color = QColor(255, 255, 255)
        self.file_path = ''
        self.line_color = QColor(0, 0, 0)
        self.color = QColor(0, 0, 0)
        self.shapes = list()
        self.excretion_coords = False
        self.main_area = QPixmap(self.rect().size())
        self.main_area.fill(Qt.white)
        self.external_area = QPixmap(self.rect().size())
        self.external_area.fill(QColor(0, 0, 0, 0))
        self.begin = QPoint()
        self.destination = QPoint()
        self.undo_redo = ControllerUndoRedo(self)
        self.current_tool = Controller(self)
        self.tools["rectangle"] = ControllerShape(self, "rectangle")
        self.tools["ellips"] = ControllerShape(self, "ellips")
        self.tools["line"] = ControllerShape(self, "line")
        self.tools["move"] = ControllerMove(self)
        self.tools["select"] = ControllerSelect(self)
        self.tools["accidentalClick"] = ControllerAccidentalClick(self)
        self.tools["fill"] = ControllerFill(self)

    def redrawing_scene(self):
        painter = QPainter(self)
        painter.drawPixmap(QPoint(), self.main_area)
        painter.drawPixmap(QPoint(), self.external_area)

    def add_functions(self, ui):
        ui.actionRectangle.triggered.connect(lambda: self.change_tool("rectangle"))
        ui.actionEllips.triggered.connect(lambda: self.change_tool("ellips"))
        ui.lineAction.triggered.connect(lambda: self.change_tool("line"))
        # self.ui.actionPalette.triggered.connect(lambda: self.change_tool("change_color"))
        ui.selectAction.triggered.connect(lambda: self.change_tool("select"))
        ui.moveAction.triggered.connect(lambda: self.change_tool("move"))
        ui.fillAction.triggered.connect(lambda: self.tools["fill"].fill(self.color))
        ui.actionPalette.triggered.connect(lambda:self.change_color(ui))
        ui.actionCleanWindow.triggered.connect(self.clean_window)
        ui.undoAction.triggered.connect(self.undo_redo.undo_redo_stack.undo)
        ui.redoAction.triggered.connect(self.undo_redo.undo_redo_stack.redo)
        ui.changeSizeAction.triggered.connect(self.change_scene_size)
        ui.saveAction.triggered.connect(self.fileSave)
        ui.saveAsAction.triggered.connect(self.fileSaveAs)
        ui.loadAction.triggered.connect(self.fileLoad)

    def fileLoad(self):
        file = QFileDialog.getOpenFileName(self, "", "", "*.png;;*.jpg")
        self.file_path = file

        if not self.file_path == '':
            l = self.file_path[0].split('.')
            print(l[-1])
            self.main_area.load(self.file_path[0], l[-1])

    def fileSave(self):
        if self.file_path == '':
            self.fileSaveAs()
        else:
            l = self.file_path[0].split('.')
            print(l[-1])
            self.main_area.save(self.file_path[0], l[-1])

    def fileSaveAs(self):
        file = QFileDialog.getSaveFileName(self, "", "untitled.png", "*.png;;*.jpg;;*.*")
        # print(QtGui.QImageWriter.supportedImageFormats())
        if not file == '':
            self.file_path = file
            self.fileSave()

    def change_tool(self, name_of_tool):
        self.current_tool = self.tools[name_of_tool]

    def change_scene_size(self,):
        self.setFixedWidth(250)
        self.setFixedHeight(250)

    def change_color(self,ui):
        color = QColorDialog.getColor()
        self.color = color
        icon_pix = QPixmap(self.rect().size())
        icon_pix.fill(color)
        ui.paletteIcon.addPixmap(QtGui.QPixmap(icon_pix), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ui.actionPalette.setIcon(ui.paletteIcon)

    def clean_window(self):
        self.main_area.fill(Qt.white)
        self.external_area.fill(QColor(0, 0, 0, 0))
        self.update()
        self.shapes.clear()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(QPoint(), self.main_area)
        painter.drawPixmap(QPoint(), self.external_area)

    def mousePressEvent(self, event):
        # fill_control=ControllerFill(self)
        if event.buttons() & Qt.LeftButton:
            self.current_tool.mouse_press_handler(event)

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.current_tool.mouse_move_handler(event)

    def mouseReleaseEvent(self, event):
        self.current_tool.mouse_release_handler(event)


if __name__ == "__main__":
    from Controllers import *
    import sys

    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
