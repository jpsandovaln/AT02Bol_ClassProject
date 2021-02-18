from PyQt5.QtWidgets import QApplication
from app.com.jalasoft.machine_learning.view.view_model import VideoView
from app.com.jalasoft.machine_learning.controller.video_controller import VideoController


if __name__ == '__main__':
    print('main')
    view = VideoView()
    controller = VideoController(view)
