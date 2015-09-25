from Structure.BitmapInfo.bitmapInfo import BitmapInfo
from Structure.info import Info


class BitmapCoreHeader(BitmapInfo):

    """docstring for BitmapCoreHeader"""

    def __init__(self, byte_array):
        super(BitmapCoreHeader, self).__init__(byte_array)
        self._width = Info(
            "bcWidth", byte_array[self._offset:self._offset + 2], self._offset,
            2, "The bitmap width in pixels (signed integer)")
        self._offset += 2
        self._height = Info(
            "bcHeight", byte_array[self._offset:self._offset + 2],
            self._offset, 2, "The bitmap height in pixels (signed integer)")
        self._offset += 2
        self._planes = Info(
            "bcPlanes", byte_array[self._offset:self._offset + 2], 2,
            self._offset, "The number of color planes must be 1")
        self._offset += 2
        self._bit_count = Info(
            "bcBitCount", byte_array[self._offset:self._offset + 2], 2,
            self._offset, "The number of bits per pixel, which is the color "
            "depth of the image. Typical values are 1, 4, 8, 16, 24 and 32")
        self._offset += 2

    def get_list_info(self):
        return(super(BitmapCoreHeader, self).get_list_info())

    def get_all_info(self):
        return(super(BitmapCoreHeader, self).get_all_info())

    def fill_color_table(self, byte_array):
        bytes_per_cell = 3

        if self._bit_count.get_unpack_value() <= 8:
            value_cell = 2**self._bit_count.get_unpack_value() * bytes_per_cell

            self._color_table = \
                byte_array[self._offset:self._offset + value_cell]
            self._color_table = \
                list(zip(*[iter(self._color_table)] * bytes_per_cell))
        else:
            self._color_table = None
