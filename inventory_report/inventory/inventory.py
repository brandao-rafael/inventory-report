from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import json
import csv
import xml.etree.ElementTree as ET


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
        return data

    @staticmethod
    def read_xml(path):
        tree = ET.parse(path)
        root = tree.getroot()

        product_list = []
        for child in root:
            product = {}
            for sub_elem in child:
                product[sub_elem.tag] = sub_elem.text
            product_list.append(product)
        return product_list

    @staticmethod
    def import_data(path: str, report_type: str):
        products = []
        if path.endswith(".json"):
            products = Inventory.read_json(path)
        elif path.endswith(".xml"):
            products = Inventory.read_xml(path)
        else:
            products = Inventory.read_csv(path)

        if report_type == "simples":
            simple = SimpleReport.generate(products)
            return simple
        if report_type == "completo":
            complete = CompleteReport.generate(products)
            return complete
        raise ValueError("Type need to be 'simples' or 'completo'")
