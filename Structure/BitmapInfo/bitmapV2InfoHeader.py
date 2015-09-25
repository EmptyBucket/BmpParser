from Structure.BitmapInfo.bitmapInfoHeader import BitmapInfoHeader
from Structure.info import Info


class BitmapV2InfoHeader(BitmapInfoHeader):

    """docstring for BitmapV2InfoHeader"""

    def __init__(self, byte_array):
        super(BitmapV2InfoHeader, self).__init__(byte_array)
        self._red_mask = Info(
            "bV2RedMask", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "Bit mask to extract the "
            "intensity of the red channel values")
        self._offset += 4
        self._green_mask = Info(
            "bV2GreenMask", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "Bit mask to extract the "
            "intensity of the green channel values")
        self._offset += 4
        self._blue_mask = Info(
            "bV2BlueMask", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "Bit mask to extract the "
            "intensity of the blue channel values")
        self._offset += 4

    def get_list_info(self):
        list_fields = [self._red_mask, self._green_mask, self._blue_mask]
        return(super(BitmapV2InfoHeader, self).get_list_info() + list_fields)

    def get_all_info(self):
        info_field = ''.join(
            map(lambda x: x.get_all_data(), self.get_list_info()))
        return(info_field)

    def get_red_mask(self):
        return(self._red_mask)

    def get_green_mask(self):
        return(self._green_mask)

    def get_blue_mask(self):
        return(self._blue_mask)
