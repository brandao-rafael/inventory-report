from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import json
import csv


class Inventory:
    @staticmethod
    def read_csv(path):
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
    def read_json(path):
        with open(path, mode="r", encoding="utf8") as file:
            contents = file.read()
            data = json.loads(contents)
            header = data[0].keys()
        product_list = []

        for row in data:
            product = {}
            for column in header:
                product[column] = row.get(column)
            product_list.append(product)
        return product_list

    @staticmethod
    def import_data(path: str, report_type: str):
        products = []
        if path.endswith(".json"):
            products = Inventory.read_json(path)
        else:
            products = Inventory.read_csv(path)

        if report_type == "simples":
            simple = SimpleReport.generate(products)
            return simple
        if report_type == "completo":
            complete = CompleteReport.generate(products)
            return complete
        raise ValueError("Type need to be 'simples' or 'completo'")
