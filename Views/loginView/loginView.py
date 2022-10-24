from PyQt5 import QtWidgets, QtGui
from PyQt5.uic import loadUi


class loginView(QtWidgets.QMainWindow):
    def __init__(self):
        super(loginView, self).__init__()
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

        # -- Настройка кнопок
        self.loginButton.setFont(
            QtGui.QFont('SansSerif', 14)
        )

    def setVersion(self, version):
        """Установка версии в label version"""
        self.version.setText(version)
