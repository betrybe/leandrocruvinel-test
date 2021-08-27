from typing import Dict, List
from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def __init__(self, path: str):
        self.path = path

    def import_data(self) -> List[Dict]:
        if self.path[-4:] != ".csv":
            raise TypeError("Arquivo deve ter formato .csv")

        col_names = []
        products = []

        with open(self.path, newline="") as csvfile:
            rows = csv.reader(csvfile, delimiter=",")
            for i, row in enumerate(rows):

                if i == 0:
                    col_names = row
                else:
                    products.append(dict(zip(col_names, row)))

        return products
