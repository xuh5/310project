# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import comment_rc
import json
import movie_info_rc
import review_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(967, 734)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.up_widget = QtWidgets.QWidget(self.centralwidget)
        self.up_widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.up_widget.setStyleSheet("background-color: rgb(108, 108, 108);")
        self.up_widget.setObjectName("up_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.up_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.Title = QtWidgets.QLabel(self.up_widget)
        self.Title.setStyleSheet("font: 16pt \"Times New Roman\";")
        self.Title.setObjectName("Title")
        self.horizontalLayout_2.addWidget(self.Title)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.up_widget)
        self.down_widget = QtWidgets.QWidget(self.centralwidget)
        self.down_widget.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.down_widget.setObjectName("down_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.down_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu = QtWidgets.QWidget(self.down_widget)
        self.menu.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.menu.setObjectName("menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menu)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 300)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.search_button = QtWidgets.QPushButton(self.menu)
        self.search_button.setMaximumSize(QtCore.QSize(200, 50))
        self.search_button.setObjectName("search_button")
        self.verticalLayout_2.addWidget(self.search_button)
        self.like_button = QtWidgets.QPushButton(self.menu)
        self.like_button.setMaximumSize(QtCore.QSize(200, 50))
        self.like_button.setObjectName("like_button")
        self.verticalLayout_2.addWidget(self.like_button)
        self.comments_button = QtWidgets.QPushButton(self.menu)
        self.comments_button.setMaximumSize(QtCore.QSize(200, 50))
        self.comments_button.setObjectName("comments_button")
        self.verticalLayout_2.addWidget(self.comments_button)
        self.favourite_button = QtWidgets.QPushButton(self.menu)
        self.favourite_button.setMaximumSize(QtCore.QSize(200, 50))
        self.favourite_button.setObjectName("favourite_button")
        self.verticalLayout_2.addWidget(self.favourite_button)
        self.horizontalLayout.addWidget(self.menu)
        self.stackedWidget = QtWidgets.QStackedWidget(self.down_widget)
        self.stackedWidget.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.search_page = QtWidgets.QWidget()
        self.search_page.setObjectName("search_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.search_page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.searchandfilter = QtWidgets.QGridLayout()
        self.searchandfilter.setObjectName("searchandfilter")
        self.review_comboBox = QtWidgets.QComboBox(self.search_page)
        self.review_comboBox.setObjectName("review_comboBox")
        self.searchandfilter.addWidget(self.review_comboBox, 2, 1, 1, 1)
        self.Genre_label = QtWidgets.QLabel(self.search_page)
        self.Genre_label.setObjectName("Genre_label")
        self.searchandfilter.addWidget(self.Genre_label, 2, 0, 1, 1)
        self.name_label = QtWidgets.QLabel(self.search_page)
        self.name_label.setObjectName("name_label")
        self.searchandfilter.addWidget(self.name_label, 0, 0, 1, 1)
        self.rate_spinBox = QtWidgets.QSpinBox(self.search_page)
        self.rate_spinBox.setObjectName("rate_spinBox")
        self.searchandfilter.addWidget(self.rate_spinBox, 1, 2, 1, 1)
        self.searchbar = QtWidgets.QLineEdit(self.search_page)
        self.searchbar.setObjectName("searchbar")
        self.searchandfilter.addWidget(self.searchbar, 0, 1, 1, 1)
        self.rate_label = QtWidgets.QLabel(self.search_page)
        self.rate_label.setObjectName("rate_label")
        self.searchandfilter.addWidget(self.rate_label, 1, 0, 1, 1)
        self.language_comboBox = QtWidgets.QComboBox(self.search_page)
        self.language_comboBox.setObjectName("language_comboBox")
        self.searchandfilter.addWidget(self.language_comboBox, 3, 1, 1, 1)
        self.language_label = QtWidgets.QLabel(self.search_page)
        self.language_label.setObjectName("language_label")
        self.searchandfilter.addWidget(self.language_label, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.search_page)
        self.label.setObjectName("label")
        self.searchandfilter.addWidget(self.label, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.searchandfilter.addItem(spacerItem2, 0, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.searchandfilter)
        self.submit_pushButton = QtWidgets.QPushButton(self.search_page)
        self.submit_pushButton.setObjectName("submit_pushButton")
        self.verticalLayout_3.addWidget(self.submit_pushButton)
        self.scrollArea = QtWidgets.QScrollArea(self.search_page)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 799, 490))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.search_page)
        self.information_page = QtWidgets.QWidget()
        self.information_page.setObjectName("information_page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.information_page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.movie_widget = QtWidgets.QWidget(self.information_page)
        self.movie_widget.setObjectName("movie_widget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.movie_widget)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.movie_gridLayout_2 = QtWidgets.QGridLayout()
        self.movie_gridLayout_2.setObjectName("movie_gridLayout_2")
        self.language_2 = QtWidgets.QLabel(self.movie_widget)
        self.language_2.setObjectName("language_2")
        self.movie_gridLayout_2.addWidget(self.language_2, 0, 2, 1, 1)
        self.review_num_2 = QtWidgets.QLabel(self.movie_widget)
        self.review_num_2.setObjectName("review_num_2")
        self.movie_gridLayout_2.addWidget(self.review_num_2, 1, 0, 1, 1)
        self.rate_2 = QtWidgets.QLabel(self.movie_widget)
        self.rate_2.setObjectName("rate_2")
        self.movie_gridLayout_2.addWidget(self.rate_2, 1, 1, 1, 1)
        self.genre_2 = QtWidgets.QLabel(self.movie_widget)
        self.genre_2.setObjectName("genre_2")
        self.movie_gridLayout_2.addWidget(self.genre_2, 0, 1, 1, 1)
        self.name_2 = QtWidgets.QLabel(self.movie_widget)
        self.name_2.setObjectName("name_2")
        self.movie_gridLayout_2.addWidget(self.name_2, 0, 0, 1, 1)
        self.collect_widget_2 = QtWidgets.QWidget(self.movie_widget)
        self.collect_widget_2.setObjectName("collect_widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.collect_widget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(115, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.collect_icon_2 = QtWidgets.QLabel(self.collect_widget_2)
        self.collect_icon_2.setMaximumSize(QtCore.QSize(20, 20))
        self.collect_icon_2.setText("")
        self.collect_icon_2.setPixmap(QtGui.QPixmap(":/icons/icons/favor.png"))
        self.collect_icon_2.setScaledContents(True)
        self.collect_icon_2.setObjectName("collect_icon_2")
        self.horizontalLayout_4.addWidget(self.collect_icon_2)
        self.movie_gridLayout_2.addWidget(self.collect_widget_2, 1, 2, 1, 1)
        self.verticalLayout_11.addLayout(self.movie_gridLayout_2)
        self.verticalLayout_6.addWidget(self.movie_widget)
        self.Review_title = QtWidgets.QLabel(self.information_page)
        self.Review_title.setObjectName("Review_title")
        self.verticalLayout_6.addWidget(self.Review_title)
        self.review_scrollArea = QtWidgets.QScrollArea(self.information_page)
        self.review_scrollArea.setWidgetResizable(True)
        self.review_scrollArea.setObjectName("review_scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 799, 516))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.review_scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.addWidget(self.review_scrollArea)
        self.stackedWidget.addWidget(self.information_page)
        self.like_page = QtWidgets.QWidget()
        self.like_page.setObjectName("like_page")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.like_page)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.like_page)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 799, 633))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        #load like page comments
        self.vertical_like_page = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.vertical_like_page.setObjectName("vertical_like_page")
        self.loadui(self.scrollAreaWidgetContents_3,self.vertical_like_page,0)
        ######################
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_9.addWidget(self.scrollArea_2)
        self.stackedWidget.addWidget(self.like_page)
        self.comments_page = QtWidgets.QWidget()
        self.comments_page.setObjectName("comments_page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.comments_page)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.comments_page)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 799, 633))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        #load comment page comments:
        self.vertical_comment_page = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.vertical_comment_page.setObjectName("vertical_comment_page")
        self.loadui(self.scrollAreaWidgetContents_4,self.vertical_comment_page,0)
        ###############
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_7.addWidget(self.scrollArea_3)
        self.stackedWidget.addWidget(self.comments_page)
        self.favourite_page = QtWidgets.QWidget()
        self.favourite_page.setObjectName("favourite_page")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.favourite_page)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.favourite_page)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 799, 633))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        ##########load
        self.vertical_favor_page = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.vertical_favor_page.setObjectName("vertical_favor_page")
        self.loadui(self.scrollAreaWidgetContents_5,self.vertical_favor_page,1)
        #############
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayout_8.addWidget(self.scrollArea_4)
        self.stackedWidget.addWidget(self.favourite_page)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.down_widget)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 15)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "MOVIE COMMENTS"))
        self.search_button.setText(_translate("MainWindow", "search"))
        self.like_button.setText(_translate("MainWindow", "like"))
        self.comments_button.setText(_translate("MainWindow", "comments"))
        self.favourite_button.setText(_translate("MainWindow", "favourite"))
        self.Genre_label.setText(_translate("MainWindow", "Genre:"))
        self.name_label.setText(_translate("MainWindow", "Name:"))
        self.rate_label.setText(_translate("MainWindow", "Rate:"))
        self.language_label.setText(_translate("MainWindow", "Language:   "))
        self.label.setText(_translate("MainWindow", "greater than"))
        self.submit_pushButton.setText(_translate("MainWindow", "SUBMIT"))
        self.language_2.setText(_translate("MainWindow", "language"))
        self.review_num_2.setText(_translate("MainWindow", "review_num"))
        self.rate_2.setText(_translate("MainWindow", "rate"))
        self.genre_2.setText(_translate("MainWindow", "genre"))
        self.name_2.setText(_translate("MainWindow", "name"))
        self.Review_title.setText(_translate("MainWindow", "Review"))
    def loadui(self,page,layout_,choice=0):
        filepath =['output.json','movie_information.json']
        with open(filepath[choice], 'r') as json_file:
            data = json.load(json_file)
        value_length = len(next(iter(data.values())))
        # Create a list for each index
        result_lists = [[] for _ in range(value_length)]
        # Populate the lists
        for key, values in data.items():
            for index, value in enumerate(values):
                result_lists[index].append(value)
        #####chose which UI to load
        uioption= [comment_rc,movie_info_rc,review_rc]
        # datastructure : rating, reviewtext,review date,image_url
        for i in range(10):  # Adjust the number of instances as needed
            ui_added = uioption[choice].Ui_Form(result_lists[i])
            layout_.addWidget(ui_added)

import resource_rc
