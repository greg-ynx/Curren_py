"""
@Author : lyl_Lynx
@Note : Form implementation generated from reading ui file 'form.ui'
        Created by: PyQt5 UI code generator 5.15.4
"""

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(755, 492)
        MainWindow.setMinimumSize(QtCore.QSize(755, 492))
        MainWindow.setMaximumSize(QtCore.QSize(755, 492))
        MainWindow.setSizeIncrement(QtCore.QSize(755, 492))
        MainWindow.setBaseSize(QtCore.QSize(755, 492))

        self.icon_name = "Logo.ico"
        MainWindow.setWindowIcon(QtGui.QIcon(self.icon_name))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 741, 441))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.frame = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 741, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_title = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_title.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_title.setObjectName("horizontalLayout_title")

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_title.addItem(spacerItem)

        self.title = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.title.setObjectName("title")
        self.horizontalLayout_title.addWidget(self.title)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_title.addItem(spacerItem1)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 120, 741, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_comboBox = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_comboBox.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_comboBox.setObjectName("horizontalLayout_comboBox")

        self.comboBox_currency_from = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_currency_from.setMinimumSize(QtCore.QSize(160, 20))
        self.comboBox_currency_from.setMaximumSize(QtCore.QSize(160, 20))
        self.comboBox_currency_from.setObjectName("comboBox_currency_from")
        self.comboBox_currency_from.setMaxCount(160)
        # self.comboBox_currency_from.setEditable(True)
        self.horizontalLayout_comboBox.addWidget(self.comboBox_currency_from)

        spacerItem2 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_comboBox.addItem(spacerItem2)

        self.comboBox_currency_to = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_currency_to.setMinimumSize(QtCore.QSize(160, 20))
        self.comboBox_currency_to.setMaximumSize(QtCore.QSize(160, 20))
        self.comboBox_currency_to.setObjectName("comboBox_currency_to")
        self.comboBox_currency_to.setMaxCount(160)
        # self.comboBox_currency_to.setEditable(True)
        self.horizontalLayout_comboBox.addWidget(self.comboBox_currency_to)

        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 170, 721, 71))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_line = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_line.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_line.setObjectName("horizontalLayout_line")

        self.only_int_pattern = QtCore.QRegExp("[0-9.]{30}")
        self.only_int = QtGui.QRegExpValidator(self.only_int_pattern)

        self.lineEdit_from = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_from.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_from.sizePolicy().hasHeightForWidth())
        self.lineEdit_from.setSizePolicy(sizePolicy)
        self.lineEdit_from.setMinimumSize(QtCore.QSize(300, 60))
        self.lineEdit_from.setMaximumSize(QtCore.QSize(300, 60))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_from.setFont(font)
        self.lineEdit_from.setObjectName("lineEdit_from")
        self.lineEdit_from.setValidator(self.only_int)
        self.horizontalLayout_line.addWidget(self.lineEdit_from)

        spacerItem3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_line.addItem(spacerItem3)

        self.lineEdit_to = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_to.setEnabled(True)
        self.lineEdit_to.setMinimumSize(QtCore.QSize(190, 60))
        self.lineEdit_to.setMaximumSize(QtCore.QSize(300, 60))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_to.setFont(font)
        self.lineEdit_to.setObjectName("lineEdit_to")
        self.lineEdit_to.setValidator(self.only_int)
        self.horizontalLayout_line.addWidget(self.lineEdit_to)

        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 50, 731, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 399, 741, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_end_button = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_end_button.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_end_button.setObjectName("horizontalLayout_end_button")

        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_end_button.addItem(spacerItem4)

        self.pushButton_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_end_button.addWidget(self.pushButton_cancel)
        self.pushButton_save = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_end_button.addWidget(self.pushButton_save)

        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_end_button.addItem(spacerItem5)

        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 270, 741, 80))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_exchange_rate = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_exchange_rate.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_exchange_rate.setObjectName("horizontalLayout_exchange_rate")

        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_exchange_rate.addItem(spacerItem6)

        self.label_exchange_rate = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_exchange_rate.setMinimumSize(QtCore.QSize(300, 0))
        self.label_exchange_rate.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_exchange_rate.setAlignment(QtCore.Qt.AlignCenter)
        self.label_exchange_rate.setObjectName("label_exchange_rate")
        self.horizontalLayout_exchange_rate.addWidget(self.label_exchange_rate)

        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_exchange_rate.addItem(spacerItem7)

        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 70, 721, 41))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_currency = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_currency.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_currency.setObjectName("horizontalLayout_currency")

        self.label_from = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_from.setAlignment(QtCore.Qt.AlignCenter)
        self.label_from.setObjectName("label_from")
        self.horizontalLayout_currency.addWidget(self.label_from)

        spacerItem8 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_currency.addItem(spacerItem8)

        self.label_to = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_to.setAlignment(QtCore.Qt.AlignCenter)
        self.label_to.setObjectName("label_to")
        self.horizontalLayout_currency.addWidget(self.label_to)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 21))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.actionExport_file = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("Export file")

        self.actionSee_on_Git_Hub = QtWidgets.QAction(MainWindow)
        self.actionSee_on_Git_Hub.setObjectName("actionSee_on_Git_Hub")

        self.menuFile.addAction(self.actionSave)

        self.menuFile.addAction(self.actionExport_file)

        self.menuHelp.addAction(self.actionSee_on_Git_Hub)

        self.menubar.addAction(self.menuFile.menuAction())

        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Currency Converter"))
        self.title.setText(_translate("MainWindow", "Currency converter"))
        #self.lineEdit_from.setText(_translate("MainWindow", "Enter currency"))
        #self.lineEdit_to.setText(_translate("MainWindow", "Enter currency"))
        self.pushButton_cancel.setText(_translate("MainWindow", "Close"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.label_exchange_rate.setText(_translate("MainWindow", ""))
        self.label_from.setText(_translate("MainWindow", "Currency : "))
        self.label_to.setText(_translate("MainWindow", "Currency : "))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExport_file.setText(_translate("MainWindow", "Export file"))
        self.actionSee_on_Git_Hub.setText(_translate("MainWindow", "See on Git Hub"))
