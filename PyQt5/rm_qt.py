# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rm_qt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RmWindow(object):
    def setupUi(self, RmWindow):
        RmWindow.setObjectName("RmWindow")
        RmWindow.resize(563, 413)
        self.centralwidget = QtWidgets.QWidget(RmWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rm_btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.rm_btn_back.setGeometry(QtCore.QRect(0, 0, 81, 31))
        self.rm_btn_back.setObjectName("rm_btn_back")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 40, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 120, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.rm_txt_no = QtWidgets.QLineEdit(self.centralwidget)
        self.rm_txt_no.setGeometry(QtCore.QRect(210, 119, 141, 21))
        self.rm_txt_no.setObjectName("rm_txt_no")
        self.rm_lbl_inf = QtWidgets.QLabel(self.centralwidget)
        self.rm_lbl_inf.setGeometry(QtCore.QRect(140, 210, 281, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rm_lbl_inf.setFont(font)
        self.rm_lbl_inf.setText("")
        self.rm_lbl_inf.setObjectName("rm_lbl_inf")
        self.rm_btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.rm_btn_search.setGeometry(QtCore.QRect(230, 160, 101, 31))
        self.rm_btn_search.setObjectName("rm_btn_search")
        self.rm_btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.rm_btn_delete.setGeometry(QtCore.QRect(230, 320, 101, 31))
        self.rm_btn_delete.setObjectName("rm_btn_delete")
        self.rm_lbl_result = QtWidgets.QLabel(self.centralwidget)
        self.rm_lbl_result.setGeometry(QtCore.QRect(370, 310, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rm_lbl_result.setFont(font)
        self.rm_lbl_result.setText("")
        self.rm_lbl_result.setObjectName("rm_lbl_result")
        RmWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RmWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 21))
        self.menubar.setObjectName("menubar")
        RmWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RmWindow)
        self.statusbar.setObjectName("statusbar")
        RmWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RmWindow)
        QtCore.QMetaObject.connectSlotsByName(RmWindow)

    def retranslateUi(self, RmWindow):
        _translate = QtCore.QCoreApplication.translate
        RmWindow.setWindowTitle(_translate("RmWindow", "MainWindow"))
        self.rm_btn_back.setText(_translate("RmWindow", "BACK"))
        self.label.setText(_translate("RmWindow", "Remove Student"))
        self.label_2.setText(_translate("RmWindow", "School No"))
        self.rm_btn_search.setText(_translate("RmWindow", "SEARCH"))
        self.rm_btn_delete.setText(_translate("RmWindow", "DELETE"))
