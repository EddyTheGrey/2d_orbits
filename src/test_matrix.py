import unittest
import matrix

class TestSplitter(unittest.TestCase):
    def test_create_matrix(self):
        mat = matrix.create_matrix(3, 4)
        self.assertEqual(mat.shape, (3, 4))

if __name__ == "__main__":
    unittest.main()        