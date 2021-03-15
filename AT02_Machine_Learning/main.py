import sys
from PyQt5.QtWidgets import QApplication
from view.view import View
from controller.controller import Controller


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View()
    controller = Controller(view)
    sys.exit(app.exec())
