# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow2.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1080, 1080))
        self.centralwidget.setMaximumSize(QtCore.QSize(1080, 1080))
        self.centralwidget.setObjectName("centralwidget")
        self.graphWidget = MplWidget(self.centralwidget)
        self.graphWidget.setGeometry(QtCore.QRect(410, 390, 360, 280))
        self.graphWidget.setMinimumSize(QtCore.QSize(360, 280))
        self.graphWidget.setObjectName("graphWidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 301, 693))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_ConfiguracoesDoOtimizador_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_ConfiguracoesDoOtimizador_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ConfiguracoesDoOtimizador_2.setObjectName("label_ConfiguracoesDoOtimizador_2")
        self.verticalLayout.addWidget(self.label_ConfiguracoesDoOtimizador_2)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.label_Topologia = QtWidgets.QLabel(self.layoutWidget)
        self.label_Topologia.setObjectName("label_Topologia")
        self.horizontalLayout_10.addWidget(self.label_Topologia)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)
        self.label_ConfiguracoesDoOtimizador_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_ConfiguracoesDoOtimizador_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ConfiguracoesDoOtimizador_3.setObjectName("label_ConfiguracoesDoOtimizador_3")
        self.verticalLayout.addWidget(self.label_ConfiguracoesDoOtimizador_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem6 = QtWidgets.QSpacerItem(121, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(30, 10))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label.setAcceptDrops(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(30, 10))
        self.label_2.setMaximumSize(QtCore.QSize(30, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(30, 10))
        self.label_3.setMaximumSize(QtCore.QSize(30, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_Vin_2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Vin_2.sizePolicy().hasHeightForWidth())
        self.label_Vin_2.setSizePolicy(sizePolicy)
        self.label_Vin_2.setMinimumSize(QtCore.QSize(121, 20))
        self.label_Vin_2.setMaximumSize(QtCore.QSize(121, 20))
        self.label_Vin_2.setObjectName("label_Vin_2")
        self.horizontalLayout_2.addWidget(self.label_Vin_2)
        self.input_Dmin = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_Dmin.setMinimumSize(QtCore.QSize(30, 20))
        self.input_Dmin.setMaximumSize(QtCore.QSize(30, 20))
        self.input_Dmin.setObjectName("input_Dmin")
        self.horizontalLayout_2.addWidget(self.input_Dmin)
        spacerItem10 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.input_D = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_D.setMinimumSize(QtCore.QSize(30, 20))
        self.input_D.setMaximumSize(QtCore.QSize(30, 20))
        self.input_D.setObjectName("input_D")
        self.horizontalLayout_2.addWidget(self.input_D)
        spacerItem11 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.input_Dmax = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_Dmax.setMinimumSize(QtCore.QSize(30, 20))
        self.input_Dmax.setMaximumSize(QtCore.QSize(30, 20))
        self.input_Dmax.setObjectName("input_Dmax")
        self.horizontalLayout_2.addWidget(self.input_Dmax)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_Vin = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Vin.sizePolicy().hasHeightForWidth())
        self.label_Vin.setSizePolicy(sizePolicy)
        self.label_Vin.setMinimumSize(QtCore.QSize(121, 20))
        self.label_Vin.setMaximumSize(QtCore.QSize(121, 20))
        self.label_Vin.setObjectName("label_Vin")
        self.horizontalLayout.addWidget(self.label_Vin)
        self.input_VinMin = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_VinMin.setMinimumSize(QtCore.QSize(30, 20))
        self.input_VinMin.setMaximumSize(QtCore.QSize(30, 20))
        self.input_VinMin.setObjectName("input_VinMin")
        self.horizontalLayout.addWidget(self.input_VinMin)
        spacerItem13 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem13)
        self.input_Vin = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_Vin.setMinimumSize(QtCore.QSize(30, 20))
        self.input_Vin.setMaximumSize(QtCore.QSize(30, 20))
        self.input_Vin.setObjectName("input_Vin")
        self.horizontalLayout.addWidget(self.input_Vin)
        spacerItem14 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem14)
        self.input_VinMax = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_VinMax.setMinimumSize(QtCore.QSize(30, 20))
        self.input_VinMax.setMaximumSize(QtCore.QSize(30, 20))
        self.input_VinMax.setObjectName("input_VinMax")
        self.horizontalLayout.addWidget(self.input_VinMax)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem15)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_Vo = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Vo.sizePolicy().hasHeightForWidth())
        self.label_Vo.setSizePolicy(sizePolicy)
        self.label_Vo.setMinimumSize(QtCore.QSize(121, 20))
        self.label_Vo.setMaximumSize(QtCore.QSize(121, 20))
        self.label_Vo.setObjectName("label_Vo")
        self.horizontalLayout_3.addWidget(self.label_Vo)
        self.input_Vo = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_Vo.setMaximumSize(QtCore.QSize(60, 20))
        self.input_Vo.setObjectName("input_Vo")
        self.horizontalLayout_3.addWidget(self.input_Vo)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem16)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_Vo_2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Vo_2.sizePolicy().hasHeightForWidth())
        self.label_Vo_2.setSizePolicy(sizePolicy)
        self.label_Vo_2.setMinimumSize(QtCore.QSize(121, 20))
        self.label_Vo_2.setMaximumSize(QtCore.QSize(121, 20))
        self.label_Vo_2.setObjectName("label_Vo_2")
        self.horizontalLayout_4.addWidget(self.label_Vo_2)
        self.input_Po = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_Po.setMaximumSize(QtCore.QSize(60, 20))
        self.input_Po.setObjectName("input_Po")
        self.horizontalLayout_4.addWidget(self.input_Po)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem17)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_DeltaIin = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_DeltaIin.sizePolicy().hasHeightForWidth())
        self.label_DeltaIin.setSizePolicy(sizePolicy)
        self.label_DeltaIin.setMinimumSize(QtCore.QSize(121, 20))
        self.label_DeltaIin.setMaximumSize(QtCore.QSize(121, 20))
        self.label_DeltaIin.setObjectName("label_DeltaIin")
        self.horizontalLayout_5.addWidget(self.label_DeltaIin)
        self.input_DeltaIin = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_DeltaIin.setMaximumSize(QtCore.QSize(60, 20))
        self.input_DeltaIin.setObjectName("input_DeltaIin")
        self.horizontalLayout_5.addWidget(self.input_DeltaIin)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem18)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_DeltaVo = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_DeltaVo.sizePolicy().hasHeightForWidth())
        self.label_DeltaVo.setSizePolicy(sizePolicy)
        self.label_DeltaVo.setMinimumSize(QtCore.QSize(121, 20))
        self.label_DeltaVo.setMaximumSize(QtCore.QSize(121, 20))
        self.label_DeltaVo.setObjectName("label_DeltaVo")
        self.horizontalLayout_6.addWidget(self.label_DeltaVo)
        self.input_DeltaVo = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_DeltaVo.setMaximumSize(QtCore.QSize(60, 20))
        self.input_DeltaVo.setObjectName("input_DeltaVo")
        self.horizontalLayout_6.addWidget(self.input_DeltaVo)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem19)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_JMax = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_JMax.sizePolicy().hasHeightForWidth())
        self.label_JMax.setSizePolicy(sizePolicy)
        self.label_JMax.setMinimumSize(QtCore.QSize(121, 20))
        self.label_JMax.setMaximumSize(QtCore.QSize(121, 20))
        self.label_JMax.setObjectName("label_JMax")
        self.horizontalLayout_7.addWidget(self.label_JMax)
        self.input_JMax = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_JMax.setMaximumSize(QtCore.QSize(60, 20))
        self.input_JMax.setObjectName("input_JMax")
        self.horizontalLayout_7.addWidget(self.input_JMax)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem20)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        spacerItem21 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem21)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem22)
        self.pushButtonCreateConverter = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonCreateConverter.setObjectName("pushButtonCreateConverter")
        self.horizontalLayout_9.addWidget(self.pushButtonCreateConverter)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem23)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem24)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem25)
        self.label_ConfiguracoesDoOtimizador = QtWidgets.QLabel(self.layoutWidget)
        self.label_ConfiguracoesDoOtimizador.setObjectName("label_ConfiguracoesDoOtimizador")
        self.horizontalLayout_12.addWidget(self.label_ConfiguracoesDoOtimizador)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem26)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        spacerItem27 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem27)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem28)
        self.pushButtonCapSel = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonCapSel.sizePolicy().hasHeightForWidth())
        self.pushButtonCapSel.setSizePolicy(sizePolicy)
        self.pushButtonCapSel.setMinimumSize(QtCore.QSize(120, 25))
        self.pushButtonCapSel.setMaximumSize(QtCore.QSize(120, 25))
        self.pushButtonCapSel.setObjectName("pushButtonCapSel")
        self.horizontalLayout_13.addWidget(self.pushButtonCapSel)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem29)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem30)
        self.pushButtonDiodeSel = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDiodeSel.sizePolicy().hasHeightForWidth())
        self.pushButtonDiodeSel.setSizePolicy(sizePolicy)
        self.pushButtonDiodeSel.setMinimumSize(QtCore.QSize(120, 25))
        self.pushButtonDiodeSel.setMaximumSize(QtCore.QSize(120, 25))
        self.pushButtonDiodeSel.setObjectName("pushButtonDiodeSel")
        self.horizontalLayout_14.addWidget(self.pushButtonDiodeSel)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem31)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem32)
        self.pushButtonSwitchSel = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSwitchSel.sizePolicy().hasHeightForWidth())
        self.pushButtonSwitchSel.setSizePolicy(sizePolicy)
        self.pushButtonSwitchSel.setMinimumSize(QtCore.QSize(120, 25))
        self.pushButtonSwitchSel.setMaximumSize(QtCore.QSize(120, 25))
        self.pushButtonSwitchSel.setObjectName("pushButtonSwitchSel")
        self.horizontalLayout_15.addWidget(self.pushButtonSwitchSel)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem33)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem34)
        self.pushButtonCableSel = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonCableSel.sizePolicy().hasHeightForWidth())
        self.pushButtonCableSel.setSizePolicy(sizePolicy)
        self.pushButtonCableSel.setMinimumSize(QtCore.QSize(120, 25))
        self.pushButtonCableSel.setMaximumSize(QtCore.QSize(120, 25))
        self.pushButtonCableSel.setObjectName("pushButtonCableSel")
        self.horizontalLayout_16.addWidget(self.pushButtonCableSel)
        spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem35)
        self.verticalLayout_3.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem36)
        self.pushButtonCoreSel = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonCoreSel.sizePolicy().hasHeightForWidth())
        self.pushButtonCoreSel.setSizePolicy(sizePolicy)
        self.pushButtonCoreSel.setMinimumSize(QtCore.QSize(120, 25))
        self.pushButtonCoreSel.setMaximumSize(QtCore.QSize(120, 25))
        self.pushButtonCoreSel.setObjectName("pushButtonCoreSel")
        self.horizontalLayout_17.addWidget(self.pushButtonCoreSel)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem37)
        self.verticalLayout_3.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem38)
        self.pushButtonDissSel = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDissSel.sizePolicy().hasHeightForWidth())
        self.pushButtonDissSel.setSizePolicy(sizePolicy)
        self.pushButtonDissSel.setMinimumSize(QtCore.QSize(120, 25))
        self.pushButtonDissSel.setMaximumSize(QtCore.QSize(120, 25))
        self.pushButtonDissSel.setObjectName("pushButtonDissSel")
        self.horizontalLayout_18.addWidget(self.pushButtonDissSel)
        spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem39)
        self.verticalLayout_3.addLayout(self.horizontalLayout_18)
        spacerItem40 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem40)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.optimize_button = QtWidgets.QPushButton(self.centralwidget)
        self.optimize_button.setGeometry(QtCore.QRect(550, 350, 75, 23))
        self.optimize_button.setObjectName("optimize_button")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 20, 521, 211))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../UDESC/2020 - Corona Vírus/Relatório 6 - Boost Bridgeless/Boost Half Bridge.png"))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 21))
        self.menubar.setObjectName("menubar")
        self.menuIn_cio = QtWidgets.QMenu(self.menubar)
        self.menuIn_cio.setObjectName("menuIn_cio")
        self.menuBiblioteca = QtWidgets.QMenu(self.menubar)
        self.menuBiblioteca.setObjectName("menuBiblioteca")
        self.menuAdd_Component = QtWidgets.QMenu(self.menuBiblioteca)
        self.menuAdd_Component.setObjectName("menuAdd_Component")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuAjuda = QtWidgets.QMenu(self.menubar)
        self.menuAjuda.setObjectName("menuAjuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSwitch = QtWidgets.QAction(MainWindow)
        self.actionSwitch.setObjectName("actionSwitch")
        self.actionDiode = QtWidgets.QAction(MainWindow)
        self.actionDiode.setObjectName("actionDiode")
        self.actionCapacitor = QtWidgets.QAction(MainWindow)
        self.actionCapacitor.setObjectName("actionCapacitor")
        self.actionCabl = QtWidgets.QAction(MainWindow)
        self.actionCabl.setObjectName("actionCabl")
        self.actionMagnetic_Core = QtWidgets.QAction(MainWindow)
        self.actionMagnetic_Core.setObjectName("actionMagnetic_Core")
        self.actionOtimizador = QtWidgets.QAction(MainWindow)
        self.actionOtimizador.setObjectName("actionOtimizador")
        self.actionSecurityConfig = QtWidgets.QAction(MainWindow)
        self.actionSecurityConfig.setObjectName("actionSecurityConfig")
        self.actionTransformador = QtWidgets.QAction(MainWindow)
        self.actionTransformador.setObjectName("actionTransformador")
        self.actionIndutor = QtWidgets.QAction(MainWindow)
        self.actionIndutor.setObjectName("actionIndutor")
        self.actionComo_funciona_o_otimizador = QtWidgets.QAction(MainWindow)
        self.actionComo_funciona_o_otimizador.setObjectName("actionComo_funciona_o_otimizador")
        self.actionComo_utilizar_o_otimizador = QtWidgets.QAction(MainWindow)
        self.actionComo_utilizar_o_otimizador.setObjectName("actionComo_utilizar_o_otimizador")
        self.actionCarregar_Arquivo = QtWidgets.QAction(MainWindow)
        self.actionCarregar_Arquivo.setObjectName("actionCarregar_Arquivo")
        self.actionComponentes = QtWidgets.QAction(MainWindow)
        self.actionComponentes.setObjectName("actionComponentes")
        self.menuIn_cio.addAction(self.actionNew)
        self.menuIn_cio.addAction(self.actionOpen)
        self.menuIn_cio.addAction(self.actionSave)
        self.menuAdd_Component.addAction(self.actionSwitch)
        self.menuAdd_Component.addAction(self.actionDiode)
        self.menuAdd_Component.addAction(self.actionCapacitor)
        self.menuAdd_Component.addAction(self.actionCabl)
        self.menuAdd_Component.addAction(self.actionMagnetic_Core)
        self.menuAdd_Component.addAction(self.actionTransformador)
        self.menuAdd_Component.addAction(self.actionIndutor)
        self.menuBiblioteca.addAction(self.menuAdd_Component.menuAction())
        self.menuBiblioteca.addAction(self.actionCarregar_Arquivo)
        self.menuSettings.addAction(self.actionOtimizador)
        self.menuSettings.addAction(self.actionSecurityConfig)
        self.menuAjuda.addAction(self.actionComo_funciona_o_otimizador)
        self.menuAjuda.addAction(self.actionComo_utilizar_o_otimizador)
        self.menubar.addAction(self.menuIn_cio.menuAction())
        self.menubar.addAction(self.menuBiblioteca.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_ConfiguracoesDoOtimizador_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Configuração do Conversor</span></p></body></html>"))
        self.label_Topologia.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Topologia</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Boost Half Bridge"))
        self.label_ConfiguracoesDoOtimizador_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Parâmetros Desejáveis</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Min"))
        self.label_2.setText(_translate("MainWindow", "Nom"))
        self.label_3.setText(_translate("MainWindow", "Max"))
        self.label_Vin_2.setText(_translate("MainWindow", "Razão Cíclica"))
        self.label_Vin.setText(_translate("MainWindow", "Tensão de Entrada (V)"))
        self.label_Vo.setText(_translate("MainWindow", "Tensão de Saída (V)"))
        self.label_Vo_2.setText(_translate("MainWindow", "Potência de Saída (W)"))
        self.label_DeltaIin.setText(_translate("MainWindow", "DeltaIinMax (%)"))
        self.label_DeltaVo.setText(_translate("MainWindow", "DeltaVoMax (%)"))
        self.label_JMax.setText(_translate("MainWindow", "JMax (A/m2)"))
        self.pushButtonCreateConverter.setText(_translate("MainWindow", "Salvar Parâmetros"))
        self.label_ConfiguracoesDoOtimizador.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Escolha dos Componentes</span></p></body></html>"))
        self.pushButtonCapSel.setText(_translate("MainWindow", "Escolher Capacitores"))
        self.pushButtonDiodeSel.setText(_translate("MainWindow", "Escolher Diodos"))
        self.pushButtonSwitchSel.setText(_translate("MainWindow", "Escolher Chaves"))
        self.pushButtonCableSel.setText(_translate("MainWindow", "Escolher Cabos"))
        self.pushButtonCoreSel.setText(_translate("MainWindow", "Escolher Núcleos"))
        self.pushButtonDissSel.setText(_translate("MainWindow", "Escolher Dissipadores"))
        self.optimize_button.setText(_translate("MainWindow", "Otimizar"))
        self.menuIn_cio.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuBiblioteca.setTitle(_translate("MainWindow", "Biblioteca"))
        self.menuAdd_Component.setTitle(_translate("MainWindow", "Adicionar Componente"))
        self.menuSettings.setTitle(_translate("MainWindow", "Configurações"))
        self.menuAjuda.setTitle(_translate("MainWindow", "Ajuda"))
        self.actionNew.setText(_translate("MainWindow", "Criar nova otimização"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Carregar parâmetros"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Salvar parâmetros"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSwitch.setText(_translate("MainWindow", "Switch"))
        self.actionDiode.setText(_translate("MainWindow", "Diode"))
        self.actionCapacitor.setText(_translate("MainWindow", "Capacitor"))
        self.actionCabl.setText(_translate("MainWindow", "Fio"))
        self.actionMagnetic_Core.setText(_translate("MainWindow", "Núcleo Magnético"))
        self.actionOtimizador.setText(_translate("MainWindow", "Otimizador"))
        self.actionSecurityConfig.setText(_translate("MainWindow", "Fatores de Seguraça"))
        self.actionTransformador.setText(_translate("MainWindow", "Transformador"))
        self.actionIndutor.setText(_translate("MainWindow", "Indutor"))
        self.actionComo_funciona_o_otimizador.setText(_translate("MainWindow", "Como funciona o otimizador?"))
        self.actionComo_utilizar_o_otimizador.setText(_translate("MainWindow", "Como utilizar o otimizador?"))
        self.actionCarregar_Arquivo.setText(_translate("MainWindow", "Carregar Arquivo"))
        self.actionComponentes.setText(_translate("MainWindow", "Componentes"))
from mplwidget import MplWidget
