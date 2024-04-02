import unittest
from src.ConvertCSVtoJSON import ConverterCSVtoJSON
import json

from src.fileCSV import FileCSV

class TestConverterToJson(unittest.TestCase):
    """Clase de prueba para la clase ConverterCSVtoJSON."""

    def test_converter_correct(self):
        """Prueba que el archivo CSV se convierte correctamente a JSON."""
        c = ConverterCSVtoJSON('C:\\Users\\Usuario\\Desktop\\CSVtoJSONConverter\\src\\files\\file_students.csv')
        c.converter_file()
        expected_result = [
            {"id": "12057", "nombre": "Pepe", "apellido": "Pérez"},
            {"id": "84062", "nombre": "Lulú", "apellido": "López"},
            {"id": "84161", "nombre": "Calvin", "apellido": "Cárdenas"},
            {"id": "17011", "nombre": "Mafalda", "apellido": "Márquez"}
        ]
        with open('C:\\Users\\Usuario\\Desktop\\CSVtoJSONConverter\\src\\files\\file_students.json', 'r', encoding='utf-8') as f:
            actual_result = json.load(f)
        
        self.assertEqual(actual_result, expected_result)

    def test_file_not_found(self):
        converter = FileCSV("xyz")
        resultado = converter.read_file()
        self.assertEqual(resultado, "No se encuentra ese archivo")

if __name__ == '__main__':
    unittest.main()
