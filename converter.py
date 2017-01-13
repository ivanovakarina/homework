import sys

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QPushButton, QDoubleSpinBox,
    QVBoxLayout
)

class Course(QObject):
    def get(self):
        return 30.0

class CurrencyConverter(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initUi()
        self.initSignals()
        self.initLayouts()


    def initUi(self):
        self.setWindowTitle('Конвертер валют')

        self.srcLabel = QLabel(' Сумма в рублях', self)
        self.resultLabel = QLabel('Сумма в долларах', self)

        self.srcAmmount = QDoubleSpinBox(self)
        self.srcAmmount.setMaximum(999999999)
        self.resultAmount = QDoubleSpinBox(self)
        self.resultAmount.setMaximum(999999999)
        #self.resultAmount.setReadOnly(True)
        #self.resultAmount.setDisabled(True)

        self.convertBtn = QPushButton('Перевести', self)

        self.resetBtn = QPushButton('Очистить', self)


    def initSignals(self):
        self.convertBtn.clicked.connect(self.onClick)
        self.convertBtn.setDisabled(False)
        self.resetBtn.clicked.connect(self.onClickReset)

    def initLayouts(self):
        self.w = QWidget()

        self.mainLayout = QVBoxLayout(self.w)
        self.mainLayout.addWidget(self.srcLabel)
        self.mainLayout.addWidget(self.srcAmmount)
        self.mainLayout.addWidget(self.resultLabel)
        self.mainLayout.addWidget(self.resultAmount)
        self.mainLayout.addWidget(self.convertBtn)
        self.mainLayout.addWidget(self.resetBtn)

        self.setCentralWidget(self.w)

    def onClick(self):
        valueRub = self.srcAmmount.value()
        valueUSD = self.resultAmount.value()
        self.convertBtn.setDisabled(False)
        if valueRub and valueUSD == 0:
            self.resultAmount.setValue(valueRub / Course().get())
        elif valueUSD and valueRub == 0:
            self.srcAmmount.setValue(valueUSD * Course().get())
        else:
            self.convertBtn.setDisabled(True)

    def onClickReset(self):
        self.resultAmount.setValue(0)
        self.srcAmmount.setValue(0)
        self.convertBtn.setDisabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    converter = CurrencyConverter()
    converter.show()

    sys.exit(app.exec_())
