from typing import List

from .poligon import Poligon
from .texture import Texture
from stuff.some import Point3D


class PoligonalModel:
    def __init__(self, textures: List[Texture] | None):
        self.textures = textures
        self.poligons: List[Poligon] = [Poligon([Point3D()])]

