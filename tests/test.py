import unittest
from src.app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        # Crea un cliente de prueba usando la aplicación Flask
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # Envía una solicitud GET a la ruta '/'
        result = self.app.get('/')
        
        # Verifica que la respuesta sea "Hello, World!"
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode(), "Hello, World!")

    # --- NUEVOS TESTS AÑADIDOS PARA LA PRÁCTICA ---

    def test_ruta_no_encontrada(self):
        # Prueba qué pasa si un usuario entra a una URL que no existe
        result = self.app.get('/pagina-falsa-que-no-existe')
        # Debe devolver un error 404 (Not Found)
        self.assertEqual(result.status_code, 404)

    def test_metodo_no_permitido(self):
        # Prueba intentar enviar un formulario (POST) a la página principal
        result = self.app.post('/')
        # Debe devolver un error 405 (Method Not Allowed) porque solo acepta GET
        self.assertEqual(result.status_code, 405)

    def test_tipo_de_contenido(self):
        # Comprueba que el tipo de contenido que devuelve es texto (HTML)
        result = self.app.get('/')
        self.assertIn('text/html', result.content_type)


if __name__ == "__main__":
    unittest.main()
    
    