from typing import Dict, List
from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path) -> List[Dict]:
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
