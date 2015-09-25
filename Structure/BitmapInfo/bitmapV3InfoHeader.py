from Structure.BitmapInfo.bitmapV2InfoHeader import BitmapV2InfoHeader
from Structure.info import Info


class BitmapV3InfoHeader(BitmapV2InfoHeader):

    """docstring for BitmapV3InfoHeader"""

    def __init__(self, byte_array):
        super(BitmapV3InfoHeader, self).__init__(byte_array)
        self._alpha_mask = Info(
            "bV3AlphaMask", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "Bit mask to extract the "
            "intensity of the alpha channel values")
        self._offset += 4

    def get_list_info(self):
        list_fields = [self._alpha_mask]
        return(super(BitmapV3InfoHeader, self).get_list_info() + list_fields)

    def get_all_info(self):
        info_field = ''.join(
            map(lambda x: x.get_all_data(), self.get_list_info()))
        return(info_field)

    def get_alpha_mask(self):
        return(self._alpha_mask)
