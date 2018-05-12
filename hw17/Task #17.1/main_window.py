import sys
from PyQt5 import QtCore, QtWidgets, QtGui
import my_form
import functools

#C:\Users\nosov\venv\qtt\Scripts\pyuic5.exe my_form.ui -o my_form.py

class MainApplication(QtWidgets.QMainWindow):
    def __init__(self):
        self.stack_operation = []
        self.last_stack_number = False
        self.exist_oper = False

        super(MainApplication, self).__init__()
        self.ui = my_form.Ui_MainWindow()
        self.ui.setupUi(self)

        # создаем кнопки цифр
        for i in range(9):
            col = i % 3
            row = 3- i // 3
            button = QtWidgets.QPushButton(self.ui.gridLayoutWidget)

            self.create_but(button,i+1,row,col)

            button.clicked.connect(functools.partial(self.button_number_pressed, i + 1))

        #ноль
        button = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
        self.create_but(button,0,4,1)
        button.clicked.connect(functools.partial(self.button_number_pressed, 0))

        #равно
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
        #self.ui.pushButton_equal.clicked.connect(self.button_oper_equal)
        #self.ui.pushButton_C.clicked.connect(self.button_oper_C)

        self.display_stack()

    def button_number_pressed(self, number):
        self.add_in_stack(str(number))

    def button_oper_plus(self):
        self.add_in_stack('+', type_number=False)

    def button_oper_del(self):
        self.add_in_stack('/', type_number=False)

    def button_oper_mul(self):
        self.add_in_stack('*', type_number=False)

    def button_oper_step(self):
        self.add_in_stack('^', type_number=False)

    def button_oper_div(self):
        self.add_in_stack('-', type_number=False)

    def button_oper_equal(self):
        self.calculate()
        self.clear_stack()

    def button_oper_C(self):
        self.clear_stack()
        self.display_stack()

    def add_in_stack(self, symbol, type_number=True):
        # если до этого было число и сейчас число
        if type_number:
            if self.last_stack_number :
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
                    res='На 0 делить нельзя'
            else:
                res = a ** b
            self.stack_operation.append('=')
            self.stack_operation.append(str(res))

        self.display_stack()

    def clear_stack(self):
        self.stack_operation.clear()
        self.last_stack_number = False
        self.exist_oper = False

    def display_stack(self):
        str_disp = functools.reduce(lambda x, y: x + y, self.stack_operation, '')
        #print(str_disp)
        self.ui.disp_stack.setText(str(str_disp))

        if (len(self.stack_operation) != 0 and self.last_stack_number):

            # if len(self.stack_operation[-1]) > self.ui.lcdNumber.digitCount():
            self.ui.lcdNumber.display((self.stack_operation[-1]))
            # self.ui.lcdNumber.display('%.10f'%(self.stack_operation[-1]))
        else:
            self.ui.lcdNumber.display('')

    def create_but(self,button,i,row,col):
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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MainApplication()
    window.show()

    sys.exit(app.exec_())
