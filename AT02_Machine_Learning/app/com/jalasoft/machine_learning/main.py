import sys
from PyQt5.QtWidgets import QApplication
from app.com.jalasoft.machine_learning.view.view_model import VideoView
from app.com.jalasoft.machine_learning.controller.video_controller import VideoController


if __name__ == '__main__':
    print('main')
    app = QApplication(sys.argv)
    view = VideoView()
    controller = VideoController(view)
    sys.exit(app.exec())
