from typing import Type, List

from model_elements.camera import Camera
from model_elements.flash import Flash
from model_elements.poligonalModel import PoligonalModel


# т.к. id зарезервированное имя заменил на scene_id
class Scene:
    def __init__(self, scene_id: int, models: List[PoligonalModel], flashes: List[Flash], cameras: List[Camera]):
        self.scene_id = scene_id
        if models is None:
            raise ValueError('Значение не может быть None')
        else:
            self.models = models
        self.flashes = flashes
        if cameras is None:
            raise ValueError('Значение не может быть None')
        else:
            self.cameras = cameras

    def method1(self, type1: Type) -> Type:
        pass

    def method2(self, type1: Type, type2: Type) -> Type:
        pass
