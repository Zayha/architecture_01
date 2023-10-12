from abc import ABC

from in_memory_model.i_model_changed_observer import IModelChangedObserver
from in_memory_model.i_model_changer import IModelChanger
from model_elements.camera import Camera
from model_elements.flash import Flash
from model_elements.poligonalModel import PoligonalModel
from typing import List

from model_elements.scene import Scene
from stuff.some import Point3D, Angle3D, Color


class ModelStore(IModelChanger, ABC):
    def __init__(self, change_observers: List[IModelChangedObserver]):
        self.models: List[PoligonalModel] = [PoligonalModel(None)]
        self.scenes: List[Scene] = []
        self.flashes: List[Flash] = [Flash(Point3D(), Angle3D(), Color(), 0.0)]
        self.cameras: List[Camera] = [Camera(Point3D(), Angle3D())]
        self.__change_observers = change_observers
        self.scenes.append(Scene(0, self.models, self.flashes, self.cameras))

    def get_scene(self, scene_id: int) -> Scene:
        pass

    def notify_change(self, sender: IModelChanger) -> IModelChanger:
        pass
