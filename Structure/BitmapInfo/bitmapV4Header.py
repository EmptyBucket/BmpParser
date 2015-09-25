from Structure.BitmapInfo.bitmapV3InfoHeader import BitmapV3InfoHeader
from Structure.info import Info


class BitmapV4Header(BitmapV3InfoHeader):

    """docstring for BitmapV4Header"""

    def __init__(self, byte_array):
        super(BitmapV4Header, self).__init__(byte_array)
        self._cs_type = Info(
            "bV4CSType", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "Type color space")
        self._offset += 4
        self._end_points = Info(
            "bV4Endpoints", byte_array[self._offset:self._offset + 36],
            self._offset, 36, "36-byte field is a structure "
            "EndPoints CIEXYZTRIPLE, which consists of three "
            "fields ciexyzRed (endpoint red), ciexyzGreen (green dot) "
            "and ciexyzBlue (blue). These three fields in turn are "
            "also the structures CIEXYZ with three fields ciexyzX, "
            "ciexyzY and ciexyzZ type FXPT2DOT30. PXPT2DOT30 - a "
            "32-bit unsigned fixed-point number, in which the two "
            "most significant bits are allocated to the integer "
            "part and 30 junior - under fractional.")
        self._offset += 36
        self._gamma_red = Info(
            "bV4GammaRed", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "The red color correction")
        self._offset += 4
        self._gamma_green = Info(
            "bV4GammaGreen", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "The green color correction")
        self._offset += 4
        self._gamma_blue = Info(
            "bV4GammaBlue", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "The blue color correction")
        self._offset += 4

    def get_list_info(self):
        list_fields = [
            self._cs_type, self._end_points, self._gamma_red,
            self._gamma_green, self._gamma_blue]
        return(super(BitmapV4Header, self).get_list_info() + list_fields)

    def get_all_info(self):
        info_field = ''.join(
            map(lambda x: x.get_all_data(), self.get_list_info()))
        return(info_field)

    def get_cs_type(self):
        return(self._cs_type)

    def get_endpoints(self):
        return(self._end_points)

    def get_gamma_red(self):
        return(self._gamma_red)

    def get_gamma_green(self):
        return(self._gamma_green)

    def get_gamma_blue(self):
        return(self._gamma_blue)
