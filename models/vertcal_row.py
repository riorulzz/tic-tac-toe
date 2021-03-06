__author__ = 'mukul'

from utils.rule_utils import RowRulesEngine


class VerticalRow(object):
    def __init__(self, id, col_size, squares):
        self.id = id
        self.squares = [squares[index] for index in range(id, len(squares), col_size)]
        self.rule_engine = RowRulesEngine()

    def __str__(self):
        return 'vertical row:'+str(self.squares)

    def __repr__(self):
        return self.__str__()

    def setSquare(self, row_no, value):
        self.squares[row_no].setValue(value)
        self.run()

    def run(self, *args, **kwargs):
        self.rule_engine.run(self, args, kwargs)