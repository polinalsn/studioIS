from PyQt5 import QtWidgets, QtGui
from PyQt5.uic import loadUi


class dialogValid(QtWidgets.QDialog):
    def __int__(self):
        super(dialogValid, self).__init__()

    def okBtnClicked(self):
        self.close()

    def setupUI(self):
        loadUi("Views/dialogs/dialogValid.ui", self)
        self.setWindowTitle('Ошибка!')
        # -- Настройка кнопки --
        self.okBtn.clicked.connect(self.okBtnClicked)
        self.move(750, 400)