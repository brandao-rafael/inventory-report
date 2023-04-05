from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.complete_report import CompleteReport


def test_decorar_relatorio():
    products = [
        {
            "id": 95432,
            "nome_do_produto": "Produto ficticio",
            "nome_da_empresa": "Empresa ficticia",
            "data_de_fabricacao": "2019-08-10",
            "data_de_validade": "2024-08-25",
            "numero_de_serie": "nsf021585",
            "instrucoes_de_armazenamento": "local seco e arejado",
        },
        {
            "id": 95433,
            "nome_do_produto": "Produto muito ficticio",
            "nome_da_empresa": "Empresa muito ficticia",
            "data_de_fabricacao": "2020-05-10",
            "data_de_validade": "2023-09-10",
            "numero_de_serie": "nsf021587",
            "instrucoes_de_armazenamento": "local seco, fresco e arejado",
        },
    ]
    colored_report = ColoredReport(CompleteReport)
    report_result = colored_report.generate(products)
    assert report_result == (
        "\033[32mData de fabricação mais antiga:\033[0m"
        + " \033[36m2019-08-10\033[0m\n"
        "\033[32mData de validade mais próxima:\033[0m"
        + " \033[36m2023-09-10\033[0m\n"
        "\033[32mEmpresa com mais produtos:\033[0m"
        + " \033[31mEmpresa ficticia\033[0m\n"
        "Produtos estocados por empresa:\n"
        "- Empresa ficticia: 1\n"
        "- Empresa muito ficticia: 1\n"
    )
