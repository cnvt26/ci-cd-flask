import unittest
from src.app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        # Configura el cliente de pruebas
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # Test 1: Comprobar página principal
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode(), "Hello, World!")

    def test_ruta_no_encontrada(self):
        # Test 2: Comprobar error 404
        result = self.app.get('/esta-ruta-no-existe')
        self.assertEqual(result.status_code, 404)

    def test_metodo_no_permitido(self):
        # Test 3: Comprobar que no acepta POST en la home
        result = self.app.post('/')
        self.assertEqual(result.status_code, 405)

    def test_content_type(self):
        # Test 4: Comprobar que devuelve texto/html
        result = self.app.get('/')
        self.assertIn('text/html', result.content_type)

if __name__ == "__main__":
    unittest.main()