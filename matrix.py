class Matrix:
    """
    Matrix superclass.
    """
    def __init__(self, num1, num2, num3, num4):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
    
    def calc_2x2(self):
        return self.num1 * self.num4 - self.num2 * self.num3