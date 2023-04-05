from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = {
        "id": 95432,
        "nome_do_produto": "Produto ficticio",
        "nome_da_empresa": "Empresa ficticia",
        "data_de_fabricacao": "10/08/2019",
        "data_de_validade": "25/08/2024",
        "numero_de_serie": "nsf021585",
        "instrucoes_de_armazenamento": "local seco e arejado",
    }

    produto_ficticio = Product(
        product["id"],
        product["nome_do_produto"],
        product["nome_da_empresa"],
        product["data_de_fabricacao"],
        product["data_de_validade"],
        product["numero_de_serie"],
        product["instrucoes_de_armazenamento"],
    )

    expected = (
        "O produto Produto ficticio fabricado em 10/08/2019"
        + " por Empresa ficticia com validade até 25/08/2024"
        + " precisa ser armazenado local seco e arejado."
    )

    assert produto_ficticio.__repr__() == expected
