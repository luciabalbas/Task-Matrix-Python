import unittest
from matrix import randomMatrix
from matrix import printMatrix

class TestMatrixMethods(unittest.TestCase):

    testMatrix = []

    def setUp(self) -> None:
        return super().setUp()
    
    def tearDown(self) -> None:
        self.testMatrix = []
        return super().tearDown()
    
    def test_randomMatrix(self):
        self.testMatrix = randomMatrix(4)
        self.assertEqual(4, len(self.testMatrix))
        self.assertEqual(4, len(self.testMatrix[0]))

    def test_emptyRandomMatrix(self):
        self.assertEqual(0, len(self.testMatrix))

    def test_printInvalidArgument(self):
        self.assertRaises(TypeError, printMatrix, 3)

    def test_randomMatrixNegativeArgument(self):
        self.assertRaises(ValueError, randomMatrix, -3)

    def test_randomMatrixFloatArgument(self):
        self.assertRaises(ValueError, randomMatrix, 3.5)