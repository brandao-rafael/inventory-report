from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(path, mode="r", encoding="utf8") as file:
            file_reader = csv.reader(file)
            header, *data = file_reader
        product_list = []

        for row in data:
            product = {}
            for index, column in enumerate(header):
                product[column] = row[index]
            product_list.append(product)
        return product_list
