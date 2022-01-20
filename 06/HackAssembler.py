import sys
import Parser
import Code
import SymbolTable

if __name__ == '__main__':
    # 读文件并进行格式化处理
    filename = str(sys.argv[1])
    with open(filename) as file:
        lst = file.readlines()
    # 去除空行和注释
    for i in range(len(lst)):
        lst[i] = lst[i].replace(' ', '')
        lst[i] = lst[i].replace('\n', '')
        lst[i] = lst[i].replace('\t', '')
        lst[i] = lst[i].split('//')[0]
    instructions = [line for line in lst if line != '']
    # print(instructions)

    # 创建对象
    parser = Parser.Parser(instructions)
    code = Code.Code()
    table = SymbolTable.SymbolTable()
    hack = []

    # First pass
    # add Label to symbolTable
    num_label = 0
    while parser.hasMoreLines():
        parser.advance()
        if parser.instructionType() == 3:  # Label
            table.addEntry(parser.symbol(), parser.line - num_label)
            num_label += 1

    # Second pass (main loop)
    parser = Parser.Parser(instructions)  # from the beginning
    num_variable = 0  # 变量的数量
    while parser.hasMoreLines():
        parser.advance()
        if parser.instructionType() == 1:  # @xxx
            symbol = parser.symbol()
            if symbol[0] in '0123456789':  # @123
                s = bin(int(symbol))
                A_instruction = ('000000000000000' + s[2:])[-16:] + '\n'
                hack.append(A_instruction)

            else:  # @sum
                if not table.contains(symbol):
                    # not exists, add to table
                    table.addEntry(symbol, 16 + num_variable)
                    num_variable += 1
                address = table.getAddress(symbol)
                s = bin(address)
                A_instruction = ('000000000000000' + s[2:])[-16:] + '\n'
                hack.append(A_instruction)
        elif parser.instructionType() == 2:
            comp = code.comp(parser.comp())
            dest = code.dest(parser.dest())
            jump = code.jump(parser.jump())
            C_instruction = '111' + comp + dest + jump + '\n'
            hack.append(C_instruction)

    new_file = filename[:-4] + '.hack'
    with open(new_file, 'w') as f:
        f.writelines(hack)
