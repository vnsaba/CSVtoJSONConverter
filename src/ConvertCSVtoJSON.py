
from .fileCSV import FileCSV
from .fileJSON import FileJSON

class ConverterCSVtoJSON():
    """
    Clase para convertir un archivo csv a json
    """
    def __init__(self, file_path_csv):
        self.file_path_csv = file_path_csv

    def converter_file (self):
        """
        Convierte un archivo CSV en un archivo JSON.

        Lee el archivo CSV especificado, crea una lista de objetos Student
        a partir de los datos leídos y luego escribe esta lista en un archivo JSON.

        Parameters:
        - file_csv (str): Ruta del archivo CSV que se convertirá a JSON.
        """

        csv_handler = FileCSV(self.file_path_csv)
        student_list = csv_handler.read_file()

        if student_list is not None:
            json_handler = FileJSON()
            json_handler.write_file(student_list, self.file_path_csv)