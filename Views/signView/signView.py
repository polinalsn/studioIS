from PyQt5 import QtWidgets, QtGui
from PyQt5.uic import loadUi

from Views.dialogs.dialogValid import dialogValid
from Views.mainView.mainView import mainView


class signView(QtWidgets.QMainWindow):
    def __init__(self):
        super(signView, self).__init__()
        loadUi("Views\signView\signView.ui", self)
        # -- Настройка надписей --
        self.version.setFont(
            QtGui.QFont('SansSerif', 14)
        )
        self.signLable.setFont(
            QtGui.QFont('SansSerif', 28)
        )

        # -- Настройка полей ввода --
        self.signName.setText('Имя пользователя')
        self.signName.setReadOnly(False)
        self.signPassword.setText('Пароль')
        self.signPassword.setReadOnly(False)

        # -- Настройка кнопок --
        self.signButton.setFont(
            QtGui.QFont('SansSerif', 14)
        )
        self.signButton.clicked.connect(self.signBtnClicked)

        self.gLoginButton.setFont(
            QtGui.QFont('SansSerif', 18)
        )
        self.gLoginButton.clicked.connect(self.gLoginButtonClicked)

    def setWidget(self, widget):
        self.widget = widget

    def setVersion(self, version):
        """Установка версии в label version"""
        self.version.setText(version)

    def signBtnClicked(self):
        if self.valid(self.signName.text()) and self.valid(self.signPassword.text()):
            with open('users.txt', 'a') as file:
                file.write(self.signName.text() + ',' + self.signPassword.text() + ',' + 'user\n')
                self.user.setData(self.signName.text(), self.signPassword.text(), 'user')
                self.widget.setCurrentIndex(2)
                self.mainWindow = mainView()
                self.widget.addWidget(self.mainWindow)
                self.mainWindow.setWidget(self.widget)
                self.mainWindow.setUser(self.user)
                self.mainWindow.setupUI()
                self.mainWindow.loadProfile()
                self.widget.setCurrentIndex(2)
        else:
            self.push = dialogValid()
            self.push.show()
            self.push.setupUI()

    def gLoginButtonClicked(self):
        self.widget.setCurrentIndex(0)

    def valid(self, name):
        if '!' in name or '@' in name or '#' in name or '$' in name or '^' in name or '&' in name or '*' in name or '(' \
                in name or ')' in name or '"' in name or '№' in name or ';' in name or ':' in name or '?' in name or ' ' in name:
            return False
        else:
            return True

    def setUser(self, user):
        self.user = user

