import json
import os 

class FileJSON:
    """
    Clase para manejar archivos JSON
    """
    def __init__(self, name_file) -> None:
        self.file_name = name_file

    def get_json_file_path(self):
        """
        Obtiene la ruta del archivo JSON asociado al archivo actual.

        Returns:
        str: La ruta completa del archivo JSON correspondiente al archivo actual.
        """
        file_name_without_extension = os.path.splitext(os.path.basename(self.file_name))[0]
        folder_name = os.path.dirname(self.file_name)
        return os.path.join(folder_name, file_name_without_extension + '.json')

    def write_file(self, student_list):
        """
        Escribe un archivo JSON a partir de una lista de objetos de estudiante.

        Parameters:
            student_list (list): Una lista de objetos de estudiante.

        Raises:
            FileNotFoundError: Si no se puede encontrar la ruta del archivo JSON.
            PermissionError: Si no se tienen permisos para escribir en el archivo JSON.
        """
        file_json = self.get_json_file_path()

        try:
            with open(file_json, 'w', encoding='utf-8') as file:
                json.dump(student_list, file, indent=4, ensure_ascii=False)
        except FileNotFoundError as exc:
            raise FileNotFoundError("JSON file path not found.") from exc
        except PermissionError as exc:
            raise PermissionError("You do not have permissions to write to the JSON file.") from exc