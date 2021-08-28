from typing import Dict, List

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory(object):
    @staticmethod
    def load_data(path: str) -> List[Dict]:
        """Load data from file

        Args:
            path (str): The path to a file (csv, json and xml)

        Returns:
            List[Dict]: The data from file in list format
        """

        if path[-4:] == ".csv":
            loader = CsvImporter()
        elif path[-5:] == ".json":
            loader = JsonImporter()
        elif path[-4:] == ".xml":
            loader = XmlImporter()

        products = loader.import_data(path)

        return products

    @classmethod
    def import_data(
        cls,
        path: str,
        option: str,
    ) -> str:
        """Generate a report from a data file

        Args:
            path (str): The path to a file (csv, json and xml)
            option (str): "simples" or "completo"

        Returns:
            str: The report from data file
        """

        products = cls.load_data(path)

        # generate report
        if option == "simples":
            return SimpleReport.generate(products)
        elif option == "completo":
            return CompleteReport.generate(products)
        else:
            raise ValueError("Opção inválida")
