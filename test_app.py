import unittest
from app import app

class CalculatorTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_suma(self):
        response = self.app.post('/suma', json={'num1': 5, 'num2': 3})
        data = response.get_json()
        self.assertEqual(data['result'], 8)

    def test_resta(self):
        response = self.app.post('/resta', json={'num1': 10, 'num2': 4})
        data = response.get_json()
        self.assertEqual(data['result'], 6)

    def test_multiplicacion(self):
        response = self.app.post('/multiplicacion', json={'num1': 7, 'num2': 6})
        data = response.get_json()
        self.assertEqual(data['result'], 42)

    def test_division(self):
        response = self.app.post('/division', json={'num1': 8, 'num2': 2})
        data = response.get_json()
        self.assertEqual(data['result'], 4)

    def test_division_by_zero(self):
        response = self.app.post('/division', json={'num1': 8, 'num2': 0})
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['result'], 'Error: División por cero')

    def test_invalid_input(self):
        response = self.app.post('/suma', json={'num1': 'a', 'num2': 3})
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['result'], 'Error: Entrada no válida')

if __name__ == '__main__':
    unittest.main()
