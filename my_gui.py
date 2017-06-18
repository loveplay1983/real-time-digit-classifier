# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(867, 682)
        MainWindow.setMinimumSize(QtCore.QSize(867, 682))
        MainWindow.setMaximumSize(QtCore.QSize(867, 682))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("vidhya_tutorial_70000_training_images/data/Train/Images/train/1000.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_scribble = QtWidgets.QWidget(self.centralwidget)
        self.widget_scribble.setGeometry(QtCore.QRect(40, 80, 400, 400))
        self.widget_scribble.setObjectName("widget_scribble")
        self.label_names = QtWidgets.QLabel(self.centralwidget)
        self.label_names.setGeometry(QtCore.QRect(210, 20, 521, 31))
        self.label_names.setText("")
        self.label_names.setAlignment(QtCore.Qt.AlignCenter)
        self.label_names.setObjectName("label_names")
        self.textEdit_console = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_console.setGeometry(QtCore.QRect(40, 550, 801, 91))
        self.textEdit_console.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit_console.setStyleSheet("")
        self.textEdit_console.setReadOnly(True)
        self.textEdit_console.setObjectName("textEdit_console")
        self.label_stdh = QtWidgets.QLabel(self.centralwidget)
        self.label_stdh.setGeometry(QtCore.QRect(90, 50, 261, 31))
        self.label_stdh.setAlignment(QtCore.Qt.AlignCenter)
        self.label_stdh.setObjectName("label_stdh")
        self.label_rtdcsudnn = QtWidgets.QLabel(self.centralwidget)
        self.label_rtdcsudnn.setGeometry(QtCore.QRect(70, 0, 671, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_rtdcsudnn.setFont(font)
        self.label_rtdcsudnn.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rtdcsudnn.setObjectName("label_rtdcsudnn")
        self.label_co = QtWidgets.QLabel(self.centralwidget)
        self.label_co.setGeometry(QtCore.QRect(720, 440, 101, 31))
        self.label_co.setAlignment(QtCore.Qt.AlignCenter)
        self.label_co.setObjectName("label_co")
        self.label_classifiedDigit = QtWidgets.QLabel(self.centralwidget)
        self.label_classifiedDigit.setGeometry(QtCore.QRect(720, 350, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(70)
        font.setBold(False)
        font.setWeight(50)
        self.label_classifiedDigit.setFont(font)
        self.label_classifiedDigit.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_classifiedDigit.setText("")
        self.label_classifiedDigit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_classifiedDigit.setObjectName("label_classifiedDigit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 520, 81, 31))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(190, 490, 75, 23))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.label_classifierInputImage = QtWidgets.QLabel(self.centralwidget)
        self.label_classifierInputImage.setGeometry(QtCore.QRect(460, 350, 90, 90))
        self.label_classifierInputImage.setStyleSheet("background-color: rgb(203, 203, 203);")
        self.label_classifierInputImage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_classifierInputImage.setObjectName("label_classifierInputImage")
        self.label_ci = QtWidgets.QLabel(self.centralwidget)
        self.label_ci.setGeometry(QtCore.QRect(580, 450, 111, 31))
        self.label_ci.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ci.setObjectName("label_ci")
        self.label_classifierInputImage_downSampled = QtWidgets.QLabel(self.centralwidget)
        self.label_classifierInputImage_downSampled.setGeometry(QtCore.QRect(590, 350, 90, 90))
        self.label_classifierInputImage_downSampled.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_classifierInputImage_downSampled.setAlignment(QtCore.Qt.AlignCenter)
        self.label_classifierInputImage_downSampled.setObjectName("label_classifierInputImage_downSampled")
        self.label_ci_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_ci_2.setGeometry(QtCore.QRect(460, 450, 101, 31))
        self.label_ci_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ci_2.setObjectName("label_ci_2")
        self.textEdit_classificationHistory = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_classificationHistory.setGeometry(QtCore.QRect(450, 80, 371, 251))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.textEdit_classificationHistory.setFont(font)
        self.textEdit_classificationHistory.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit_classificationHistory.setObjectName("textEdit_classificationHistory")
        self.label_ci_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_ci_3.setGeometry(QtCore.QRect(450, 50, 371, 31))
        self.label_ci_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ci_3.setObjectName("label_ci_3")
        self.checkBox_autoNext = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_autoNext.setGeometry(QtCore.QRect(40, 490, 121, 21))
        self.checkBox_autoNext.setObjectName("checkBox_autoNext")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 867, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MNIST-based real-time classifier | Adnan Niazi"))
        self.label_stdh.setText(_translate("MainWindow", "Scribble the digit here"))
        self.label_rtdcsudnn.setText(_translate("MainWindow", "Real-time Hand-written Digit Classification System Using \n"
"Deep Neural Networks and TensorFlow"))
        self.label_co.setText(_translate("MainWindow", "Classified ouput"))
        self.label_6.setText(_translate("MainWindow", "Output console"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
        self.label_classifierInputImage.setText(_translate("MainWindow", "Image to be \n"
"classifier here"))
        self.label_ci.setText(_translate("MainWindow", "Pre-processed image\n"
"used for classifier input"))
        self.label_classifierInputImage_downSampled.setText(_translate("MainWindow", "Image to be classifier here"))
        self.label_ci_2.setText(_translate("MainWindow", "Image from \n"
"the scribble area"))
        self.label_ci_3.setText(_translate("MainWindow", "Stream of classifier output"))
        self.checkBox_autoNext.setText(_translate("MainWindow", "Auto next"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

