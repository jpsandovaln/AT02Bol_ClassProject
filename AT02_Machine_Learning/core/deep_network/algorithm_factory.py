from core.deep_network.vgg16_model import VGG16Model
from core.deep_network.resnet50_model import ResNet50Model


class AlgorithmFactory:
    @staticmethod
    def instance(algorithm_param):
        if algorithm_param == 'VGG16':
            return VGG16Model()
        else:
            return ResNet50Model()
