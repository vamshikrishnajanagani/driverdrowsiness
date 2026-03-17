
from PyQt5 import QtCore, QtGui, QtWidgets
from detect_drowsiness import VisualBehaviour
from Classification import classfy
class Ui_Home(object):

    def visual(self):
        d = VisualBehaviour()
        d.start()

    def barchart(self):
        classfy()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(742, 432)
        Dialog.setStyleSheet("background-image: url(../Drowsy/images/d2.jpg);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 170, 201, 41))
        self.pushButton.setStyleSheet("color: rgb(85, 0, 0);\n"
"font: 16pt \"Franklin Gothic Heavy\";\n"
"color: rgb(170, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.visual)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 280, 201, 41))
        self.pushButton_2.setStyleSheet("color: rgb(85, 0, 0);\n"
"font: 16pt \"Franklin Gothic Heavy\";\n"
"color: rgb(170, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.barchart)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Drowsiness Monitoring System"))
        self.pushButton.setText(_translate("Dialog", "Visual  Behaviour"))
        self.pushButton_2.setText(_translate("Dialog", "Machine Learning"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Home()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

