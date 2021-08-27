from typing import Dict, List
from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path: str) -> List[Dict]:

        if path[-5:] != ".json":
            raise ValueError("Arquivo inválido")

        f = open(path)
        products = json.load(f)
        f.close()

        return products
