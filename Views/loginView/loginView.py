from PyQt5 import QtWidgets, QtGui
from PyQt5.uic import loadUi

from Views.dialogs.dialogValid import dialogValid
from Views.mainView.mainView import mainView


class loginView(QtWidgets.QMainWindow):
    def __init__(self):
        super(loginView, self).__init__()
        self.p = None
        self.widget = None
        loadUi("Views\loginView\loginView.ui", self)
        self.setWindowTitle('Вход - АБИС')
        # -- Настройка надписей --
        self.version.setFont(
            QtGui.QFont('SansSerif', 14)
        )
        self.loginLable.setFont(
            QtGui.QFont('SansSerif', 28)
        )

        # -- Настройка полей ввода --
        self.loginName.setText('Имя пользователя')
        self.loginName.setReadOnly(False)
        self.loginPassword.setText('Пароль')
        self.loginPassword.setReadOnly(False)

        # -- Настройка кнопок --
        self.loginButton.setFont(
            QtGui.QFont('SansSerif', 14)
        )
        self.loginButton.clicked.connect(self.loginBtnClicked)

        self.gSignButton.setFont(
            QtGui.QFont('SansSerif', 18)
        )
        self.gSignButton.clicked.connect(self.gSignButtonClicked)

    def setVersion(self, version):
        """Установка версии в label version"""
        self.version.setText(version)

    def setWidget(self, widget):
        self.widget = widget

    def loginBtnClicked(self):
        """Обработка нажатия на кнопку 'Войти'"""
        temp = self.loginName.text() + ',' + self.loginPassword.text()
        found = False
        with open('users.txt', 'r') as file:
            for line in file:
                if temp in line:
                    found = True
                    print('[INFO] Пользователь найден')
                    cringe = line.split(',')
                    self.user.setData(cringe[0], cringe[1], cringe[2])
                    self.mainWindow = mainView()
                    self.widget.addWidget(self.mainWindow)
                    self.mainWindow.setWidget(self.widget)
                    self.mainWindow.setServer(self.server)
                    self.mainWindow.setUser(self.user)
                    self.mainWindow.setupUI()
                    self.mainWindow.loadProfile()
                    self.widget.setCurrentIndex(2)
                    break
        if not found:
            self.p = dialogValid()
            self.p.show()
            self.p.setupUI()

    def gSignButtonClicked(self):
        """Обработка нажатия на кнопку 'Перейти к регистрации'"""
        self.widget.setCurrentIndex(1)

    def setUser(self, user):
        self.user = user

    def setServer(self, server):
        self.server = server
