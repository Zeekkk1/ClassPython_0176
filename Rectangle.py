class Rectangle:
    def __init__(self, lebar, tinggi):
        if tinggi == 0 or lebar == 0:
            raise ValueError("tinggi dan lebar tidak bisa 0")
        self.tinggi = tinggi
        self.lebar = lebar
    def circumference(self):
        return 2 * (self.tinggi + self.lebar)
    def area(self):
        return self.tinggi * self.lebar
    def _