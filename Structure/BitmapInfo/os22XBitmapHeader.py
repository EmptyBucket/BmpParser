from Structure.BitmapInfo.bitmapInfoHeader import BitmapInfoHeader
from Structure.info import Info


class Os22XBitmapHeader(BitmapInfoHeader):

    """docstring for Os22XBitmapHeader"""

    def __init__(self, byte_array):
        super(Os22XBitmapHeader, self).__init__(byte_array)
        self._units = Info(
            "osUnits", byte_array[self._offset:self._offset + 2],
            self._offset, 2, "Type of units used to measure resolution")
        self._offset += 2
        self._reserved = Info(
            "osReserved", byte_array[self._offset:self._offset + 2],
            self._offset, 2, "Pad structure to 4-byte boundary")
        self._offset += 2
        self._recording = Info(
            "osRecording", byte_array[self._offset:self._offset + 2],
            self._offset, 2, "Recording algorithm")
        self._offset += 2
        self._rendering = Info(
            "osRendering", byte_array[self._offset:self._offset + 2],
            self._offset, 2, "Halftoning algorithm used")
        self._offset += 2
        self._size1 = Info(
            "osSize1", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "Reserved for halftoning algorithm use")
        self._offset += 4
        self._size2 = Info(
            "osSize2", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "Reserved for halftoning algorithm use")
        self._offset += 4
        self._color_encoding = Info(
            "osColorEncoding", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "Color model used in bitmap")
        self._offset += 4
        self._identified = Info(
            "osIdentified", byte_array[self._offset:self._offset + 4],
            self._offset, 4, "Reserved for application use")
        self._offset += 4

    def get_list_info(self):
        list_fields = [
            self._units, self._reserved, self._recording, self._rendering,
            self._size1, self._size2, self._color_encoding, self._identified]
        return(super(Os22XBitmapHeader, self).get_list_info() + list_fields)

    def get_all_info(self):
        info_field = ''.join(
            map(lambda x: x.get_all_data(), self.get_list_info()))
        return(info_field)

    def get_units(self):
        return(self._units)

    def get_reserved(self):
        return(self._reserved)

    def get_recording(self):
        return(self._recording)

    def get_rendering(self):
        return(self._rendering)

    def get_size1(self):
        return(self._size1)

    def get_size2(self):
        return(self._size2)

    def get_color_encodeing(self):
        return(self._color_encoding)

    def get_indentifier(self):
        return(self._identified)
