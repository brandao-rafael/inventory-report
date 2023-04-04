from datetime import datetime


class SimpleReport:
    def __init__(self, products: list) -> None:
        self._products = products

    @staticmethod
    def convert_to_date(date: str):
        return datetime.strptime(date, "%Y-%m-%d").date()

    @staticmethod
    def counter_products_by_company(products):
        company_counter = {}
        for product in products:
            company = product["nome_da_empresa"]
            if company not in company_counter:
                company_counter[company] = 1
            else:
                company_counter[company] += 1

        return max(company_counter, key=company_counter.get)

    @staticmethod
    def get_older_date(products):
        older_date = SimpleReport.convert_to_date(
            products[0]["data_de_fabricacao"]
        )
        for product in products:
            date_converted = SimpleReport.convert_to_date(
                product["data_de_fabricacao"]
            )
            if date_converted < older_date:
                older_date = date_converted
        return older_date

    @staticmethod
    def get_expiration_close(products):
        expired = []
        not_expired = []
        for product in products:
            date_converted = SimpleReport.convert_to_date(
                product["data_de_validade"]
            )
            if date_converted < datetime.today().date():
                expired.append(product)
            else:
                not_expired.append(product["data_de_validade"])
        return sorted(not_expired)[0]

    @staticmethod
    def generate(products):
        company_most_products = SimpleReport.counter_products_by_company(
            products
        )
        expiration_close = SimpleReport.get_expiration_close(products)
        older_date = SimpleReport.get_older_date(products)

        #         return f"""
        # Data de fabricação mais antiga: {older_date}
        # Data de validade mais próxima: {expiration_close}
        # Empresa com mais produtos: {company_most_products}"""
        return (
            f"Data de fabricação mais antiga: {older_date}\n"
            f"Data de validade mais próxima: {expiration_close}\n"
            f"Empresa com mais produtos: {company_most_products}"
        )
