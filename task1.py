import sys

class Marker:
    def __init__(self, _color = 'red', _quantity = 100):
        self.color = _color
        self.quantity = _quantity
        
    def printt(self):
        print('\n', self.color, self.quantity)

    def print_by_marker(self, string):
        x = True
        while x == True:
            for i in string:
                if i != ' ':
                    print(i, end = '')
                    self.quantity -= 0.5
                else: print(i, end = '')
                if self.quantity == 0 : x = False; break
            x = False
                
mar1 = Marker()
my_text = 'String, string'
mar1.print_by_marker(my_text)
mar1.printt()
