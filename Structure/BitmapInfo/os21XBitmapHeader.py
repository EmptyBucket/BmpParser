from Structure.BitmapInfo.bitmapInfo import BitmapInfo
from Structure.info import Info


class Os21XBitmapHeader(BitmapInfo):

    """docstring for Os21XBitmapHeader"""

    def __init__(self, byte_array):
        super(Os21XBitmapHeader, self).__init__(byte_array)
        self._width = Info(
            "osWidth", byte_array[self._offset:self._offset + 2],
            self._offset, 2, "The bitmap width in pixels (unsigned 16bit)")
        self._offset += 2
        self.height = Info(
            "osHeight", byte_array[self._offset:self._offset + 2],
            self._offset, 2, "The bitmap height in pixels (unsigned 16bit)")
        self._offset += 2
        self._planes = Info(
            "osPlanes", byte_array[self._offset:self._offset + 2],
            self._offset, 2, "The number of color planes must be 1")
        self._offset += 2
        self._bit_count = Info(
            "osBitCount", byte_array[self._offset:self._offset + 2],
            self._offset, 2, "the number of bits per pixel")
        self._offset += 2

    def get_list_info(self):
        return(super(Os21XBitmapHeader, self).get_list_info())

    def get_all_info(self):
        return(super(Os21XBitmapHeader, self).get_all_info())

    def fill_Color_Table(self):
        self._color_table = None
