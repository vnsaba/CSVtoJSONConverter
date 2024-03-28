
from .fileCSV import FileCSV
from .fileJSON import FileJSON

class ConverterCSVtoJSON():
    """
    Clase para convertir un archivo csv a json
    """
    def converter_file (self, file_csv):
        """
        Convierte un archivo CSV en un archivo JSON.

        Lee el archivo CSV especificado, crea una lista de objetos Student
        a partir de los datos leídos y luego escribe esta lista en un archivo JSON.

        Parameters:
        - file_csv (str): Ruta del archivo CSV que se convertirá a JSON.
        """

        csv_handler = FileCSV(file_csv)
        student_list = csv_handler.read_file()

        if student_list is not None:
            json_handler = FileJSON()
            json_handler.write_file(student_list, file_csv)