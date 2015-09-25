from Structure.BitmapInfo.bitmapV4Header import BitmapV4Header
from Structure.info import Info


class BitmapV5Header(BitmapV4Header):

    """docstring for BitmapV5Header"""

    def __init__(self, byte_array):
        super(BitmapV5Header, self).__init__(byte_array)
        self._intent = Info(
            "bV5Intent", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "The preferences when rendering raster")
        self._offset += 4
        self._profile_data = Info(
            "bV5ProfileData", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "The offset in bytes from "
            "the beginning of the color profile BITMAPINFO")
        self._offset += 4
        self._profile_size = Info(
            "bV5ProfileSize", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "If the BMP is directly "
            "included a color profile, here indicated by its size in bytes")
        self._offset += 4
        self._reserved = Info(
            "bV5Reserved", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "Reserved and must be reset")
        self._offset += 4

    def get_list_info(self):
        list_fields = [
            self._intent, self._profile_data, self._profile_size,
            self._reserved]
        return(super(BitmapV5Header, self).get_list_info() + list_fields)

    def get_all_info(self):
        info_field = ''.join(
            map(lambda x: x.get_all_data(), self.get_list_info()))
        return(info_field)

    def get_intent(self):
        return(self._intent)

    def get_profile_data(self):
        return(self._profile_data)

    def get_profile_size(self):
        return(self._profile_size)

    def get_reserved(self):
        return(self._reserved)
