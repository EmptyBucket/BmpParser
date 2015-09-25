def get_bit(byte, index):
        """returns the number of bits"""
        bit = int(byte & 1 << index != 0)
        return bit


def bytes_to_bits(array_byte):
    list_bit = []
    for i in array_byte:
        for j in range(7, -1, -1):
            list_bit.append(get_bit(i, j))
    return list_bit


class PixelData(object):

    """creator of the pixel data"""

    def __init__(self, byte_array, offset, bitmap_info):
        super(PixelData, self).__init__()
        self._offset = offset
        self._bitmap_info = bitmap_info
        self._addition = 0

        pixel_size = self._bitmap_info.get_bit_count().get_unpack_value()

        if pixel_size <= 8:
            bytes_per_pixel = 1
        else:
            bytes_per_pixel = pixel_size // 8
        width_image = self._bitmap_info.get_width().get_unpack_value()
        if width_image % 4 != 0:
            self._addition = width_image // 4 * 4 + 4 - width_image
        width_image += self._addition
        height_image = abs(self._bitmap_info.get_height().get_unpack_value())
        image_size = width_image * height_image * bytes_per_pixel

        if pixel_size == 1:
            self._pixel_data = bytes_to_bits(
                byte_array[self._offset:self._offset + image_size])
        elif pixel_size == 4:
            pixel_data = bytes_to_bits(
                byte_array[self._offset:self._offset + image_size])
            pixel_data = map(lambda x: str(x), pixel_data)
            pixel_data = list(zip(*[iter(pixel_data)] * 4))
            self._pixel_data = \
                list(map(lambda x: int(''.join(x), 2), pixel_data))
        else:
            self._pixel_data = \
                byte_array[self._offset:self._offset + image_size]

    def get_pixel_color(self):
        """returns an array of pixels"""
        color_size = self._bitmap_info.get_bit_count().get_unpack_value() // 8
        if self._bitmap_info.get_color_table() is not None:
            color_table = self._bitmap_info.get_color_table()
            pixel_colors_generator = (color_table[i] for i in self._pixel_data)
        else:
            pixel_colors = list(zip(*[iter(self._pixel_data)] * color_size))
            pixel_colors_generator = (i for i in pixel_colors)

        return pixel_colors_generator

    def get_pixel_data(self):
        """returns an array of pixels"""
        return(self._pixel_data)

    def set_pixel_data(self, pixel_data):
        self._pixel_data = pixel_data

    def get_addition(self):
        return self._addition
