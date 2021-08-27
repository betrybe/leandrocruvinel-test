from typing import Dict, List
from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def __init__(self, path: str):
        self.path = path

    def import_data(self) -> List[Dict]:

        if self.path[-5:] != ".json":
            raise TypeError("Arquivo deve ter formato .json")

        f = open(self.path)
        products = json.load(f)
        f.close()

        return products
