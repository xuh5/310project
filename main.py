from PyQt5.QtWidgets import  QApplication, QMainWindow,QMessageBox
from PyQt5 import QtCore, QtGui
import login
import sys
import main_ui
import client
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= login.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.widget_3.hide()
        self.ui.pushButton_1.clicked.connect(self.change_widget2)
        self.ui.pushButton_2.clicked.connect(self.change_widget3)
        self.ui.pushButton_3.clicked.connect(self.login_in)
        self.ui.pushButton_5.clicked.connect(self.register)
        self.show()
    def register(self):
        email= self.ui.lineEdit_3.text()
        username = self.ui.lineEdit_5.text()
        password = self.ui.lineEdit_4.text()
        try_register =client.add_user({"username":username,"email":email,"password":password})
        if(try_register[0]):
            self.show_notification(try_register[1]['message'],"registered successfully, plz remeber your userid: "
                                   +str(try_register[1]['userid']))
        else:
            self.show_notification("register Failed", try_register[1]['message'])
    def login_in(self):
        account = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        try_login=client.login({"userid":account,"password":password})
        if(try_login[0]):
            self.win = MainWindow(account)
            self.close()
        else:
            self.show_notification("Login Failed",try_login[1]['message'])

    def show_notification(self, title, message):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec_()
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def change_widget3(self):
        self.ui.widget_2.hide()
        self.ui.widget_3.show()
    def change_widget2(self):
        self.ui.widget_3.hide()
        self.ui.widget_2.show()
class MainWindow(QMainWindow):
    def __init__(self,id):
        super().__init__()
        self.ui= main_ui.Ui_MainWindow()
        self.ui.setupUi(self,id)
    # xhc_write
        self.ui.search_button.clicked.connect(self.switchsearch)
        self.ui.like_button.clicked.connect(self.switchlike)
        self.ui.comments_button.clicked.connect(self.switchcomment)
        self.ui.favourite_button.clicked.connect(self.swithfavourite)

        self.show()
    def switchsearch(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def switchlike(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def switchcomment(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    def swithfavourite(self):
        self.ui.stackedWidget.setCurrentIndex(4)
    ######


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWindow()
    sys.exit(app.exec_())
