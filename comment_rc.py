# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comment.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import random

import client
import resource_rc

class Ui_Form(QtWidgets.QWidget):
    def __init__(self, data,main_UI=None,buttonon=True):
        super(Ui_Form, self).__init__()
        self.setupUi(data,main_UI,buttonon)

    def setupUi(self, data,main_UI=None,buttonon=True):
        self.main_UI=main_UI
        # Adding a random True or False value to data
        self.setObjectName("Ui_Form")
        self.resize(591, 482)
        self.ID= data['ReviewID']
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        self.widget_3 = QtWidgets.QWidget(self)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 158))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.widget = QtWidgets.QWidget(self.widget_3)
        self.widget.setMaximumSize(QtCore.QSize(100, 100))
        self.widget.setObjectName("widget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setMinimumSize(QtCore.QSize(50, 50))
        self.label_16.setMaximumSize(QtCore.QSize(50, 50))
        self.label_16.setAutoFillBackground(False)
        self.label_16.setText("")
        self.label_16.setTextFormat(QtCore.Qt.PlainText)
        self.label_16.setPixmap(QtGui.QPixmap(":/icons/icons/icon.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_8.addWidget(self.label_16)

        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setMaximumSize(QtCore.QSize(50, 50))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_8.addWidget(self.label_17)
        self.horizontalLayout_3.addWidget(self.widget)

        self.widget_2 = QtWidgets.QWidget(self.widget_3)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName("verticalLayout_10")

        self.label_18 = QtWidgets.QLabel(self.widget_2)
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_18.setObjectName("label_18")
        self.verticalLayout_10.addWidget(self.label_18)

        self.label_19 = QtWidgets.QLabel(self.widget_2)
        self.label_19.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_19.setWordWrap(True)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_10.addWidget(self.label_19)
        self.horizontalLayout_3.addWidget(self.widget_2)

        self.verticalLayout_7.addWidget(self.widget_3)

        self.widget_4 = QtWidgets.QWidget(self)
        self.widget_4.setMinimumSize(QtCore.QSize(200, 200))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        spacerItem = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)

        self.label_20 = QtWidgets.QLabel(self.widget_4)
        self.label_20.setMinimumSize(QtCore.QSize(0, 0))
        self.label_20.setMaximumSize(QtCore.QSize(400, 300))
        self.label_20.setText("")
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_4.addWidget(self.label_20)
        self.verticalLayout_7.addWidget(self.widget_4)

        self.widget_5 = QtWidgets.QWidget(self)
        self.widget_5.setMinimumSize(QtCore.QSize(50, 0))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        #####setting likebutton
        self.pushButton = QtWidgets.QToolButton(self.widget_5)
        self.pushButton.setText("")
        self.pushButton.setCheckable(True)  # Make the button checkable
        self.pushButton.setChecked(buttonon)  # Set the initial state
        self.checked_image = QtGui.QPixmap(":/icons/icons/like_t.png")
        self.unchecked_image = QtGui.QPixmap(":/icons/icons/like.png")
        self.pushButton.toggled.connect(self.checkPrecondition)
        self.Buttoninitialize()
        self.pushButton.setObjectName("pushButton")

        self.horizontalLayout_5.addWidget(self.pushButton)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)

        self.label_27 = QtWidgets.QLabel(self.widget_5)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_5.addWidget(self.label_27)

        self.label_28 = QtWidgets.QLabel(self.widget_5)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_5.addWidget(self.label_28)

        self.verticalLayout_7.addWidget(self.widget_5)


        self.retranslateUi(data)

    def retranslateUi(self, data):

        _translate = QtCore.QCoreApplication.translate

        self.setWindowTitle(_translate("Ui_Form", "Form"))
        self.label_17.setText(_translate("Ui_Form", str(data['Username'])))
        self.label_18.setText(_translate("Ui_Form", data['Title']))
        self.label_19.setText(_translate("Ui_Form", data['ReviewText']))
        self.label_27.setText(_translate("Ui_Form", 'Rate:'+str(data['Rating'])))
        if(data['ImageURL']!="" and data['ImageURL']!=None ):
            self.label_20.setPixmap(QtGui.QPixmap(data['ImageURL'] ))
        self.label_28.setText(_translate("Ui_Form",data['ReviewDate']))

    def checkPrecondition(self, checked):
        if not self.shouldToggle(checked):
            self.pushButton.blockSignals(True)
            self.pushButton.setChecked(not checked)
            self.pushButton.blockSignals(False)
        else:
            self.changeImage(checked)

    def shouldToggle(self,checked):
        if(checked):
            tmp_result = client.like_review({"userid":self.main_UI.id,'reviewid':self.ID})
        else:
            tmp_result = client.unlike_review({"userid":self.main_UI.id,'reviewid':self.ID})
        return tmp_result[0]

    def Buttoninitialize(self):
        icon = QtGui.QIcon()
        if self.pushButton.isChecked():
            icon.addPixmap(self.checked_image, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        else:
            icon.addPixmap(self.unchecked_image, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)

    def changeImage(self,state):
        icon = QtGui.QIcon()
        if state:
            icon.addPixmap(self.checked_image, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        else:
            icon.addPixmap(self.unchecked_image, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)



