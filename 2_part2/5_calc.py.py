# Form implementation generated from reading ui file '.\5_calc.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(605, 465)
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(70, 360, 240, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(320, 360, 220, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.splitter = QtWidgets.QSplitter(parent=Form)
        self.splitter.setGeometry(QtCore.QRect(40, 290, 451, 24))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton = QtWidgets.QPushButton(parent=self.splitter)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.splitter)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.splitter)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.splitter)
        self.pushButton_4.setObjectName("pushButton_4")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(70, 70, 262, 54))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def dodanie(self):
        liczba1 = int(self.lineEdit.text())
        liczba2 = int(self.lineEdit_2.text())
        suma = liczba1 + liczba2
        self.label_3.setText("Dodawanie : {}".format(suma))

    def odejmowanie(self):
        liczba1 = int(self.lineEdit.text())
        liczba2 = int(self.lineEdit_2.text())
        roznica = liczba1 - liczba2
        self.label_3.setText("Odejmowanie : {}".format(roznica))

    def mnozenie(self):
        liczba1 = int(self.lineEdit.text())
        liczba2 = int(self.lineEdit_2.text())
        iloczyn = liczba1 * liczba2
        self.label_3.setText("mnozenie : {}".format(iloczyn))

    def dzielenie(self):
        liczba1 = int(self.lineEdit.text())
        liczba2 = int(self.lineEdit_2.text())
        iloraz = liczba1 / liczba2
        self.label_3.setText("mnozenie : {}".format(iloraz))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "TextLabel"))
        self.label_4.setText(_translate("Form", "TextLabel"))
        self.pushButton.setText(_translate("Form", "+"))
        self.pushButton.clicked.connect(self.dodanie)

        self.pushButton_2.setText(_translate("Form", "-"))
        self.pushButton_2.clicked.connect(self.odejmowanie)

        self.pushButton_3.setText(_translate("Form", "*"))
        self.pushButton_3.clicked.connect(self.mnozenie)

        self.pushButton_4.setText(_translate("Form", "/"))
        self.pushButton_4.clicked.connect(self.dzielenie)
        self.label.setText(_translate("Form", "Pierwsza liczba"))
        self.label_2.setText(_translate("Form", "Druga liczba"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
