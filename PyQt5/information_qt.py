# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'information_qt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InfWindow(object):
    def setupUi(self, InfWindow):
        InfWindow.setObjectName("InfWindow")
        InfWindow.resize(540, 397)
        self.centralwidget = QtWidgets.QWidget(InfWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inf_btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.inf_btn_back.setGeometry(QtCore.QRect(0, 0, 81, 31))
        self.inf_btn_back.setObjectName("inf_btn_back")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 50, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.inf_lbl_no = QtWidgets.QLabel(self.centralwidget)
        self.inf_lbl_no.setGeometry(QtCore.QRect(130, 120, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inf_lbl_no.setFont(font)
        self.inf_lbl_no.setObjectName("inf_lbl_no")
        self.inf_txt_no = QtWidgets.QLineEdit(self.centralwidget)
        self.inf_txt_no.setGeometry(QtCore.QRect(200, 119, 131, 21))
        self.inf_txt_no.setObjectName("inf_txt_no")
        self.inf_lbl_inf = QtWidgets.QLabel(self.centralwidget)
        self.inf_lbl_inf.setGeometry(QtCore.QRect(150, 210, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inf_lbl_inf.setFont(font)
        self.inf_lbl_inf.setText("")
        self.inf_lbl_inf.setObjectName("inf_lbl_inf")
        self.inf_btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.inf_btn_search.setGeometry(QtCore.QRect(220, 160, 91, 31))
        self.inf_btn_search.setObjectName("inf_btn_search")
        InfWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(InfWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 21))
        self.menubar.setObjectName("menubar")
        InfWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(InfWindow)
        self.statusbar.setObjectName("statusbar")
        InfWindow.setStatusBar(self.statusbar)

        self.retranslateUi(InfWindow)
        QtCore.QMetaObject.connectSlotsByName(InfWindow)

    def retranslateUi(self, InfWindow):
        _translate = QtCore.QCoreApplication.translate
        InfWindow.setWindowTitle(_translate("InfWindow", "MainWindow"))
        self.inf_btn_back.setText(_translate("InfWindow", "BACK"))
        self.label.setText(_translate("InfWindow", "Search Student"))
        self.inf_lbl_no.setText(_translate("InfWindow", "School No"))
        self.inf_btn_search.setText(_translate("InfWindow", "SEARCH"))
