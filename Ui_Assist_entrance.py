# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Work\ProxyAssistant\Assist_entrance.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(811, 507)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(811, 507))
        MainWindow.setMaximumSize(QtCore.QSize(811, 507))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.proxyTable = QtWidgets.QTableWidget(self.centralWidget)
        self.proxyTable.setGeometry(QtCore.QRect(0, 0, 811, 461))
        self.proxyTable.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.proxyTable.setObjectName("proxyTable")
        self.proxyTable.setColumnCount(0)
        self.proxyTable.setRowCount(0)
        self.btnStartFetch = QtWidgets.QPushButton(self.centralWidget)
        self.btnStartFetch.setGeometry(QtCore.QRect(700, 470, 92, 28))
        self.btnStartFetch.setObjectName("btnStartFetch")
        self.testURL = QtWidgets.QLineEdit(self.centralWidget)
        self.testURL.setGeometry(QtCore.QRect(248, 475, 190, 21))
        self.testURL.setObjectName("testURL")
        self.countrySelector = QtWidgets.QComboBox(self.centralWidget)
        self.countrySelector.setGeometry(QtCore.QRect(530, 474, 151, 21))
        self.countrySelector.setObjectName("countrySelector")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(441, 469, 71, 28))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(14, 477, 231, 17))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.status_label = QtWidgets.QLabel(self.layoutWidget)
        self.status_label.setObjectName("status_label")
        self.horizontalLayout.addWidget(self.status_label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.actionExportJSON_SR = QtWidgets.QAction(MainWindow)
        self.actionExportJSON_SR.setObjectName("actionExportJSON_SR")
        self.actionExport_Proxychains = QtWidgets.QAction(MainWindow)
        self.actionExport_Proxychains.setObjectName("actionExport_Proxychains")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnStartFetch.setText(_translate("MainWindow", "Fetch"))
        self.testURL.setText(_translate("MainWindow", "https://www.screenscraper.fr"))
        self.label.setText(_translate("MainWindow", "Country:"))
        self.status_label.setText(_translate("MainWindow", "Ready"))
        self.label_2.setText(_translate("MainWindow", "Test URL:"))
        self.actionExportJSON_SR.setText(_translate("MainWindow", "Export JSON for Shadowrocket"))
        self.actionExport_Proxychains.setText(_translate("MainWindow", "Export for Proxychains"))
        self.actionExport_Proxychains.setToolTip(_translate("MainWindow", "Export Table for Proxychains"))
