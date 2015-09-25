from Structure.BitmapInfo.bitmapCoreHeader import BitmapCoreHeader
from Structure.BitmapInfo.bitmapInfoHeader import BitmapInfoHeader
from Structure.BitmapInfo.bitmapV2InfoHeader import BitmapV2InfoHeader
from Structure.BitmapInfo.bitmapV3InfoHeader import BitmapV3InfoHeader
from Structure.BitmapInfo.bitmapV4Header import BitmapV4Header
from Structure.BitmapInfo.bitmapV5Header import BitmapV5Header
from Structure.BitmapInfo.os22XBitmapHeader import Os22XBitmapHeader
from Structure.bitmapFileHeader import BitmapFileHeader
from Structure.pixelData import PixelData
from Structure.decode_bmp_rle import BI_RLE
from struct import unpack
import os
from sys import path


class NotBmpFormat(Exception):

    """path points to a file does not bmp format"""

    pass


class BMP(object):

    """creates a detailed description of the internal structure "
    "of the BMP file and image"""

    def __init__(self, path):
        super(BMP, self).__init__()
        if path[-4:] != ".bmp":
            raise NotBmpFormat("path points to a file does not bmp format")
        self._path = path
        self._byte_array = self._open(self._path)

        self._bitmap_file_header = BitmapFileHeader(self._byte_array)

        size_bitmap_info = unpack("i", self._byte_array[14:14 + 4])[0]
        self._bitmapInfo = self._get_actual_version(size_bitmap_info)
        self._bitmapInfo.fill_color_table(self._byte_array)

        self._pixel_data = PixelData(
                self._byte_array,
                self._bitmap_file_header.get_off_bits().get_unpack_value(),
                self._bitmapInfo)

        if self._bitmapInfo.get_size_header().get_unpack_value() != 12 and \
                self._bitmapInfo.get_compression().get_unpack_value() \
                in (1, 2):
            rle = BI_RLE(path)
            self._pixel_data.set_pixel_data(rle.Decode())

    def _get_actual_version(self, size):
        """returns an appropriate version of the BMP file"""
        if size == 12:
            return(BitmapCoreHeader(self._byte_array))
        elif size == 40:
            return(BitmapInfoHeader(self._byte_array))
        elif size == 52:
            return(BitmapV2InfoHeader(self._byte_array))
        elif size == 56:
            return(BitmapV3InfoHeader(self._byte_array))
        elif size == 64:
            return(Os22XBitmapHeader(self._byte_array))
        elif size == 108:
            return(BitmapV4Header(self._byte_array))
        elif size == 124:
            return(BitmapV5Header(self._byte_array))
        else:
            return(None)

    def get_pixel_data(self):
        """returns pixel data"""
        return(self._pixel_data)

    def get_color_table(self):
        """returns the color table"""
        return(self._bitmapInfo.get_color_table())

    def _open(self, path):
        """opens the file with an image"""
        with open(path, "rb") as bmpFile:
            return(bmpFile.read())

    def get_byte_array(self):
        """returns an array of bytes"""
        return(self._byte_array)

    def get_bitmap_file_header(self):
        """returns the title BMP file"""
        return(self._bitmap_file_header)

    def get_bitmap_info(self):
        """returns information about the BMP file"""
        return(self._bitmapInfo)

    @staticmethod
    def test():
        lever = False

        with open(os.path.join(path[0], "test", "coreHeader.txt")) as f:
            bmp = BMP(os.path.join(path[0], "test", "coreHeader.bmp"))
            information = bmp.get_bitmap_file_header().get_all_info() +\
                bmp.get_bitmap_info().get_all_info()
            print("Test bmp version coreHeader:")
            if information == f.read():
                print("Verification was successful")
            else:
                print("Validation fails")
                lever = True

        with open(os.path.join(path[0], "test", "infoHeader.txt")) as f:
            bmp = BMP(os.path.join(path[0], "test", "infoHeader.bmp"))
            information = bmp.get_bitmap_file_header().get_all_info() +\
                bmp.get_bitmap_info().get_all_info()
            print("Test bmp version infoHeader:")
            if information == f.read():
                print("Verification was successful")
            else:
                print("Validation fails")
                lever = True

        with open(os.path.join(path[0], "test", "os21.txt")) as f:
            bmp = BMP(os.path.join(path[0], "test", "os21.bmp"))
            information = bmp.get_bitmap_file_header().get_all_info() +\
                bmp.get_bitmap_info().get_all_info()
            print("Test bmp version os21:")
            if information == f.read():
                print("Verification was successful")
            else:
                print("Validation fails")
                lever = True

        with open(os.path.join(path[0], "test", "os22.txt")) as f:
            bmp = BMP(os.path.join(path[0], "test", "os22.bmp"))
            information = bmp.get_bitmap_file_header().get_all_info() +\
                bmp.get_bitmap_info().get_all_info()
            print("Test bmp version os22:")
            if information == f.read():
                print("Verification was successful")
            else:
                print("Validation fails")
                lever = True

        with open(os.path.join(path[0], "test", "v2header.txt")) as f:
            bmp = BMP(os.path.join(path[0], "test", "v2header.bmp"))
            information = bmp.get_bitmap_file_header().get_all_info() +\
                bmp.get_bitmap_info().get_all_info()
            print("Test bmp version v2header:")
            if information == f.read():
                print("Verification was successful")
            else:
                print("Validation fails")
                lever = True

        with open(os.path.join(path[0], "test", "v3header.txt")) as f:
            bmp = BMP(os.path.join(path[0], "test", "v3header.bmp"))
            information = bmp.get_bitmap_file_header().get_all_info() +\
                bmp.get_bitmap_info().get_all_info()
            print("Test bmp version v3header:")
            if information == f.read():
                print("Verification was successful")
            else:
                print("Validation fails")
                lever = True

        with open(os.path.join(path[0], "test", "v4header.txt")) as f:
            bmp = BMP(os.path.join(path[0], "test", "v4header.bmp"))
            information = bmp.get_bitmap_file_header().get_all_info() +\
                bmp.get_bitmap_info().get_all_info()
            print("Test bmp version v4header:")
            if information == f.read():
                print("Verification was successful")
            else:
                print("Validation fails")
                lever = True

        with open(os.path.join(path[0], "test", "v5header.txt")) as f:
            bmp = BMP(os.path.join(path[0], "test", "v5header.bmp"))
            information = bmp.get_bitmap_file_header().get_all_info() +\
                bmp.get_bitmap_info().get_all_info()
            print("Test bmp version v5header:")
            if information == f.read():
                print("Verification was successful")
            else:
                print("Validation fails")
                lever = True

        with open(os.path.join(
                path[0], "test", "pixelDataInfoHeader.txt")) as f:
            bmp = BMP(os.path.join(path[0], "test", "infoHeader.bmp"))
            pixelData = str(bmp.get_pixel_data().get_pixel_data())
            print("Test bmp pixelData:")
            if pixelData == f.read():
                print("Verification was successful")
            else:
                print("Validation fails")
                lever = True
        print("Complete test")

        return lever
