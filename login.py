
# https://stackoverflow.com/questions/49909633/pyqt5-custom-dialog-input-popup-within-main-window?rq=1

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QDialog


form_class = uic.loadUiType("./ui/login.ui")[0]

class CustomDialog(QDialog, form_class):
    def __init__(self):
        super(CustomDialog, self).__init__()
        self.setupUi(self)


        # set initials values to widgets
        self.inputPw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputCert.setEchoMode(QtWidgets.QLineEdit.Password)

    def getResults(self):
        if self.exec_() == QDialog.Accepted:
            # get all values
            val1 = self.inputId.text()
            val2 = self.inputPw.text()
            val3 =self.inputCert.text()
            return val1, val2,val3
        else:
            return None