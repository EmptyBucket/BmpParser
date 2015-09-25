from Structure.BitmapInfo.bitmapInfo import BitmapInfo
from Structure.info import Info


class BitmapInfoHeader(BitmapInfo):

    """docstring for BitmapInfoHeader"""

    def __init__(self, byte_array):
        super(BitmapInfoHeader, self).__init__(byte_array)
        self._width = Info(
            "biWidth", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "The bitmap width in pixels (signed integer)")
        self._offset += 4
        self._height = Info(
            "biHeight", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "The bitmap height in pixels (signed integer)")
        self._offset += 4
        self._planes = Info(
            "biPlanes", byte_array[self._offset:self._offset + 2],
            self._offset, 2, "The number of color planes must be 1")
        self._offset += 2
        self._bit_count = Info(
            "biBitCount", byte_array[self._offset:self._offset + 2],
            self._offset, 2, "The number of bits per pixel, which is the "
            "color depth of the image. Typical values are 1, 4, 8, 16, 24"
            " and 32")
        self._offset += 2
        self._compression = Info(
            "biCompression", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "The compression method being used. See the next "
            "table for a list of possible values")
        self._offset += 4
        self._size_image = Info(
            "biSizeImage", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "The image size. This is the size of the"
            " raw bitmap data; a dummy 0 can be given for BI_RGB bitmaps")
        self._offset += 4
        self._x_pels_per_meter = Info(
            "biXPelsPerMeter", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "The horizontal resolution of the image. "
            "(pixel per meter, signed integer)")
        self._offset += 4
        self._y_pels_per_meter = Info(
            "biYPelsPerMeter", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "The vertical resolution of the "
            "image. (pixel per meter, signed integer)")
        self._offset += 4
        self._clr_used = Info(
            "biClrUsed", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "The number of colors in the color "
            "palette, or 0 to default to 2^n")
        self._offset += 4
        self._clr_important = Info(
            "biClrImportant", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "The number of important colors used, "
            "or 0 when every color is important; generally ignored")
        self._offset += 4

    def get_list_info(self):
        list_fields = [
            self._compression, self._size_image, self._x_pels_per_meter,
            self._y_pels_per_meter, self._clr_used, self._clr_important]
        return(super(BitmapInfoHeader, self).get_list_info() + list_fields)

    def get_all_info(self):
        info_field = ''.join(
            map(lambda x: x.get_all_data(), self.get_list_info()))
        return(info_field)

    def get_compression(self):
        return(self._compression)

    def get_size_bitmap(self):
        return(self._size_image)

    def get_x_pels_per_meter(self):
        return(self._x_pels_per_meter)

    def get_y_pels_per_meter(self):
        return(self._y_pels_per_meter)

    def get_clr_used(self):
        return(self._clr_used)

    def get_clr_important(self):
        return(self._clr_important)

    def fill_color_table(self, byte_array):
        bytes_per_cell = 4
        value_cell = 0

        if self._bit_count.get_unpack_value() <= 8 or \
                self._bit_count.get_unpack_value() >= 8 and \
                self._clr_used.get_unpack_value() != 0:
            if self._bit_count.get_unpack_value() <= 8:
                if self._clr_used.get_unpack_value() == 0:
                    value_cell = \
                        2**self._bit_count.get_unpack_value() * \
                            bytes_per_cell
                else:
                    value_cell = \
                        self._clr_used.get_unpack_value() * bytes_per_cell
            elif self._bit_count.get_unpack_value() >= 8 and \
                    self._clr_used.get_unpack_value() != 0:
                value_cell = \
                    self._clr_used.get_unpack_value() * bytes_per_cell

            self._color_table = \
                byte_array[self._offset:self._offset + value_cell]
            self._color_table = \
                list(zip(*[iter(self._color_table)] * bytes_per_cell))
            if self._clr_important.get_unpack_value() != 0:
                self._color_table = self._color_table[:self._clr_important]
        else:
            self._color_table = None
