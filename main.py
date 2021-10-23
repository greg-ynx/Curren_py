"""
@Author : lyl_Lynx
@Note : Main script that has to be run
"""

import sys
from functools import partial

from rt_currency_converter import RealTimeCurrencyConverter
from form import *


class Main:

    def __init__(self):
        # App initialization
        self.app = QtWidgets.QApplication(sys.argv)
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)

        self.rl_currency = RealTimeCurrencyConverter()
        self.list_currencies = list(self.rl_currency.currencies)
        self.init_comboBox()
        self.main_window.show()
        # END App initialization

        # Component connection
        self.ui.comboBox_currency_from.currentTextChanged.connect(self.change_exchange_rate)
        self.ui.comboBox_currency_to.currentTextChanged.connect(self.change_exchange_rate)

        self.ui.comboBox_currency_from.currentTextChanged.connect(partial(self.change_lineEdit_value,
                                                                          self.ui.lineEdit_to))
        self.ui.comboBox_currency_to.currentTextChanged.connect(partial(self.change_lineEdit_value,
                                                                        self.ui.lineEdit_from))

        self.ui.lineEdit_from.textEdited.connect(partial(self.change_lineEdit_value, self.ui.lineEdit_from))
        self.ui.lineEdit_to.textEdited.connect(partial(self.change_lineEdit_value, self.ui.lineEdit_to))
        # END Component connection

        sys.exit(self.app.exec())

    def init_comboBox(self):
        self.ui.comboBox_currency_to.addItems(self.list_currencies)
        self.ui.comboBox_currency_from.addItems(self.list_currencies)

    def change_exchange_rate(self):
        self.ui.label_exchange_rate.setText(self.rl_currency.exchange_rate(self.ui.comboBox_currency_from.currentText(),
                                                                           self.ui.comboBox_currency_to.currentText()))

    def change_lineEdit_value(self, line_edit):

        if line_edit.text() == "":
            self.ui.lineEdit_from.setText("")
            self.ui.lineEdit_to.setText("")

        elif line_edit.text().count('.') > 1:
            line_edit.setText(line_edit.text()[0:-1])

        elif line_edit.text() == ".":
            self.ui.lineEdit_from.setText("")
            self.ui.lineEdit_to.setText("")

        else:
            list_f = line_edit.text().split(".")
            print(list_f)
            deci_len = 2
            if len(list_f) > 1 and len(list_f[1]) > 2:
                deci_len = len(list_f[1])
            print(deci_len)
            if line_edit.objectName() == self.ui.lineEdit_from.objectName():
                self.ui.lineEdit_to.setText(
                    format(self.rl_currency.convert(self.ui.comboBox_currency_from.currentText(),
                                                    self.ui.comboBox_currency_to.currentText(),
                                                    float(line_edit.text()),
                                                    deci_len),
                           '.{}f'.format(deci_len)))
            elif line_edit.objectName() == self.ui.lineEdit_to.objectName():
                self.ui.lineEdit_from.setText(
                    format(self.rl_currency.convert(self.ui.comboBox_currency_to.currentText(),
                                                    self.ui.comboBox_currency_from.currentText(),
                                                    float(line_edit.text()),
                                                    deci_len),
                           '.{}f'.format(deci_len)))


if __name__ == '__main__':
    main = Main()
