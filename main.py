from GUI.mainWindow import MainWindow
from PyQt4 import QtGui
import argparse
from bmp import BMP
import sys


if __name__ == "__main__":
    def console():
        try:
            bmp = BMP(args.image)
            if args.out_file:
                with open(args.out_file, "w") as f:
                    f.write(bmp.get_bitmap_file_header().get_all_info())
                    f.write(bmp.get_bitmap_info().get_all_info())
            else:
                print(bmp.get_bitmap_file_header().get_all_info())
                print(bmp.get_bitmap_info().get_all_info())
        except Exception as e:
            sys.exit("Error: {0}".format(e))

    def gui():
        app = QtGui.QApplication([])
        # try:
        icon = MainWindow(args.no_auto)
        if args.image:
            icon.view_data_image(args.image)
        icon.show()
        app.exec_()
        # except Exception as e:
            # sys.exit("Error: {0}".format(e))

    def test():
        lever = BMP.test()
        if not lever:
            print("Test is passed")
        else:
            print("Test fails")

    parser = argparse.ArgumentParser(
        prog="",
        description="",
        epilog="Copyright (C) 2015 Politov Alexey Version 1.0")
    sub_parsers = \
        parser.add_subparsers(title="use console or gui or test mode")

    console_parser = sub_parsers.add_parser("console")
    console_parser.add_argument("image", type=str, help="image")
    console_parser.add_argument(
        "-o", "--out_file", action="store",
        type=str, help="out file")
    console_parser.set_defaults(func=console)

    gui_parser = sub_parsers.add_parser("gui")
    gui_parser.add_argument(
        "-i", "--image", action="store",
        type=str, help="Image")
    gui_parser.add_argument(
        "-n", "--no_auto", action="store_true",
        help="per pixel render active")
    gui_parser.set_defaults(func=gui)

    test_parser = sub_parsers.add_parser("test")
    test_parser.set_defaults(func=test)

    args = parser.parse_args()
    # try:
    args.func()
    # except AttributeError:
        # parser.parse_args(["-h"])
