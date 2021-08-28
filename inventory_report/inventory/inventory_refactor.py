from typing import Optional, Union

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor:
    def __init__(
        self,
        importer: Optional[Union[CsvImporter, JsonImporter, XmlImporter]],
        data=[],
    ):
        self.importer = importer
        self.data = data

    def import_data(
        self,
        path: str,
        option: str,
    ) -> str:
        """Import data and generate report

        Args:
            path (str): Path of file (csv, json or xml)
            option (str): "simples" or "completo"

        Raises:
            ValueError: If an invalid file, raise value error

        Returns:
            str: The formatted report
        """

        loader = self.importer()

        # clear data if another instance
        if self.data:
            self.data += loader.import_data(path)
        else:
            self.data = loader.import_data(path)

        # generate report
        if option == "simples":
            return SimpleReport.generate(self.data)

        elif option == "completo":
            return CompleteReport.generate(self.data)
        else:
            raise ValueError("Opção inválida")

    def __iter__(self):
        return InventoryIterator(self)
