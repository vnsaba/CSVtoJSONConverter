
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
        print(student_list)

        if student_list != "No se encuentra ese archivo":
            json_handler = FileJSON(self.file_path_csv)
            json_handler.write_file(student_list)