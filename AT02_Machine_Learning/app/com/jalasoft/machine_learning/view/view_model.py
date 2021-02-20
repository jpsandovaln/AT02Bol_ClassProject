from PyQt5.QtWidgets import QMainWindow
from app.com.jalasoft.machine_learning.view.main_widget import MainWidget


class VideoView(QMainWindow):
    def __init__(self):
        super().__init__()
        print('view')
        self.__main_widget = MainWidget()

    def init_ui(self):
        self.setWindowTitle("AT02 Machine Learning")
        self.setGeometry(1000, 1000, 1000, 1000)
        self.setCentralWidget(self.__main_widget)
        self.showMaximized()
        self.show()
