from PyQt5 import QtWidgets, QtGui
from PyQt5.uic import loadUi


class mainView(QtWidgets.QMainWindow):
    def __int__(self):
        super(mainView, self).__init__()
        loadUi("Views\mainView\mainView.ui", self)
        #self.loadProfile()

    def setWidget(self, widget):
        self.widget = widget

    def setUser(self, user):
        self.user = user

    def loadProfile(self):
        # -- Настройка надписей --
        self.nameLabel.setFont(
            QtGui.QFont('SansSerif', 18)
        )
        self.nameText.setFont(
            QtGui.QFont('SansSerif', 18)
        )
        self.nameText.setText(self.user.name)
