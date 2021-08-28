import csv
from typing import Dict, List

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path) -> List[Dict]:
        """Import and handle csv file

        Args:
            path (str): A csv file path

        Raises:
            ValueError: If file is not csv it raises a value error

        Returns:
            List[Dict]: The file in list format
        """
        if path[-4:] != ".csv":
            raise ValueError("Arquivo inválido")

        col_names = []
        products = []

        with open(path, newline="") as csvfile:
            rows = csv.reader(csvfile, delimiter=",")
            for i, row in enumerate(rows):

                if i == 0:
                    col_names = row
                else:
                    products.append(dict(zip(col_names, row)))

        return products
