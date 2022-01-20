class Code:
    def dest(self, dest):
        """:return the binary representation of the parsed dest field"""
        if dest == None:
            return '000'
        str = 'ADM'
        ret = ''
        for char in str:
            if char in dest:
                ret = ret + '1'
            else:
                ret = ret + '0'

        return ret

    def comp(self, key):
        """:return the binary representation of the parsed comp field"""
        # 数据字典
        dic = {
            '0': '0101010',
            '1': '0111111',
            '-1': '0111010',
            'D': '0001100',
            'A': '0110000',
            'M': '1110000',
            '!D': '0001101',
            '!A': '0110001',
            '!M': '1110001',
            '-D': '0001111',
            '-A': '0110011',
            '-M': '1110011',
            'D+1': '0011111',
            'A+1': '0110111',
            'M+1': '1110111',
            'D-1': '0001110',
            'A-1': '0110010',
            'M-1': '1110010',
            'D+A': '0000010',
            'D+M': '1000010',
            'D-A': '0010011',
            'D-M': '1010011',
            'A-D': '0000111',
            'M-D': '1000111',
            'D&A': '0000000',
            'D&M': '1000000',
            'D|A': '0010101',
            'D|M': '1010101',
        }
        # 返回字典的值
        return dic[key]

    def jump(self, condition):
        """:return the binary representation of the parsed jump field"""
        if condition == None:
            return '000'
        dic = {
            'JGT': '001',
            'JEQ': '010',
            'JGE': '011',
            'JLT': '100',
            'JNE': '101',
            'JLE': '110',
            'JMP': '111',
        }
        return dic[condition]
