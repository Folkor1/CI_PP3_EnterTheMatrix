import unittest
import matrix

class TestMatrix(unittest.TestCase):

    def test_matrix_2x2_input(self):
        numbers = matrix.Matrix_2x2(1,2,3,4)
        calculation = numbers.determinant_2x2()
        determ_2x2 = '-2'
        msg_2x2 = "Matrix 2x2 determinant caclulation is not correct!"
        self.assertEqual(calculation, determ_2x2, msg_2x2)

    def test_matrix_3x3_input(self):
        numbers = matrix.Matrix_3x3(2,6,7,2,0,8,1,2,5)
        calculation = numbers.determinant_3x3()
        determ_3x3 = -16
        msg_3x3 = "Matrix 3x3 determinant caclulation is not correct!"
        self.assertEqual(calculation, determ_3x3, msg_3x3)

if __name__ == '__main__':
    unittest.main()