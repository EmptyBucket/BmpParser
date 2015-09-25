from Structure.info import Info


class BitmapFileHeader(Info):

    """docstring for BitmapFileHeader"""

    def __init__(self, byte_array):
        self._offset = 0
        super(BitmapFileHeader, self).__init__(
            "BitmapFileHeader", None, self._offset, None,
            "To store general information about the Bitmap Image File")
        self._type = Info(
            "bfType", byte_array[self._offset:self._offset + 2],
            self._offset, 2, "The header field used to identify "
            "the BMP & DIB file is 0x42 0x4D in hexadecimal, "
            "same as BM in ASCII."
            "The following entries are possible:"
            "BM - Windows 3.1x, 95, NT, ... etc; "
            "BA - OS/2 struct Bitmap Array; "
            "CI - OS/2 struct Color Icon; "
            "CP - OS/2 const Color Pointer; "
            "IC - OS/2 struct Icon; "
            "PT - OS/2 Pointer")
        self._offset += 2
        self._sizeFile = Info(
            "bfSize", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "The size of the BMP file in bytes")
        self._offset += 4
        self._reserver1 = Info(
            "bfReserved1", byte_array[self._offset:self._offset + 2],
            self._offset, 2, "Reserved; actual value depends "
            "on the application that creates the image")
        self._offset += 2
        self._reserver2 = Info(
            "bfReserved2", byte_array[self._offset:self._offset + 2],
            self._offset, 2, "Reserved; actual value depends on "
            "the application that creates the image")
        self._offset += 2
        self._offBits = Info(
            "bfOffBits", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "The offset, i.e. starting address, "
            "of the byte where the bitmap image data "
            "(pixel array) can be found")
        self._offset += 4

    def get_list_info(self):
        return([
            self, self._type, self._sizeFile, self._reserver1, self._reserver2,
            self._offBits])

    def get_all_info(self):
        info_fields = ''.join(
            map(lambda x: x.get_all_data(), self.get_list_info()))
        return(info_fields)

    def get_name(self):
        return(self._name)

    def get_address(self):
        return(self._address)

    def get_type(self):
        return(self._type)

    def get_size(self):
        return(self._sizeFile)

    def get_reserver1(self):
        return(self._reserver1)

    def get_reserver2(self):
        return(self._reserver2)

    def get_off_bits(self):
        return(self._offBits)
