import os
from core.convert.video_manager import VideoManger
from core.deep_network.algorithm_factory import AlgorithmFactory
from core.convert.video_parameter import VideoParameter
from PyQt5.QtWidgets import QTableWidgetItem
import datetime

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FFMPEG_PATH = os.path.join(ROOT_DIR, '..\\thirdparty\\ffmpeg\\ffmpeg.exe')
OUTPUTH_PATH = os.path.join(ROOT_DIR, '..\\output_image\\')
if not os.path.isdir(OUTPUTH_PATH):
    os.mkdir(OUTPUTH_PATH)


class Controller:
    def __init__(self, view):
        self.__view = view
        self.__view.init_ui()
        self.__view.get_main_widget().get_button_search().clicked.connect(self.process)
        self.table_result = self.__view.get_main_widget().table

    def process(self):
        word = self.__view.get_main_widget().word.text()
        min_accepted_percentage = self.__view.get_main_widget().percentage.currentText()
        algorithm_param = self.__view.get_main_widget().algorithm.currentText()
        video_path = self.__view.get_main_widget().file_path.text()

        video_param = VideoParameter()
        video_param.set_ffmpeg_path(FFMPEG_PATH)
        video_param.set_video_path(video_path)
        video_param.set_output_folder(OUTPUTH_PATH)

        video = VideoManger()
        video.convert(video_param)

        algorithm = AlgorithmFactory.instance(algorithm_param)
        result = algorithm.run(OUTPUTH_PATH, word, min_accepted_percentage)
        print(result)

        self.table_result.setRowCount(0)
        count = 0
        for res in result:
            self.table_result.insertRow(count)
            self.table_result.setItem(count, 0, QTableWidgetItem(algorithm_param))
            self.table_result.setItem(count, 1, QTableWidgetItem(res.get('word')))
            self.table_result.setItem(count, 2, QTableWidgetItem(res.get('percentage')))
            self.table_result.setItem(count, 3, QTableWidgetItem(res.get('second')))
            self.table_result.setItem(count, 4, QTableWidgetItem(self.sec_to_time(res.get('second'))))
            self.table_result.setItem(count, 5, QTableWidgetItem(res.get('image')))
            count += 1

    def sec_to_time(self, second):
        return str(datetime.timedelta(seconds=int(second)))
