import unittest
from src.app import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode(), "Hello, World!")

    def test_ruta_no_encontrada(self):
        result = self.app.get('/pagina-falsa')
        self.assertEqual(result.status_code, 404)

    def test_metodo_no_permitido(self):
        result = self.app.post('/')
        self.assertEqual(result.status_code, 405)

    def test_tipo_de_contenido(self):
        result = self.app.get('/')
        self.assertIn('text/html', result.content_type)

if __name__ == "__main__":
    unittest.main()