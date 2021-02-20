from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("Button a")
        self.button2 = QPushButton("Button b")
        self.__layout = QHBoxLayout()
        self.__layout.addWidget(self.button1, 25)
        self.__layout.addWidget(self.button2, 75)
        self.setLayout(self.__layout)
