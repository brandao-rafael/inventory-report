# from simple_report import SimpleReport

from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products):
        company_most_products = CompleteReport.counter_products_by_company(
            products
        )
        expiration_close = CompleteReport.get_expiration_close(products)
        older_date = CompleteReport.get_older_date(products)
        company_with_products = CompleteReport.get_products_by_company(
            products
        )

        product_list = [
            f"- {key}: {value}" for key, value in company_with_products.items()
        ]
        product_string = "\n".join(product_list)
        return (
            f"Data de fabricação mais antiga: {older_date}\n"
            f"Data de validade mais próxima: {expiration_close}\n"
            f"Empresa com mais produtos: {company_most_products}\n"
            f"Produtos estocados por empresa:\n"
            f"{product_string}\n"
        )

    @staticmethod
    def get_products_by_company(products: list):
        companies_with_products = {}
        for product in products:
            if product["nome_da_empresa"] not in companies_with_products:
                companies_with_products[product["nome_da_empresa"]] = 0
            companies_with_products[product["nome_da_empresa"]] += 1

        return companies_with_products
