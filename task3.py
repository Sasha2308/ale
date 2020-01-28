class Circle:    
    def __init__(self, radius = 0):
        self._radius = radius

    def square(self):
        square = 3.14 * self._radius**2
        print('Окружность: ', square)

    def length(self):
        length = 2 * 3.14 * self._radius
        print('Длина окружности: ', length)
        
    def set_radius(self, radius):
        self._radius = radius
    
    def get_radius(self):
        return self._radius

    def get_diam(self):
        d = self._radius * 2
        print('Диаметр: ', d)    

c = Circle(int(input('Input your radius: ')))
c.get_diam()
c.square()
c.length()
