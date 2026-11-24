# Controle de chamados

## Baixar e abrir no navegador

**[Baixar projeto em ZIP](https://github.com/NathaliaCosmo3/controle-de-chamados/archive/refs/heads/main.zip)**

1. Extraia o ZIP. No Windows, clique com o botão direito no arquivo e escolha **Extrair Tudo**.
2. Na pasta extraída, abra `index.html` com duplo clique. A interface funciona offline e dispensa instalação.

Na interface, cadastre com prioridade, pesquise por título ou número, filtre por status e exporte a lista exibida em CSV. Os chamados ficam no navegador usado e podem ser reabertos. A versão visual tem armazenamento próprio e o programa Python usa o banco SQLite.

## Versão em Python para terminal


Projeto de portfólio inspirado na rotina de suporte técnico. Registra chamados com título e descrição, lista os registros e muda o status de Aberto para Resolvido. O SQLite mantém os dados entre execuções.

## Como executar

Use Python 3 e execute `python chamados.py` na pasta do projeto. O programa cria `chamados.db` automaticamente.

## Exemplo

Cadastre o chamado fictício “Impressora offline”, liste os registros para conferir seu número e escolha **Resolver** para atualizar o status.

Ferramentas: Python e SQLite da biblioteca padrão. Projeto de portfólio desenvolvido com assistência de IA.
