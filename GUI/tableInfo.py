from PyQt4 import QtGui


class TableInfo(object):

    """docstring for TableInfo"""

    def __init__(self, all_list_info):
        super(TableInfo, self).__init__()
        self.all_list_info = all_list_info

        self.table_widget = QtGui.QTableWidget()
        self.table_widget.setShowGrid(False)
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(len(self.all_list_info) * 6)
        self.table_widget.setHorizontalHeaderItem(
            0, QtGui.QTableWidgetItem("Name field"))
        self.table_widget.setHorizontalHeaderItem(
            1, QtGui.QTableWidgetItem("Value"))
        self.table_widget.verticalHeader().hide()
        self.table_widget.setColumnWidth(1, 457)

    def fill_row(
            self, number_row, name_field, value_field,
            color_name_field=QtGui.QColor(170, 170, 170),
            color_value_field=QtGui.QColor(200, 200, 200)):
        name_field_header = QtGui.QTableWidgetItem(name_field)
        name_field_header.setBackgroundColor(color_name_field)
        font_name_field_header = QtGui.QFont()
        font_name_field_header.setBold(True)
        name_field_header.setFont(font_name_field_header)

        valueFiledHeader = QtGui.QTableWidgetItem(value_field)
        valueFiledHeader.setBackgroundColor(color_value_field)

        self.table_widget.setItem(number_row, 0, name_field_header)
        self.table_widget.setItem(number_row, 1, valueFiledHeader)

    def fill_table(self):
        number_row = 0
        for info in self.all_list_info:
            name = info.get_name()
            if name is not None:
                self.fill_row(
                    number_row, "Name", name, QtGui.QColor(110, 110, 110),
                    QtGui.QColor(140, 140, 140))
                number_row += 1

            value = info.get_value()
            if value is not None:
                self.fill_row(number_row, "Value", str(value))
                number_row += 1

            unpack_value = info.get_unpack_value()
            if unpack_value is not None:
                self.fill_row(number_row, "Unpack value", str(unpack_value))
                number_row += 1

            address = info.get_address()
            if address is not None:
                self.fill_row(number_row, "Address", str(address))
                number_row += 1

            value_byte = info.get_value_byte()
            if value_byte is not None:
                self.fill_row(number_row, "Value byte", str(value_byte))
                number_row += 1

            details = info.get_details()
            if details is not None:
                self.fill_row(number_row, "Details", details)
                number_row += 1

        self.table_widget.setRowCount(number_row)
        self.table_widget.item(
            0, 0).setBackgroundColor(QtGui.QColor(110, 170, 110))
        self.table_widget.item(
            0, 1).setBackgroundColor(QtGui.QColor(140, 200, 140))
        self.table_widget.item(
            33, 0).setBackgroundColor(QtGui.QColor(110, 170, 110))
        self.table_widget.item(
            33, 1).setBackgroundColor(QtGui.QColor(140, 200, 140))

    def get_table_info(self):
        self.fill_table()
        self.table_widget.resizeRowsToContents()
        return(self.table_widget)
