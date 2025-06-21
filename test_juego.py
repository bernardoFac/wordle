import unittest
from Juego import generar_palabra_secreta, actualizarHistorial
import os

class TestJuegoFunciones(unittest.TestCase):

    def test_generar_palabra_secreta(self):
        ejemplo = ("Milan", "River", "Paris", "Lima", "Roma")
        resultado = generar_palabra_secreta(ejemplo)
        self.assertIn(resultado, [p.lower() for p in ejemplo if len(p) == 5])

    def test_actualizarHistorial_crea_archivo(self):
        test_dni = 99999999
        test_nombre = "Test"
        test_aciertos = 3
        actualizarHistorial(test_dni, test_nombre, test_aciertos)

        ruta_archivo = os.path.join(os.path.dirname(__file__), "historial.csv")
        self.assertTrue(os.path.exists(ruta_archivo))

        with open(ruta_archivo, "r") as f:
            contenido = f.read()
            self.assertIn(str(test_dni), contenido)
            self.assertIn(test_nombre, contenido)

if __name__ == '__main__':
    unittest.main()
