from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv


class Inventory:
    @staticmethod
    def read(path):
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

    @staticmethod
    def import_data(path: str, report_type: str):
        products = Inventory.read(path)
        if report_type == "simples":
            simple = SimpleReport.generate(products)
            return simple
        if report_type == "completo":
            complete = CompleteReport.generate(products)
            return complete
        raise ValueError("Type need to be 'simples' or 'completo'")
