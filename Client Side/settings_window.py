from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi

class SettingsWindow(QMainWindow):
    def __init__(self):
        super(SettingsWindow,self).__init__()
        loadUi("UI/settings_window.ui", self)

        self.pushButton.clicked.connect(self.go_to_detection_window)


    def displayInfo(self):
        self.show()
    def go_to_detection_window(self):
        print("go to detection window")