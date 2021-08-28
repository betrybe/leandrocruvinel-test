from typing import Dict, List
from xml.etree import ElementTree

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path: str) -> List[Dict]:
        """Import and handle xml file

        Args:
            path (str): A xml file path

        Raises:
            ValueError: If file is not xml it raises a value error

        Returns:
            List[Dict]: The file in list format
        """

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
