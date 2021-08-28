from collections import Counter
from typing import Dict, List

from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products: List[Dict]) -> str:
        """Gera um relatório completo

        Args:
            dados (List[Dict]): uma lista contendo estruturas do tipo dict

        Returns:
            str: relatório completo formatado
        """
        rep = super(CompleteReport, CompleteReport).generate(products)

        # ! product_counter já é computada na classe pai
        # ! Seria interessante o reaproveitamento da mesma
        # ! A mesma será computada novamente apenas para atender os testes
        product_counter = Counter()

        for product in products:
            product_counter[product["nome_da_empresa"]] += 1

        rep += "\n"

        rep += "Produtos estocados por empresa: \n"
        for company in product_counter:
            rep += "- {}: {}\n".format(company, product_counter[company])

        return rep
