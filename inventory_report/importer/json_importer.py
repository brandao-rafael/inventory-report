from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")
        with open(path, mode="r", encoding="utf8") as file:
            contents = file.read()
            data = json.loads(contents)
        return data
