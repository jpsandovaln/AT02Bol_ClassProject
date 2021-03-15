import os
from PyQt5.QtWidgets import QWidget, QTableWidget, QHeaderView, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton,\
    QLabel, QSpacerItem, QSizePolicy, QFileDialog, QGroupBox, QComboBox, QAbstractItemView, QMainWindow
from PyQt5.QtGui import QPixmap

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
STYLE_PATH = os.path.join(ROOT_DIR, '../styles/basic_style.css')


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(open(STYLE_PATH).read())
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(('Algorithm', 'Word', 'Percentage', 'Second', 'Time', 'image'))
        self.table.setColumnHidden(5, True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.layoutLeftMain = QVBoxLayout()
        self.group_box = QGroupBox()
        self.group_box_img = QGroupBox()

        self.layoutRightMain = QVBoxLayout()
        self.group_boxRightTable = QGroupBox()
        self.showImageButton = QPushButton("Show Image")
        self.showImageButton.clicked.connect(self.__show_image)
        self.group_boxRightTable.setLayout(self.layoutRightMain)
        self.layoutRightMain.addWidget(self.table)
        self.layoutRightMain.addWidget(self.showImageButton)

        self.layoutImg = self.load_members()

        self.group_box_img.setLayout(self.layoutImg)

        self.layoutLeftMain.addWidget(self.group_box)
        self.layoutLeftMain.addWidget(self.group_box_img)

        self.layoutLeft = QVBoxLayout()
        self.group_box.setLayout(self.layoutLeft)

        self.file_path = QLineEdit()
        self.file_path.setReadOnly(True)
        self.browse_button = QPushButton('Browse')
        self.browse_button.clicked.connect(self.__browse_file)

        self.word = QLineEdit()
        self.algorithm = QComboBox()
        self.algorithm.addItem("VGG16")
        self.algorithm.addItem("ResNet50")

        self.percentage = self.load_percentage()

        self.buttonSearch = QPushButton('Search')
        self.vertical_spacer = QSpacerItem(10, 5, QSizePolicy.Expanding)

        self.layoutLeft.setSpacing(5)

        self.layoutLeft.addWidget(QLabel('Video Path:'))
        self.layoutLeft.addWidget(self.file_path)
        self.layoutLeft.addWidget(self.browse_button)
        self.layoutLeft.addWidget(QLabel('Word:'))
        self.layoutLeft.addWidget(self.word)
        self.layoutLeft.addWidget(QLabel('Neural network Model'))
        self.layoutLeft.addWidget(self.algorithm)
        self.layoutLeft.addWidget(QLabel('Percentage'))
        self.layoutLeft.addWidget(self.percentage)
        self.layoutLeft.addWidget(self.buttonSearch)

        self.layoutLeftMain.addSpacerItem(self.vertical_spacer)

        self.layout = QHBoxLayout()
        self.layout.addLayout(self.layoutLeftMain, 25)
        self.layout.addWidget(self.group_boxRightTable, 75)
        self.setLayout(self.layout)

    def load_members(self):
        members = QVBoxLayout()
        members.addWidget(QLabel('Trainer:'))
        members.addWidget(QLabel('\t Jose Paolo Sandoval Noel'))
        members.addWidget(QLabel('Students:'))
        members.addWidget(QLabel('\t Ivan Flores Mendizabal'))
        members.addWidget(QLabel('\t Juan Gutierrez Choque'))
        members.addWidget(QLabel('\t Brian Santivañez Flores'))
        return members

    def load_percentage(self):
        min_percentage = 0
        max_percentage = 100
        percentage = QComboBox()
        while min_percentage <= max_percentage:
            percentage.addItem(str(min_percentage))
            min_percentage += 10
        return percentage

    def __browse_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', 'D:\\', 'Video file (*.mp4)')
        print(file_name[0])
        self.file_path.setText(file_name[0])

    def __show_image(self):
        index = self.table.selectionModel().currentIndex()
        if index.row() == -1:
            return
        image_path = self.table.item(index.row(), 5).text()
        self.selected_image = QLabel()
        self.pixmap = QPixmap(image_path)
        self.selected_image.setPixmap(self.pixmap)
        self.imgWidget = QMainWindow()
        self.imgWidget.setCentralWidget(self.selected_image)
        self.imgWidget.setGeometry(100, 100, 400, 400)
        self.imgWidget.setWindowTitle("ATBootCamp Bolivia 02")
        self.imgWidget.show()

    def get_button_search(self):
        return self.buttonSearch
