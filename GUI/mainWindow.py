from PyQt4 import QtGui, QtCore
import os.path
from GUI.informationWidget import InformationWidget


class MainWindow(QtGui.QMainWindow):

    def __init__(self, no_auto):
        super(MainWindow, self).__init__()

        self.no_auto = no_auto
        self.setWindowTitle('BMP')
        self.setFixedSize(1200, 700)

        open_file = QtGui.QAction('Open', self)
        open_file.setShortcut('Ctrl+O')
        open_file.setStatusTip('Open new File')
        self.connect(open_file, QtCore.SIGNAL('triggered()'), self.show_dialog)

        exit = QtGui.QAction("Exit", self)
        exit.setShortcut("Ctrl+Q")
        exit.setStatusTip("Exit program")
        self.connect(
            exit, QtCore.SIGNAL("triggered()"), QtCore.SLOT("close()"))

        menu_bar = self.menuBar()
        file = menu_bar.addMenu('&File')
        file.addAction(open_file)
        file.addAction(exit)

    def show_dialog(self):
        file_path = QtGui.QFileDialog.getOpenFileName(
            self, 'Open file', '/home')
        if file_path is not None and os.path.isfile(file_path):
            self.view_data_image(file_path)

    def view_data_image(self, file_path):
        widget = QtGui.QWidget()
        self.setCentralWidget(widget)
        information_widget = InformationWidget(widget, file_path)
        information_widget.fill_info()
        if self.no_auto:
            information_widget.fill_picture_per_pixel()
        else:
            information_widget.fill_picture_auto()
