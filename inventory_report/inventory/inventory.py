from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory(object):
    def __init__(self, path: str, option: str):
        """Initializate object

        Args:
            path (str): path of file
            option (str): "simples" or "completo"
        """
        self.path = path
        self.option = option

    def import_data(self) -> str:

        # !TODO
        # recuperar os dados do arquivo
        if self.path[-4:] == ".csv":
            loader = CsvImporter(self.path)
            products = loader.import_data()

        elif self.path[-5:] == ".json":
            loader = JsonImporter(self.path)
            products = loader.import_data()

        # chamar o método de generate correspondente à entrada passada
        if self.option == "simples":
            return SimpleReport.generate(products)

        if self.option == "completo":
            return CompleteReport.generate(products)
