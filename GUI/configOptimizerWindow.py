# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configOptimizerWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(306, 340)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 254, 265))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_Vin = QtWidgets.QLabel(self.layoutWidget)
        self.label_Vin.setObjectName("label_Vin")
        self.horizontalLayout.addWidget(self.label_Vin)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.input_fvcmax = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_fvcmax.setMaximumSize(QtCore.QSize(60, 16777215))
        self.input_fvcmax.setObjectName("input_fvcmax")
        self.horizontalLayout.addWidget(self.input_fvcmax)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_Vo = QtWidgets.QLabel(self.layoutWidget)
        self.label_Vo.setObjectName("label_Vo")
        self.horizontalLayout_2.addWidget(self.label_Vo)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.input_fdmax = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_fdmax.setMaximumSize(QtCore.QSize(60, 16777215))
        self.input_fdmax.setObjectName("input_fdmax")
        self.horizontalLayout_2.addWidget(self.input_fdmax)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_Vo_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_Vo_2.setObjectName("label_Vo_2")
        self.horizontalLayout_3.addWidget(self.label_Vo_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.input_ficmax = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_ficmax.setMaximumSize(QtCore.QSize(60, 16777215))
        self.input_ficmax.setObjectName("input_ficmax")
        self.horizontalLayout_3.addWidget(self.input_ficmax)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_DeltaIin = QtWidgets.QLabel(self.layoutWidget)
        self.label_DeltaIin.setObjectName("label_DeltaIin")
        self.horizontalLayout_4.addWidget(self.label_DeltaIin)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.input_fidmax = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_fidmax.setMaximumSize(QtCore.QSize(60, 16777215))
        self.input_fidmax.setObjectName("input_fidmax")
        self.horizontalLayout_4.addWidget(self.input_fidmax)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_DeltaVo = QtWidgets.QLabel(self.layoutWidget)
        self.label_DeltaVo.setObjectName("label_DeltaVo")
        self.horizontalLayout_5.addWidget(self.label_DeltaVo)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.input_futrafo = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_futrafo.setMaximumSize(QtCore.QSize(60, 16777215))
        self.input_futrafo.setObjectName("input_futrafo")
        self.horizontalLayout_5.addWidget(self.input_futrafo)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_JMax = QtWidgets.QLabel(self.layoutWidget)
        self.label_JMax.setObjectName("label_JMax")
        self.horizontalLayout_6.addWidget(self.label_JMax)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.input_fuLi = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_fuLi.sizePolicy().hasHeightForWidth())
        self.input_fuLi.setSizePolicy(sizePolicy)
        self.input_fuLi.setMinimumSize(QtCore.QSize(20, 20))
        self.input_fuLi.setMaximumSize(QtCore.QSize(60, 20))
        self.input_fuLi.setObjectName("input_fuLi")
        self.horizontalLayout_6.addWidget(self.input_fuLi)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_DeltaVo_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_DeltaVo_2.setObjectName("label_DeltaVo_2")
        self.horizontalLayout_7.addWidget(self.label_DeltaVo_2)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.input_fuLk = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_fuLk.setMaximumSize(QtCore.QSize(60, 16777215))
        self.input_fuLk.setObjectName("input_fuLk")
        self.horizontalLayout_7.addWidget(self.input_fuLk)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem11)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_11.addWidget(self.pushButton)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem12)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 306, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Configurações de Otimização</span></p></body></html>"))
        self.label_Vin.setText(_translate("MainWindow", "Fator VcMáx"))
        self.label_Vo.setText(_translate("MainWindow", "Fator VdMáx"))
        self.label_Vo_2.setText(_translate("MainWindow", "Fator Icef Máx"))
        self.label_DeltaIin.setText(_translate("MainWindow", "Fator Idef Máx"))
        self.label_DeltaVo.setText(_translate("MainWindow", "Fu transformador"))
        self.label_JMax.setText(_translate("MainWindow", "Fu indutor de entrada"))
        self.label_DeltaVo_2.setText(_translate("MainWindow", "Fu indutor auxiliar"))
        self.pushButton.setText(_translate("MainWindow", "Salvar"))
