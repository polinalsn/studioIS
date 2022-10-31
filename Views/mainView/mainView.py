from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QFont
from PyQt5.uic import loadUi


class mainView(QtWidgets.QMainWindow):
    def __int__(self):
        super(mainView, self).__init__()

    def setWidget(self, widget):
        self.widget = widget

    def setUser(self, user):
        self.user = user

    def loadProfile(self):
        # -- Настройка надписей --
        self.nameLabel.setFont(
            QtGui.QFont('SansSerif', 18, QFont.Bold)
        )
        self.roleLabel.setFont(
            QtGui.QFont('SansSerif', 18, QFont.Bold)
        )
        self.nameText.setFont(
           QtGui.QFont('SansSerif', 18)
        )
        self.roleText.setFont(
            QtGui.QFont('SansSerif', 18)
        )
        self.nameText.setText(self.user.name)
        match self.user.role:
            case 'user\n':
                self.roleText.setText('Пользователь')
            case 'admin\n':
                self.roleText.setText('Администратор')
        print(self.user.name)
        print(self.user.role)

    def setupUI(self):
        loadUi("Views\mainView\mainView.ui", self)
        self.tabWidget.setTabText(0, 'Профиль')
