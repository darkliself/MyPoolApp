# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 681)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.text_tabs_layout = QtWidgets.QVBoxLayout()
        self.text_tabs_layout.setSpacing(6)
        self.text_tabs_layout.setObjectName("text_tabs_layout")
        self.tab_container = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_container.setObjectName("tab_container")
        self.pool = QtWidgets.QWidget()
        self.pool.setObjectName("pool")
        self.gridLayout = QtWidgets.QGridLayout(self.pool)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.pool_textarea = QtWidgets.QTextEdit(self.pool)
        self.pool_textarea.setObjectName("pool_textarea")
        self.gridLayout.addWidget(self.pool_textarea, 0, 0, 1, 1)
        self.tab_container.addTab(self.pool, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab_container.addTab(self.tab_2, "")
        self.text_tabs_layout.addWidget(self.tab_container)
        self.gridLayout_5.addLayout(self.text_tabs_layout, 1, 0, 1, 4)
        self.reserved_2 = QtWidgets.QGridLayout()
        self.reserved_2.setSpacing(6)
        self.reserved_2.setObjectName("reserved_2")
        self.gridLayout_5.addLayout(self.reserved_2, 0, 3, 1, 1)
        self.left_upper_layout = QtWidgets.QVBoxLayout()
        self.left_upper_layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.left_upper_layout.setSpacing(6)
        self.left_upper_layout.setObjectName("left_upper_layout")
        self.api_label_layout = QtWidgets.QVBoxLayout()
        self.api_label_layout.setSpacing(6)
        self.api_label_layout.setObjectName("api_label_layout")
        self.api_label = QtWidgets.QLabel(self.centralwidget)
        self.api_label.setObjectName("api_label")
        self.api_label_layout.addWidget(self.api_label)
        self.left_upper_layout.addLayout(self.api_label_layout)
        self.get_layout = QtWidgets.QVBoxLayout()
        self.get_layout.setSpacing(6)
        self.get_layout.setObjectName("get_layout")
        self.get_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.get_button.sizePolicy().hasHeightForWidth())
        self.get_button.setSizePolicy(sizePolicy)
        self.get_button.setObjectName("get_button")
        self.get_layout.addWidget(self.get_button)
        self.left_upper_layout.addLayout(self.get_layout)
        self.gridLayout_5.addLayout(self.left_upper_layout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.api_input_layout = QtWidgets.QVBoxLayout()
        self.api_input_layout.setSpacing(6)
        self.api_input_layout.setObjectName("api_input_layout")
        self.api_input = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.api_input.sizePolicy().hasHeightForWidth())
        self.api_input.setSizePolicy(sizePolicy)
        self.api_input.setMinimumSize(QtCore.QSize(250, 0))
        self.api_input.setObjectName("api_input")
        self.api_input_layout.addWidget(self.api_input)
        self.verticalLayout_2.addLayout(self.api_input_layout)
        self.set_layout = QtWidgets.QVBoxLayout()
        self.set_layout.setSpacing(6)
        self.set_layout.setObjectName("set_layout")
        self.set_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.set_button.sizePolicy().hasHeightForWidth())
        self.set_button.setSizePolicy(sizePolicy)
        self.set_button.setObjectName("set_button")
        self.set_layout.addWidget(self.set_button)
        self.verticalLayout_2.addLayout(self.set_layout)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.reserved_1 = QtWidgets.QGridLayout()
        self.reserved_1.setSpacing(6)
        self.reserved_1.setObjectName("reserved_1")
        self.gridLayout_5.addLayout(self.reserved_1, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.tab_container.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tab_container.setTabText(self.tab_container.indexOf(self.pool), _translate("MainWindow", "pool"))
        self.tab_container.setTabText(self.tab_container.indexOf(self.tab_2), _translate("MainWindow", "tab_2"))
        self.api_label.setText(_translate("MainWindow", "API key"))
        self.get_button.setText(_translate("MainWindow", "Get"))
        self.set_button.setText(_translate("MainWindow", "Set"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())

