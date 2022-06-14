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

class Matrix_2x2(Matrix):
    """
    2x2 matrix class,
    returns 2x2 matrix determinant.
    """
    def __init__(self, num1, num2, num3, num4):
        super().__init__(num1, num2, num3, num4)
    
    def determinant_2x2(self):
        return f'{super().calc_2x2()}'

class Matrix_3x3(Matrix):
    """
    3x3 matrix class,
    calculates 3x3 matrix determinant.
    """
    def __init__(self, num1, num2, num3, num4, num5, num6, num7, 
    num8, num9):
        Matrix.__init__(self, num1, num2, num3, num4)
        self.num5 = num5
        self.num6 = num6
        self.num7 = num7
        self.num8 = num8
        self.num9 = num9
    
    def determinant_3x3(self):
        a = self.num1 * self.num5 * self.num9
        b = self.num2 * self.num6 * self.num7
        c = self.num3 * self.num4 * self.num8
        d = self.num3 * self.num5 * self.num7
        e = self.num2 * self.num4 * self.num9
        f = self.num1 * self.num6 * self.num8
        
        return a + b + c - d - e - f