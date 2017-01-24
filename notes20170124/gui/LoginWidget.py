# coding: utf-8

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal

from .ui.Ui_LoginWidget import Ui_LoginForm
from .NotesWidget import NotesWidget
from core.NoteModel import NoteModel

LOGIN = 'karina'
PASSWORD = '123'
class LoginWidget(QWidget, Ui_LoginForm):
    login_password_right = pyqtSignal(name='loginPasswordRight')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()
        self.init_signals()


    def init_ui(self):
        # loadUi('gui/ui/notes_widget.ui', self)
        self.setupUi(self)

    def init_signals(self):
        self.okBtn.clicked.connect(self.onClickOk)
        self.cancelBtn.clicked.connect(self.onClickCancel)

    def onClickOk(self):
        valueLogin = self.loginEdit.text()
        valuePassword = self.passwordEdit.text()
        if str(valueLogin) == LOGIN and str(valuePassword) == PASSWORD:
            #signal
            self.login_password_right.emit()
        else:
            self.loginEdit.setText('Что-то пошло не так...')
            self.passwordEdit.setText('Проверьте правильность логина и пароля')

    def onClickCancel(self):
        self.loginEdit.setText(None)
        self.passwordEdit.setText(None)

