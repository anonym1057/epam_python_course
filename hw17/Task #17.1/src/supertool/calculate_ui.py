import sys
from PyQt5 import QtCore, QtWidgets, QtGui
import supertool.calculate_form as form
import functools


class CalculateWidget(QtWidgets.QWidget):
    """
    Class of calculator widget.
    """
    def __init__(self):
        self.stack_operation = []
        self.last_stack_number = False
        self.exist_oper = False

        super(CalculateWidget, self).__init__()
        self.ui = form.Ui_Form()
        self.ui.setupUi(self)

        # создаем кнопки цифр
        for i in range(9):
            col = i % 3
            row = 3 - i // 3
            button = QtWidgets.QPushButton(self.ui.gridLayoutWidget)

            self.create_but(button, i + 1, row, col)

            button.clicked.connect(functools.partial(self.button_number_pressed, i + 1))

        # ноль
        button = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
        self.create_but(button, 0, 4, 1)
        button.clicked.connect(functools.partial(self.button_number_pressed, 0))

        # равно
        button = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
        self.create_but(button, '=', 4, 2)
        button.clicked.connect(self.button_oper_equal)

        # равно
        button = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
        self.create_but(button, 'C', 4, 0)
        button.clicked.connect(self.button_oper_C)

        self.ui.pushButton_plus.clicked.connect(self.button_oper_plus)
        self.ui.pushButton_del.clicked.connect(self.button_oper_del)
        self.ui.pushButton_mul.clicked.connect(self.button_oper_mul)
        self.ui.pushButton_div.clicked.connect(self.button_oper_div)
        self.ui.pushButton_step.clicked.connect(self.button_oper_step)
        # self.ui.pushButton_equal.clicked.connect(self.button_oper_equal)
        # self.ui.pushButton_C.clicked.connect(self.button_oper_C)

        self.display_stack()

    def button_number_pressed(self, number):
        """
        Connected with numbers button.
        Add number in stack operation

        :param number: number of button
        :return: none
        """
        self.add_in_stack(str(number))

    def button_oper_plus(self):
        """
        Connected with plus_button.
        Add plus in stack operation if possible

        :return: None
        """

        self.add_in_stack('+', type_number=False)

    def button_oper_del(self):
        """
        Connected with division_button.
        Add division in stack operation if possible

        :return: None
        """

        self.add_in_stack('/', type_number=False)

    def button_oper_mul(self):
        """
        Connected with multiplication_button.
        Add multiplication in stack operation if possible

        :return:
        """
        self.add_in_stack('*', type_number=False)

    def button_oper_step(self):
        """
        Connected with Connected with exponentiation_button.
        Add exponentiation in stack operation if possible

        :return:
        """
        self.add_in_stack('^', type_number=False)

    def button_oper_div(self):
        """
        Connected with subtraction_button.
        Add subtraction in stack operation if possible

        :return:
        """
        self.add_in_stack('-', type_number=False)

    def button_oper_equal(self):
        """
        Connected with equal_button.
        Calculates expression in stack and clear stack/

        :return:
        """
        self.calculate()
        self.clear_stack()

    def button_oper_C(self):
        """
        Connected with clear_buttom/
        Clear stack.

        :return:
        """
        self.clear_stack()
        self.display_stack()

    def add_in_stack(self, symbol, type_number=True):
        """
        Function add operation or number in stack if possible.

        :param symbol: operation or number
        :type symbol: str
        :param type_number: number or operation
        :type type_number: bool
        :return:
        """
        # если до этого было число и сейчас число
        if type_number:
            if self.last_stack_number:
                if len(self.stack_operation[-1]) < self.ui.lcdNumber.digitCount():
                    self.stack_operation[-1] += symbol
            else:
                self.stack_operation.append(symbol)

            self.last_stack_number = True

        elif self.last_stack_number and not self.exist_oper and self.stack_operation != []:
            self.stack_operation.append(symbol)
            self.exist_oper = True
            self.last_stack_number = False

        self.display_stack()

    def calculate(self):
        """
        Calculate expression in stack and print result in window

        :return:
        """

        if len(self.stack_operation) > 1:
            a = int(self.stack_operation[-3])
            op = self.stack_operation[-2]
            b = int(self.stack_operation[-1])

            res = 0
            if op == '+':
                res = a + b
            elif op == '-':
                res = a - b
            elif op == '*':
                res = a * b
            elif op == '/':
                if b != 0:
                    res = a / b
                else:
                    res = 'На 0 делить нельзя'
                    self.stack_operation.append('=')
                    self.stack_operation.append(str(res))
                    self.display_stack()
                    return
            else:
                res = a ** b
            self.stack_operation.append('=')

            if len(str(int(res))) < self.ui.lcdNumber.digitCount():
                self.stack_operation.append(str(res))
            else:
                self.stack_operation.append("Слишком длинный результат")

        self.display_stack()

    def clear_stack(self):
        """
        Clear stack.

        :return:
        """
        self.stack_operation.clear()
        self.last_stack_number = False
        self.exist_oper = False

    def display_stack(self):
        """
        Display expression on window/

        :return:
        """
        str_disp = functools.reduce(lambda x, y: x + y, self.stack_operation, '')
        # print(str_disp)
        self.ui.disp_stack.setText(str(str_disp))

        if (len(self.stack_operation) != 0 and self.last_stack_number):

            # if len(self.stack_operation[-1]) > self.ui.lcdNumber.digitCount():
            self.ui.lcdNumber.display((self.stack_operation[-1]))
            # self.ui.lcdNumber.display('%.10f'%(self.stack_operation[-1]))
        else:
            self.ui.lcdNumber.display('')

    def create_but(self, button, i, row, col):
        """
        Cleate Button style

        """
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        button.setFont(font)
        button.setObjectName(f'button_{i}')
        self.ui.gridLayout.addWidget(button, row, col, 1, 1)
        button.setText(str(i))