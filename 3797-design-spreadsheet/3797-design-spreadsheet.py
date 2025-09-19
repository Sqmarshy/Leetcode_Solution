class Spreadsheet:
    letters = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    def __init__(self, rows: int):
        self.sheet = {}
        for i in range(1, rows + 1):
            for j in self.letters:
                self.setCell(j + str(i), 0)

    def setCell(self, cell: str, value: int) -> None:
        self.sheet[cell] = value
        

    def resetCell(self, cell: str) -> None:
        self.sheet[cell] = 0

    def getValue(self, formula: str) -> int:
        s = formula[1:]
        a, b = s.split('+')
        val2 = self.sheet[b] if b[0] in self.letters else int(b)
        val1 = self.sheet[a] if a[0] in self.letters else int(a)
        return val1 + val2



# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)