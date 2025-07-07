import unittest
from Juego import generar_palabra_secreta, actualizarHistorial, filtrar_palabras_por_dificultad, mostrar_estado_letras
import os

class TestJuegoFunciones(unittest.TestCase):

    def test_generar_palabra_secreta(self):
        """Verifica que la palabra generada esté dentro de la lista original."""
        ejemplo = ("Milan", "River", "Paris", "Lima", "Roma")
        resultado = generar_palabra_secreta(ejemplo)
        self.assertIn(resultado, [p.lower() for p in ejemplo if len(p) == 5])

    def test_actualizarHistorial_crea_archivo(self):
        """
        Verifica que al usar actualizarHistorial:
        - Se cree el archivo historial.csv si no existe.
        - Se agregue correctamente la información del jugador.
        """
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
    
    def test_filtrar_palabras_por_dificultad_facil(self):
        """
        Verifica que la función filtre solo palabras de 4 letras 
        cuando la dificultad seleccionada es '1' (fácil).
        """
        categorias = {
            "animales": ("gato", "mono", "lobo", "oso"),
            "paises": ("Peru", "Chile", "India"),
            }
        resultado = filtrar_palabras_por_dificultad(categorias, "1")
        self.assertTrue(all(len(p) == 4 for p in resultado))


    def test_mostrar_estado_letras_no_falla(self):
        """
        Verifica que la función mostrar_estado_letras se ejecute sin errores 
        al comparar dos listas de letras distintas.
        """
        intento = list("roma")
        palabra = list("amor")
        mostrar_estado_letras(intento, palabra)  


if __name__ == '__main__':
    unittest.main()
