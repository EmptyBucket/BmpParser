from abc import ABCMeta, abstractmethod
from Structure.info import Info


class BitmapInfo(Info):

    """docstring for BitmapInfo"""

    __metaclass__ = ABCMeta

    def __init__(self, byte_array):
        self._offset = 14
        super(BitmapInfo, self).__init__(
            "BitmapInfo", None, self._offset, None,
            "To store detailed information about the "
            "bitmap image and define the pixel format")
        self._size_header = Info(
            "bcSize", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "The size of this header")
        self._offset += 4
        version = {
            12: "BITMAPCORE||OS21XHEADER",
            40: "BITMAPINFOHEADER",
            52: "BITMAPV2INFOHEADER",
            56: "BITMAPV3INFOHEADER",
            64: "OS22XBITMAPHEADER",
            108: "BITMAPV4HEADER",
            124: "BITMAPV5HEADER"}[self._size_header.get_unpack_value()]
        self._version = Info(
            "Version", version, None, None, None)

    def get_list_info(self):
        return([
            self, self._version, self._size_header, self._width, self._height,
            self._planes, self._bit_count])

    def get_all_info(self):
        info_field = ''.join(map(
            lambda x: x.get_all_data(), self.get_list_info()))
        return(info_field)

    @abstractmethod
    def fill_color_table(self, byte_array):
        pass

    def get_color_table(self):
        return(self._color_table)

    def get_size_header(self):
        return(self._size_header)

    def get_version(self):
        return(self._version)

    def get_width(self):
        return(self._width)

    def get_height(self):
        return(self._height)

    def get_planes(self):
        return(self._planes)

    def get_bit_count(self):
        return(self._bit_count)
