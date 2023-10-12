from stuff.some import Angle3D, Point3D


class Camera:
    def __init__(self, location: Point3D, angle: Angle3D):
        self.location = location
        self.angle = angle

    def rotate(self, a: Angle3D):
        pass

    def move(self, p: Point3D):
        pass
