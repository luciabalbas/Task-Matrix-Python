import unittest
from sums import addsColumns
from sums import addsRows

class TestSumsMethods(unittest.TestCase):
    testMatrix = []

    def setUp(self) -> None:
        self.testMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        return super().setUp()
    
    def tearDown(self) -> None:
        self.testMatrix = []
        return super().tearDown()
    
    def test_correctSumRows(self):
        testSum = addsRows(self.testMatrix)
        self.assertEqual(6, testSum[0])
        self.assertEqual(15, testSum[1])
        self.assertEqual(24, testSum[2])

    def test_correctSumColumns(self):
        testSums = addsColumns(self.testMatrix)
        self.assertEqual(12, testSums[0])
        self.assertEqual(15, testSums[1])
        self.assertEqual(18, testSums[2])

    def test_InvalidArgument(self):
        matrixError = [[1, 2, 'k'], [4, 5, 6], [7, 8, 9]]
        self.assertRaises(TypeError, addsColumns, matrixError)
        self.assertRaises(TypeError, addsRows, matrixError)