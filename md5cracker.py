# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import os
import sys
import hashlib
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):

    def md5(self):

        self.completed = 0
        while self.completed < 100:
            self.completed += 0.000010
            self.progressBar.setValue(self.completed)

        self.md = "Dont MD5 !"

        if len(str(self.lineEdit.text)) != None:  # Md5 Wordlist içerisinde olmasada aynı Mesaj
            self.textBrowser.setText(self.md)

        for self.esc in self.temiz:

            self.esc = self.esc.strip()
            self.headshot = hashlib.md5(self.esc).hexdigest()


            if self.headshot == self.lineEdit.text():
                self.textBrowser.setText(self.esc)



    def al(self):
        self.lineEdit_2.setText(QtGui.QFileDialog.getOpenFileName())
        self.temiz = open(self.lineEdit_2.text(), 'r').readlines()

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(418, 312)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 270, 92, 26))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 80, 241, 21))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 80, 81, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 120, 101, 26))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 120, 241, 25))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(230, 159, 62, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(140, 180, 231, 20))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(200, 50, 500, 25))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(0, 240, 421, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))


        self.pushButton_2.clicked.connect(self.al)
        self.pushButton.clicked.connect(self.md5)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "MD5 CRACKER", None))
        self.pushButton.setText(_translate("Form", "Crack ME!", None))
        self.label.setText(_translate("Form", "MD5 Hash ?", None))
        self.pushButton_2.setText(_translate("Form", "Open Wordlist", None))
        self.label_2.setText(_translate("Form", "RESULT", None))
        self.label_3.setText(_translate("Form", "MD5 CRACKER\nA.Aziz Altuntaş", None))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = QtGui.QWidget()
    cls = Ui_Form()
    cls.setupUi(form)
    form.show()
    app.exec_()
