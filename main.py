
from src.ConvertCSVtoJSON import ConverterCSVtoJSON

def main():
    file_csv_path = input("ingrese la ruta del archivo csv: ")
    converter = ConverterCSVtoJSON(file_csv_path)
    converter.converter_file()
if __name__ == "__main__":
    main()
