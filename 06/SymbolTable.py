import string


class SymbolTable:
    def __init__(self):
        # variable symbol的数量
        self.num = 0

        # 初始化表
        self.table = {}
        for i in range(16):
            key = 'R' + str(i)
            self.table[key] = i
        self.table['SCREEN'] = 16384
        self.table['KBD'] = 24576
        self.table['SP'] = 0
        self.table['LCL'] = 1
        self.table['ARG'] = 2
        self.table['THIS'] = 3
        self.table['THAT'] = 4

    def contains(self, key: string):
        return key in self.table

    def getAddress(self, key: string):
        return self.table[key]

    def addEntry(self, symbol: string, address: int):
        self.table[symbol] = address

