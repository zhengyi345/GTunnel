# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gtunnel.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_GTunnel(object):
    def setupUi(self, GTunnel):
        if not GTunnel.objectName():
            GTunnel.setObjectName(u"GTunnel")
        GTunnel.setEnabled(True)
        GTunnel.resize(322, 232)
        GTunnel.setMinimumSize(QSize(322, 229))
        GTunnel.setMaximumSize(QSize(322, 232))
        self.groupBox = QGroupBox(GTunnel)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 10, 281, 185))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(275, 185))
        font = QFont()
        font.setFamily(u"\u5b8b\u4f53")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setToolTipDuration(-1)
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(110, 70))
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font1.setPointSize(12)
        self.pushButton.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButton)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.label_5)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(110, 70))
        self.pushButton_2.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 16))

        self.verticalLayout.addWidget(self.label_6)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(45, 16777215))
        self.pushButton_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_3 = QLabel(GTunnel)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(25, 200, 271, 20))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(10)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.retranslateUi(GTunnel)
        self.pushButton.clicked.connect(GTunnel.RunSer)
        self.pushButton_3.clicked.connect(GTunnel.LoadFile)
        self.pushButton_2.clicked.connect(GTunnel.StopSer)

        QMetaObject.connectSlotsByName(GTunnel)
    # setupUi

    def retranslateUi(self, GTunnel):
        GTunnel.setWindowTitle(QCoreApplication.translate("GTunnel", u"GTunnel", None))
        self.groupBox.setTitle(QCoreApplication.translate("GTunnel", u"v1.0", None))
        self.pushButton.setText(QCoreApplication.translate("GTunnel", u"\u670d\u52a1\u542f\u52a8", None))
        self.label_5.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("GTunnel", u"\u505c\u6b62\u670d\u52a1", None))
        self.label_6.setText("")
        self.label.setText(QCoreApplication.translate("GTunnel", u"\u52a0\u8f7d\u914d\u7f6e\u6587\u4ef6\uff1a", None))
        self.pushButton_3.setText(QCoreApplication.translate("GTunnel", u"...", None))
        self.label_2.setText(QCoreApplication.translate("GTunnel", u"\u672a\u52a0\u8f7d", None))
        self.label_3.setText(QCoreApplication.translate("GTunnel", u"stopped", None))
    # retranslateUi

