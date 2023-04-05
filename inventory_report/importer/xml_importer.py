from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        tree = ET.parse(path)
        root = tree.getroot()

        product_list = []
        for child in root:
            product = {}
            for sub_elem in child:
                product[sub_elem.tag] = sub_elem.text
            product_list.append(product)
        return product_list
