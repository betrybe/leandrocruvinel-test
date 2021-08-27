from typing import Dict, List
from inventory_report.importer.importer import Importer
from xml.etree import ElementTree


class XmlImporter(Importer):
    @staticmethod
    def import_data(path: str) -> List[Dict]:

        if path[-4:] != ".xml":
            raise ValueError("Arquivo inválido")

        root = ElementTree.parse(path).getroot()
        products = []
        for row in list(root):
            product = dict()
            for item in list(row):
                product[item.tag] = item.text
            products.append(product)

        return products
