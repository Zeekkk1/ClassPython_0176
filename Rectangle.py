class Rectangle:
    def __init__(self, lebar, tinggi):
        if tinggi == 0 or lebar == 0:
            raise ValueError("tinggi dan lebar tidak bisa 0")
        self.tinggi