import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import unittest
from utils import genurlsede


class TestGenUrlSede(unittest.TestCase):

    def test_Prueba(self):
        self.assertEqual(genurlsede.transformarnombremunicipio("Prueba"), 'Prueba')

if __name__ == '__main__':
    unittest.main()