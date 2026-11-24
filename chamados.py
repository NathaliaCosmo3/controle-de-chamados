import sqlite3
from pathlib import Path

BANCO = Path(__file__).with_name("chamados.db")


def ler_texto(rotulo):
    while True:
        valor = input(rotulo).strip()
        if valor:
            return valor
        print("Preencha este campo.")


def executar(conexao):
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS chamados (
            id INTEGER PRIMARY KEY,
            titulo TEXT NOT NULL,
            descricao TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Aberto'
        )
    """)

    while True:
        print("\n1. Cadastrar | 2. Listar | 3. Resolver | 0. Sair")
        opcao = input("Opção: ").strip()
        if opcao == "0":
            return
        if opcao == "1":
            titulo = ler_texto("Título: ")
            descricao = ler_texto("Descrição: ")
            with conexao:
                chamado = conexao.execute(
                    "INSERT INTO chamados (titulo, descricao) VALUES (?, ?)",
                    (titulo, descricao),
                )
            print(f"Chamado #{chamado.lastrowid} cadastrado.")
        elif opcao == "2":
            chamados = conexao.execute(
                "SELECT id, titulo, descricao, status FROM chamados ORDER BY id"
            ).fetchall()
            if not chamados:
                print("Nenhum chamado cadastrado.")
            for numero, titulo, descricao, status in chamados:
                print(f"#{numero} [{status}] {titulo} — {descricao}")
        elif opcao == "3":
            try:
                numero = int(input("Número do chamado: "))
                if not 1 <= numero <= 2**63 - 1:
                    raise ValueError
            except ValueError:
                print("Informe um número de chamado válido.")
                continue
            with conexao:
                alteracao = conexao.execute(
                    "UPDATE chamados SET status = 'Resolvido' "
                    "WHERE id = ? AND status = 'Aberto'",
                    (numero,),
                )
            if alteracao.rowcount:
                print(f"Chamado #{numero} resolvido.")
            else:
                print("Chamado inexistente ou já resolvido.")
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    conexao = sqlite3.connect(BANCO)
    try:
        executar(conexao)
    except (EOFError, KeyboardInterrupt):
        print("\nPrograma encerrado.")
    finally:
        conexao.close()
