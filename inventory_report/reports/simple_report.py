from collections import Counter
from datetime import datetime, timedelta
from typing import Dict, List


class SimpleReport(object):
    @staticmethod
    def generate(products: List[Dict]) -> str:
        """Gera um relatório simples

        Args:
            dados (List[Dict]): uma lista contendo estruturas do tipo dict

        Returns:
            str: relatório simples formatado
        """

        oldest_fabrication_date = datetime.max
        next_validation_date = datetime.max
        product_counter = Counter()

        for product in products:

            # get oldest fabrication date
            formatted_fabrication_date = datetime.strptime(
                product["data_de_fabricacao"], "%Y-%m-%d"
            )
            if formatted_fabrication_date < oldest_fabrication_date:
                oldest_fabrication_date = formatted_fabrication_date

            # get next validation date (after yesterday)
            formatted_validation_date = datetime.strptime(
                product["data_de_validade"], "%Y-%m-%d"
            )
            yesterday = datetime.now() - timedelta(1)
            if (formatted_validation_date < next_validation_date) and (
                formatted_validation_date > yesterday
            ):
                next_validation_date = formatted_validation_date

            # update products counter each iteration
            product_counter[product["nome_da_empresa"]] += 1

        # get company with more products
        target_company = product_counter.most_common(1)[0][0]

        # generate simple report
        rep = "Data de fabricação mais antiga: {}\n".format(
            datetime.strftime(oldest_fabrication_date, "%Y-%m-%d")
        )
        rep += "Data de validade mais próxima: {}\n".format(
            datetime.strftime(next_validation_date, "%Y-%m-%d")
        )
        rep += (
            "Empresa com maior quantidade de produtos estocados: {}\n".format(
                target_company
            )
        )

        return rep
