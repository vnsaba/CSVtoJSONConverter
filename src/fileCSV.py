import csv
import os
from .model.student import Student

class FileCSV:
    """
    Clase para manejar archivos csv
    """
    def __init__(self, file:str):
        self.file = file

    def validate_file_csv (self) -> bool:
        """
        Valida si el archivo tiene la extensión .csv

        Returns:
        - bool: True si el archivo es un archivo CSV válido, False en caso contrario.
        """
        extension = '.csv'
        _, file_extension = os.path.splitext(self.file)
        return file_extension in extension
        
    def validate_is_file(self) -> bool:
        """
        Valida si es un archivo.

        Returns:
        - bool: True si es un archivo, False en caso contrario.
        """
        return os.path.isfile(self.file)
    
    def validate_exist_file (self) -> bool:
        """
        Valida si existe el archivo.

        Returns:
        - bool: True si exsite el archivo, False en caso contrario.
        """
        exist = os.path.exists(self.file) 
        if exist:
            return True
        print("No se encuentra ese archivo")   
        return False  
    def read_file (self) :
        """
        Lee el archivo CSV y devuelve una lista de objetos Student.

        Returns:
        - list: Lista de objetos Student leídos del archivo CSV.
        """
        students = []
        if self.validate_exist_file() and self.validate_file_csv() and self.validate_is_file():         
            with open(self.file,  encoding='utf-8') as file:
                csv_reader = csv.reader(file,  delimiter=',')
                for row in csv_reader:
                    student_id, nombre, apellido = row
                    students.append({'id': student_id.strip(), 'nombre': nombre.strip(), 'apellido': apellido.strip()})
            return students
        