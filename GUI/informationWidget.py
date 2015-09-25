from PyQt4 import QtGui
from bmp import BMP
from GUI.tableInfo import TableInfo


class InformationWidget(QtGui.QWidget):

    """docstring for InformationWidget"""

    def __init__(self, widget, image_path):
        super(InformationWidget, self).__init__()
        self.image_path = image_path

        self.grid = QtGui.QGridLayout(widget)
        self.grid.setColumnStretch(0, 1)
        self.grid.setColumnStretch(1, 1)

    def fill_info(self):

        self.bmp = BMP(self.image_path)

        bitmap_file_header = self.bmp.get_bitmap_file_header()
        bitmap_info = self.bmp.get_bitmap_info()
        all_list_info =\
            bitmap_file_header.get_list_info() + bitmap_info.get_list_info()

        tableInfo = TableInfo(all_list_info)

        self.grid.addWidget(tableInfo.get_table_info(), 0, 0, 2, 1)

    def fill_picture_auto(self):
        pix_map = QtGui.QPixmap(self.image_path)
        pix_map = pix_map.scaled(600, 600, 1)
        pic = QtGui.QLabel()
        pic.setPixmap(pix_map)

        self.grid.addWidget(pic, 0, 1)

    def fill_picture_per_pixel(self):
        bitmap_info = self.bmp.get_bitmap_info()
        pixel_data = self.bmp.get_pixel_data()

        width = bitmap_info.get_width().get_unpack_value()
        height = bitmap_info.get_height().get_unpack_value()
        pixel_colors_generator = pixel_data.get_pixel_color()
        addition = pixel_data.get_addition()

        image = QtGui.QImage(width, abs(height), QtGui.QImage.Format_RGB32)
        if height < 0:
            try:
                for i in range(abs(height)):
                    for j in range(width):
                        color = next(pixel_colors_generator)
                        image.setPixel(
                            j, i, QtGui.qRgb(color[2], color[1], color[0]))
                    for a in range(addition):
                        next(pixel_colors_generator)
            except StopIteration:
                for i in range(abs(height)):
                    for j in range(width):
                        color = next(pixel_colors_generator)
                        image.setPixel(
                            j, i, QtGui.qRgb(color[2], color[1], color[0]))
        try:
            for i in range(height-1, -1, -1):
                for j in range(width):
                    color = next(pixel_colors_generator)
                    image.setPixel(
                        j, i, QtGui.qRgb(color[2], color[1], color[0]))
                for a in range(addition):
                    next(pixel_colors_generator)
        except StopIteration:
            pixel_colors_generator = pixel_data.get_pixel_color()
            for i in range(height-1, -1, -1):
                for j in range(width):
                    color = next(pixel_colors_generator)
                    image.setPixel(
                        j, i, QtGui.qRgb(color[2], color[1], color[0]))

        pix_map = QtGui.QPixmap()
        pix_map.convertFromImage(image)
        pix_map = pix_map.scaled(600, 600, 1)
        pic = QtGui.QLabel()
        pic.setPixmap(pix_map)

        self.grid.addWidget(pic, 0, 1)
