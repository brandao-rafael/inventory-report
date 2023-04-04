from inventory_report.inventory.product import Product


def test_cria_produto():
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

    assert produto_ficticio.id == product["id"]
    assert produto_ficticio.nome_do_produto == product["nome_do_produto"]
    assert produto_ficticio.nome_da_empresa == product["nome_da_empresa"]
    assert produto_ficticio.data_de_fabricacao == product["data_de_fabricacao"]
    assert produto_ficticio.data_de_validade == product["data_de_validade"]
    assert produto_ficticio.numero_de_serie == product["numero_de_serie"]
    # indented in autosave by flake8
    assert (
        produto_ficticio.instrucoes_de_armazenamento
        == product["instrucoes_de_armazenamento"]
    )
