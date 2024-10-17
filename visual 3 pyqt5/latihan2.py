import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Create line edits
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(260, 80, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 120, 191, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 160, 211, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(260, 190, 113, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        
        # Create labels
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 80, 55, 16))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 120, 55, 16))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 160, 55, 16))
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(84, 190, 121, 20))
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 220, 55, 16))
        self.label_5.setObjectName("label_5")
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(140, 250, 55, 16))
        self.label_6.setObjectName("label_6")
        
        # Additional line edits for TELEPON and ALAMAT
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(260, 220, 113, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(260, 250, 113, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        
        # Create buttons
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 320, 93, 28))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 320, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 320, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 320, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setText(_translate("MainWindow", "2210010495"))
        self.lineEdit_2.setText(_translate("MainWindow", "Wiza Pramana Putra"))
        self.lineEdit_3.setText(_translate("MainWindow", "5E Reg Pagi Banjarmasin"))
        self.lineEdit_4.setText(_translate("MainWindow", "23/12/2003"))
        self.label.setText(_translate("MainWindow", "NIM"))
        self.label_2.setText(_translate("MainWindow", "NAMA"))
        self.label_3.setText(_translate("MainWindow", "KELAS"))
        self.label_4.setText(_translate("MainWindow", "TANGGAL LAHIR"))
        self.label_5.setText(_translate("MainWindow", "TELEPON"))
        self.label_6.setText(_translate("MainWindow", "ALAMAT"))
        self.lineEdit_5.setText(_translate("MainWindow", "0878-7435-7460"))
        self.lineEdit_6.setText(_translate("MainWindow", "jalan HKSN"))
        self.pushButton.setText(_translate("MainWindow", "SIMPAN"))
        self.pushButton_2.setText(_translate("MainWindow", "EDIT "))
        self.pushButton_3.setText(_translate("MainWindow", "HAPUS"))
        self.pushButton_4.setText(_translate("MainWindow", "BATAL"))

class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
