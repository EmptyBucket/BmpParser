from tempfile import TemporaryFile
import struct


class BI_RLE(object):

    def __init__(self, i):
        self._input_image = open(i, "rb")
        self.tmp = TemporaryFile()
        self._decode_pixel_data = bytearray()

        if self._input_image.read(2) != b'BM':
            raise IOError("Not BMP file")
        self._input_image.seek(10)

        of = self._input_image.read(4)
        # offset to start image data
        self._offset = struct.unpack('i', of)[0]

        self._input_image.seek(18)
        w = self._input_image.read(4)
        # image width
        self.w = struct.unpack('i', w)[0] + 1
        if self.w % 4 != 0:
            addition = self.w // 4 * 4 + 4 - self.w
        else:
            addition = 0
        self.w += addition

        h = self._input_image.read(4)
        # image height
        self.h = struct.unpack('i', h)[0]

        self._input_image.seek(28)
        b = self._input_image.read(2)
        # channel:bit per pixel
        self.bpp = struct.unpack('h', b)[0]

        if self.bpp != 4 and self.bpp != 8:
            raise IOError("Not 4-Bit or 8-Bit BMP file")

        c = self._input_image.read(4)
        # compression type
        self.comp = struct.unpack('i', c)[0]

        if self.comp != 2 and self.comp != 1:
            raise IOError("Not Compressed file")

        self.tPix = self.w * self.h
        self.rPix = 0
        self.lns = 1

        self.c = 0
        self.EORLED = False
        # fix for EORLE

        self._input_image.seek(self._offset)
        self.enc = self._input_image.read()
        self.dec = ""
        self.buf = ""

    def Decode(self):
        mrk = {0: self.EOSL, 1: self.EORLE, 2: self.MOFF}
        # funcs for RLE Data markers

        while (self.lns*self.w) <= self.tPix:
            b = self.enc[self.c:self.c+2]
            self.c += 2
            if len(b) != 2:
                break
            b0, b1 = b[0], b[1]
            if b0 == 0:
                mrk.get(b1, self.UENCD)(b0, b1)
            else:
                self.DENCD(b0, b1)

        return self._decode_pixel_data

    def HPIX(self, pixel):
        """ Half-Byte Packing for 4-Bit and Pixel Data Handler """
        if self.bpp == 4:
            if self.buf == "":
                self.buf = pixel << 4
            else:
                self.buf = self.buf | pixel
                self.tmp.write(struct.pack('i', self.buf))
                self.buf = ""
        else:
            self.tmp.write(bytes([pixel]))

    def EOSL(self, *arg):
        """ 00 00: End Of Scan Line """
        remain = self.w - self.rPix
        if not self.EORLED:
            self.rPix = 0
            self.lns += 1
        if remain == 0:
            remain = 2
        # fix for EOSL
        for i in range(remain):
            self.HPIX(0x00)

    def MOFF(self, *arg):
        """ 00 02: Move Offset """
        mov = self.enc[self.c:self.c+2]
        self.c += 2
        mov = mov[0] + mov[1]*self.w
        for i in range(mov):
            self.HPIX(0x00)
        self.rPix += mov
        self.lns += self.rPix // mov
        self.rPix %= mov

    def UENCD(self, *arg):
        """ 00 NN: Unencoded Data """
        p = arg[1]
        # unencoded pixels data
        if self.bpp == 4:
            # read bytes with padding byte for 4 bit
            b = int(round(p / 2)) + (int(round(p / 2)) % 2 | p % 2)
        else:
            # read bytes with padding byte for 8 bit
            b = p + p % 2
        ue = self.enc[self.c:self.c+b]
        self.c += b
        delta = self.rPix + p
        for i in range(b):
            if self.rPix == delta:
                break
            if self.bpp == 4:
                for j in range(2):
                    if self.rPix == delta:
                        break
                    self.HPIX((ue[i] & (
                        0x0F << (4 * ((j + 1) % 2))) >> (4 * ((j + 1) % 2))))
                    self.rPix += 1
            else:
                self.HPIX(ue[i])
                self.rPix += 1

    def DENCD(self, *arg):
        """ NN PP: Decode Encoded Data """
        b0, b1 = arg[0], arg[1]
        # piece, 2 pixels data
        for i in range(b0):
            if self.bpp == 4:
                self.HPIX((b1 & (0x0F << (4 * ((
                    i + 1) % 2)))) >> (4 * ((i + 1) % 2)))
            else:
                self.HPIX(b1)
            self.rPix += 1

    def EORLE(self, *arg):
        """ 00 01: End Of RLE Data, Writing Decoded File """
        self.EORLED = True
        self.EOSL()
        if not self.buf == "":
            self.tmp.write(self.buf)

        self.tmp.seek(0)
        self.dec = self.tmp.read()
        self.tmp.close()

        self._decode_pixel_data = self.dec

        self._input_image.close()
