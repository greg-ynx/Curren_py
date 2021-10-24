"""
@Author : lyl_Lynx
@Note : Main script that has to be run
"""
import json
import sys
import webbrowser
from functools import partial
from rt_currency_converter import RealTimeCurrencyConverter
from form import *
from Exceptions import *
from PyQt5.QtWidgets import QMessageBox, QFileDialog


class Main:

    def __init__(self):
        # App initialization
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)

        self.rl_currency = RealTimeCurrencyConverter()
        self.list_currencies = list(self.rl_currency.currencies)
        self.init_comboBox()
        self.ui.label_exchange_rate.setText(self.rl_currency.exchange_rate(self.ui.comboBox_currency_from.currentText(),
                                                                           self.ui.comboBox_currency_to.currentText()))
        self.main_window.show()
        self.obj_list = []
        self.export_count = 0
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

        self.ui.pushButton_cancel.clicked.connect(self.on_close)
        self.ui.pushButton_save.clicked.connect(self.on_save)
        self.ui.actionSave.triggered.connect(self.on_save)
        self.ui.actionExport_file.triggered.connect(self.on_export)
        self.ui.actionSee_on_Git_Hub.triggered.connect(partial(webbrowser.open,
                                                               "https://github.com/lyl-Lynx/Currency-Converter"))
        # END Component connection

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

    def on_close(self):
        close_valid = QMessageBox(QMessageBox.Question, 'Close question', "Do you want to close Currency Converter ?",
                                  QMessageBox.Yes | QMessageBox.No)
        close_valid.setWindowIcon(QtGui.QIcon(self.ui.icon_name))
        close_valid.setDefaultButton(QMessageBox.Yes)
        close_valid.buttonClicked.connect(self.confirm_close)
        close_valid.exec()

    def confirm_close(self, i):
        print(i.text())
        if i.text() == "&Yes":
            sys.exit(app.exec())

    def on_save(self):
        try:
            if self.ui.lineEdit_from.text() == "" or self.ui.lineEdit_to.text() == "":
                raise NoneValueException
            else:
                obj = {
                    "id": "{}".format(len(self.obj_list)),
                    "from_currency": self.ui.comboBox_currency_from.currentText(),
                    "from_currency_value": self.ui.lineEdit_from.text(),
                    "to_currency": self.ui.comboBox_currency_to.currentText(),
                    "to_currency_value": self.ui.lineEdit_to.text()
                }
                self.obj_list.append(obj)
                print('New object added')
                data_saved = QMessageBox(QMessageBox.NoIcon, 'Add data message',
                                         "Data saved                   ",
                                         QMessageBox.Ok)
                data_saved.setWindowIcon(QtGui.QIcon(self.ui.icon_name))
                data_saved.exec()

        except NoneValueException:
            print('NoneValueException : No values entered in input lines')
            data_saved = QMessageBox(QMessageBox.Warning, 'Add data warning',
                                     "NoneValueException : No values entered in input lines",
                                     QMessageBox.Ok)
            data_saved.setWindowIcon(QtGui.QIcon(self.ui.icon_name))
            data_saved.exec()
        finally:
            print(self.obj_list)

    def on_export(self):
        try:
            if self.obj_list:
                option = QFileDialog.Options()
                option |= QFileDialog.DontUseNativeDialog
                file_name = QFileDialog.getSaveFileName(self.main_window, "Export file",
                                                        "cc" + str(self.export_count) + ".json",
                                                        filter="JSON files (*.json)", options=option)
                print(file_name)
                if file_name == ('', ''):
                    raise ActionCanceled
                else:
                    json.dump(self.obj_list, open(file_name[0], 'w'))
                    print('JSON file created')
                    message_exp = QMessageBox(QMessageBox.NoIcon, 'Export message',
                                              "JSON file created",
                                              QMessageBox.Ok)
                    message_exp.setWindowIcon(QtGui.QIcon(self.ui.icon_name))
                    message_exp.exec()
                    self.export_count += 1
            else:
                raise NoneValueException
        except NoneValueException:
            print('NoneValueException : No value in object list\n'
                  'Try to save some data')
            message_exp = QMessageBox(QMessageBox.Warning, 'Export warning',
                                      "NoneValueException : No value in object list\nTry to save some data",
                                      QMessageBox.Ok)
            message_exp.setWindowIcon(QtGui.QIcon(self.ui.icon_name))
            message_exp.exec()
        except ActionCanceled:
            print("Export canceled")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec())
