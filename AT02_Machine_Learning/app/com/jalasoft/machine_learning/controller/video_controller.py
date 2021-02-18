from app.com.jalasoft.machine_learning.model.video_model import VideoModel


class VideoController:
    def __init__(self, view):
        print('controller')
        model = VideoModel()
        model.get_value()
