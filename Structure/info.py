from struct import unpack


class Info(object):

    """docstring for Info"""

    def __init__(self, name, value, address, size, details):
        super(Info, self).__init__()
        self._name = name
        self._value = value
        if type(value) is bytes and len(value) <= 4:
            if len(value) == 2:
                self._unpack_value = unpack('h', value)[0]
            else:
                self._unpack_value = unpack('i', value)[0]
        else:
            self._unpack_value = None
        self._address = address
        self._valueByte = size
        self._details = details

    def get_name(self):
        return(self._name)

    def get_value(self):
        return(self._value)

    def get_address(self):
        return(self._address)

    def get_details(self):
        return(self._details)

    def get_unpack_value(self):
        return(self._unpack_value)

    def get_value_byte(self):
        return(self._valueByte)

    def get_all_data(self):
        allInfo = ''
        if self._name is not None:
            allInfo += self._name + ":\n"
        if self._value is not None:
            allInfo += "\tValue:" + str(self._value) + "\n"
        if self._unpack_value is not None:
            allInfo += "\tUnpack value:" + str(self._unpack_value) + "\n"
        if self._address is not None:
            allInfo += "\tAddress:" + str(self._address) + "\n"
        if self._valueByte is not None:
            allInfo += "\tSize:" + str(self._valueByte) + "\n"
        if self._details is not None:
            allInfo += "\tDetails:" + self._details + "\n"
        allInfo += "-------------------------------------------------------\n"
        return(allInfo)
