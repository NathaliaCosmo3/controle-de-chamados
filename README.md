# Controle de chamados

## Abrir a versão visual

1. Abra o [arquivo index.html](https://github.com/NathaliaCosmo3/controle-de-chamados/blob/main/index.html).
2. Na barra acima do código, clique no ícone de download (**Download raw file**).
3. Na pasta **Downloads**, abra `index.html` com dois cliques. Ele funciona offline no Chrome ou Edge, sem instalar Python.

**[Baixar todos os arquivos em ZIP](https://github.com/NathaliaCosmo3/controle-de-chamados/archive/refs/heads/main.zip)**

Cadastre e edite chamados, acompanhe os indicadores de pendências e resoluções, altere o status e exporte a lista filtrada em CSV. Os chamados ficam no navegador usado.

## Versão em Python para terminal

Projeto de portfólio inspirado na rotina de suporte técnico. Registra chamados com título e descrição, lista os registros e muda o status de Aberto para Resolvido. O SQLite mantém os dados entre execuções.

## Como executar

Use Python 3 e execute `python chamados.py` na pasta do projeto. O programa cria `chamados.db` automaticamente.

## Exemplo

Cadastre o chamado fictício “Impressora offline”, liste os registros para conferir seu número e escolha **Resolver** para atualizar o status.

Ferramentas: Python e SQLite da biblioteca padrão. Projeto de portfólio desenvolvido com assistência de IA.
