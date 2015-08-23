__author__ = 'mukul'

from utils.rule_utils import RowRulesEngine


class HorizontalRow(RowRulesEngine):
    def __init__(self, id, col_size, squares):
        self.id = id
        self.squares = [squares[index] for index in range(id * col_size, (id + 1) * col_size, 1)]

    def __str__(self):
        return 'horizontal row:'+str(self.squares)

    def __repr__(self):
        return self.__str__()

    def setSquare(self, col, value):
        self.squares[col].setValue(value)
        self.run()