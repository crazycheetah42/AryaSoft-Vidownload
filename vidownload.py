from PyQt5 import QtCore, QtGui, QtWidgets
from pytube import YouTube
import os
import getpass

class Ui_MainWindow(object):
    def openfilelocation(self):
        username = getpass.getuser()
        os.system(f'explorer "%systemdrive%\\Users\\{username}\\Vidownload"')
    def code(self):
        QtCore.QCoreApplication.processEvents()
        url = self.textEdit.toPlainText()
        video = YouTube(url)
        title = video.title
        self.label_3.setText(f"Downloading {title}...")
        video = video.streams.get_highest_resolution()
        video.download()
        username = getpass.getuser()
        try:
            os.mkdir(f"C:\\Users\\{username}\\Vidownload")
            os.system(f'move *.mp4 "%systemdrive%\\Users\\{username}\\Vidownload"')
        except FileExistsError:
            os.system(f'move *.mp4 "%systemdrive%\\Users\\{username}\\Vidownload"')
        self.label_3.setText(f"Downloaded {title}")
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(849, 455)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 10, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 691, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 160, 821, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 220, 191, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.code)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 300, 691, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QtCore.QRect(100, 280, 681, 51))
        self.label_3.setFont(font) 
        font2 = QtGui.QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(14)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QtCore.QRect(340, 360, 191, 61))
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setAcceptDrops(False)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.clicked.connect(self.openfilelocation)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vidownload"))
        self.label.setText(_translate("MainWindow", "Vidownload"))
        self.label_2.setText(_translate("MainWindow", "Welcome to Vidownload by Aryaman! Enter a YouTube Video URL to download:"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "URL goes here"))
        self.pushButton.setText(_translate("MainWindow", "Download"))
        self.label_3.setText(_translate("MainWindow", "Select Download to begin the download."))
        self.pushButton_2.setText(_translate("MainWindow", "Open File Location"))

import darkdetect
import qdarkstyle
if darkdetect.isDark() == True:
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
if darkdetect.isLight() == True:
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
