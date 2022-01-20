class Parser:
    def __init__(self, instructions):
        self.line = -1
        self.current = ''

        self.instructions = instructions

    def hasMoreLines(self):
        if self.line < len(self.instructions) - 1:
            return True
        return False

    def advance(self):
        # 下一条指令
        self.line += 1
        self.current = self.instructions[self.line]

    def instructionType(self):
        if self.current[0] == '@':
            return 1
        elif self.current[0] == '(' and self.current[-1] == ')':
            return 3
        else:
            return 2

    def symbol(self):
        if self.current[0] == '@':
            return self.current[1:]
        elif self.current[0] == '(' and self.current[-1] == ')':
            return self.current[1:-1]

    def dest(self):
        # 没有dest
        if '=' not in self.current:
            return None
        # 有dest
        return self.current.split("=")[0]

    def comp(self):
        return self.current.split(';')[0].split('=')[-1]

    def jump(self):
        # no jump
        if ';' not in self.current:
            return None
        return self.current.split(';')[-1]
