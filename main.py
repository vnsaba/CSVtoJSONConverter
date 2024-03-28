
from src.ConvertCSVtoJSON import ConverterCSVtoJSON

def main():
    file_csv_path = input("ingrese la ruta del archivo csv: ")
    converter = ConverterCSVtoJSON()
    converter.converter_file(file_csv_path)
if __name__ == "__main__":
    main()
