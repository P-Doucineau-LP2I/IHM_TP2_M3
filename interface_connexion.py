# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_connexion.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 175)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_identifiant = QtWidgets.QLineEdit(Form)
        self.lineEdit_identifiant.setGeometry(QtCore.QRect(120, 10, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_identifiant.setFont(font)
        self.lineEdit_identifiant.setObjectName("lineEdit_identifiant")
        self.lineEdit_motDePasse = QtWidgets.QLineEdit(Form)
        self.lineEdit_motDePasse.setGeometry(QtCore.QRect(120, 40, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_motDePasse.setFont(font)
        self.lineEdit_motDePasse.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_motDePasse.setObjectName("lineEdit_motDePasse")
        self.lineEdit_email = QtWidgets.QLineEdit(Form)
        self.lineEdit_email.setGeometry(QtCore.QRect(120, 70, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.bouton_valider = QtWidgets.QPushButton(Form)
        self.bouton_valider.setGeometry(QtCore.QRect(150, 110, 75, 23))
        self.bouton_valider.setObjectName("bouton_valider")
        self.label_message = QtWidgets.QLabel(Form)
        self.label_message.setGeometry(QtCore.QRect(16, 150, 371, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_message.setFont(font)
        self.label_message.setText("")
        self.label_message.setAlignment(QtCore.Qt.AlignCenter)
        self.label_message.setWordWrap(True)
        self.label_message.setObjectName("label_message")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Identifiant :"))
        self.label_2.setText(_translate("Form", "Mot de passe :"))
        self.label_3.setText(_translate("Form", "Adresse mail :"))
        self.bouton_valider.setText(_translate("Form", "Valider"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())