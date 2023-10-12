from abc import abstractmethod

from stuff.some import Angle3D, Point3D, Color


class Flash:
    def __init__(self, location: Point3D, angle: Angle3D, color: Color, power: float):
        self.location = location
        self.angle = angle
        self.color = color
        self.power = power

    def rotate(self, r: Angle3D):
        pass

    def move(self, p: Point3D):
        pass
