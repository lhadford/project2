# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Project2(object):
    def setupUi(self, Project2):
        Project2.setObjectName("Project2")
        Project2.resize(600, 700)
        Project2.setMinimumSize(QtCore.QSize(600, 700))
        Project2.setMaximumSize(QtCore.QSize(600, 700))
        self.widget = QtWidgets.QWidget(parent=Project2)
        self.widget.setObjectName("widget")
        self.labelMenu = QtWidgets.QLabel(parent=self.widget)
        self.labelMenu.setGeometry(QtCore.QRect(194, 5, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelMenu.setFont(font)
        self.labelMenu.setObjectName("labelMenu")
        self.labelDiscription = QtWidgets.QLabel(parent=self.widget)
        self.labelDiscription.setGeometry(QtCore.QRect(80, 70, 471, 16))
        self.labelDiscription.setObjectName("labelDiscription")
        self.radioButtonLogin = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButtonLogin.setGeometry(QtCore.QRect(150, 320, 95, 20))
        self.radioButtonLogin.setObjectName("radioButtonLogin")
        self.buttonGroup = QtWidgets.QButtonGroup(Project2)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButtonLogin)
        self.radioButtonSignup = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButtonSignup.setGeometry(QtCore.QRect(350, 320, 95, 20))
        self.radioButtonSignup.setObjectName("radioButtonSignup")
        self.buttonGroup.addButton(self.radioButtonSignup)
        self.ButtonSubmit = QtWidgets.QPushButton(parent=self.widget)
        self.ButtonSubmit.setGeometry(QtCore.QRect(200, 390, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ButtonSubmit.setFont(font)
        self.ButtonSubmit.setObjectName("ButtonSubmit")
        self.lineName = QtWidgets.QLineEdit(parent=self.widget)
        self.lineName.setGeometry(QtCore.QRect(170, 140, 261, 41))
        self.lineName.setAutoFillBackground(True)
        self.lineName.setInputMask("")
        self.lineName.setObjectName("lineName")
        self.labelName = QtWidgets.QLabel(parent=self.widget)
        self.labelName.setGeometry(QtCore.QRect(40, 150, 111, 31))
        self.labelName.setObjectName("labelName")
        self.labelPin = QtWidgets.QLabel(parent=self.widget)
        self.labelPin.setGeometry(QtCore.QRect(40, 220, 101, 41))
        self.labelPin.setObjectName("labelPin")
        self.linePin = QtWidgets.QLineEdit(parent=self.widget)
        self.linePin.setGeometry(QtCore.QRect(170, 220, 261, 41))
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.linePin.setFont(font)
        self.linePin.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.linePin.setObjectName("linePin")
        self.radioButtonEnterAccount = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButtonEnterAccount.setGeometry(QtCore.QRect(230, 320, 111, 20))
        self.radioButtonEnterAccount.setObjectName("radioButtonEnterAccount")
        self.buttonGroup.addButton(self.radioButtonEnterAccount)
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(50, 110, 321, 16))
        self.label.setObjectName("label")
        self.radioButtonExit = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButtonExit.setGeometry(QtCore.QRect(480, 30, 95, 20))
        self.radioButtonExit.setObjectName("radioButtonExit")
        self.buttonGroup.addButton(self.radioButtonExit)
        Project2.setCentralWidget(self.widget)
        self.menubar = QtWidgets.QMenuBar(parent=Project2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        Project2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Project2)
        self.statusbar.setObjectName("statusbar")
        Project2.setStatusBar(self.statusbar)

        self.retranslateUi(Project2)
        QtCore.QMetaObject.connectSlotsByName(Project2)

    def retranslateUi(self, Project2):
        _translate = QtCore.QCoreApplication.translate
        Project2.setWindowTitle(_translate("Project2", "MainWindow"))
        self.labelMenu.setText(_translate("Project2", "Bank Account"))
        self.labelDiscription.setText(_translate("Project2", "Welcome please either login or sign up for an account"))
        self.radioButtonLogin.setText(_translate("Project2", "Login"))
        self.radioButtonSignup.setText(_translate("Project2", "Sign up"))
        self.ButtonSubmit.setText(_translate("Project2", "SUBMIT"))
        self.labelName.setText(_translate("Project2", "Enter Name"))
        self.labelPin.setText(_translate("Project2", "Enter PIN"))
        self.radioButtonEnterAccount.setText(_translate("Project2", "Enter Account"))
        self.label.setText(_translate("Project2", "Current Balance:"))
        self.radioButtonExit.setText(_translate("Project2", "Exit Account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Project2 = QtWidgets.QMainWindow()
    ui = Ui_Project2()
    ui.setupUi(Project2)
    Project2.show()
    sys.exit(app.exec())