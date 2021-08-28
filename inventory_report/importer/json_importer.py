import json
from typing import Dict, List

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path: str) -> List[Dict]:
        """Import and handle json file

        Args:
            path (str): A json file path

        Raises:
            ValueError: If file is not json it raises a value error

        Returns:
            List[Dict]: The file in list format
        """

        if path[-5:] != ".json":
            raise ValueError("Arquivo inválido")

        f = open(path)
        products = json.load(f)
        f.close()

        return products
