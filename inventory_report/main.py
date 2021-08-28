from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor
import sys


def main():

    if len(sys.argv) < 3:
        sys.stderr.write("Verifique os argumentos\n")
    else:
        _, path, option = sys.argv

        if path[-4:] == ".csv":
            loader = CsvImporter
        elif path[-5:] == ".json":
            loader = JsonImporter
        elif path[-4:] == ".xml":
            loader = XmlImporter

        inventory = InventoryRefactor(loader)
        print(inventory.import_data(path, option), end="")


if __name__ == "__main__":
    main()
