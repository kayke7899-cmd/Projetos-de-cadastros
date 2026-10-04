# 🗂️ Projetos de Cadastros

Coleção de scripts em **Python** desenvolvidos durante meus estudos em Análise e Desenvolvimento de Sistemas. O foco é consolidar os fundamentos de lógica de programação: **listas**, **laços de repetição** (`while` e `for`), **condicionais** e **entrada e saída de dados** pelo terminal.

Todos os projetos seguem a mesma ideia: ler dados digitados pelo usuário, guardá-los em listas paralelas (o mesmo índice em cada lista representa o mesmo registro) e exibi-los no final.

## 📁 Projetos

| Arquivo | O que faz |
| --- | --- |
| [`biblioteca.py`](biblioteca.py) | Cadastra livros (título e autor) e exibe um catálogo formatado |
| [`piloto_e_carro.py`](piloto_e_carro.py) | Registra pilotos e seus carros e mostra a lista final |
| [`sistema_cadastro.py`](sistema_cadastro.py) | Sistema com menu para cadastrar e listar nome, CPF e telefone |

---

### 📚 `biblioteca.py` — Cadastro de livros

Pede o **título** e o **autor** de cada livro em loop, até o usuário digitar `sair`. Ao final, exibe uma "Biblioteca Virtual" com o título centralizado e a lista de livros cadastrados.

**Conceitos praticados:** listas, `while True` com `break`, `f-strings` com alinhamento (`:<15`), `str.center()` e `range(len(...))`.

**Exemplo de saída:**

```text
==============================
      BIBLIOTECA VIRTUAL
==============================
Livro: Dom Casmurro   |Autor: Machado de Assis
Livro: O Cortico      |Autor: Aluisio Azevedo
```

---

### 🏎️ `piloto_e_carro.py` — Pilotos e carros

Registra o **nome do piloto** e o **nome do carro** dele, em loop, até digitar `sair`. A cada registro o programa confirma com "Registrado!" e, no final, mostra a lista completa no formato `piloto->carro`.

**Conceitos praticados:** duas listas paralelas, `input()`, `.lower()` para aceitar `sair` em qualquer capitalização, `break` e `for` com `range(len(...))`.

**Exemplo de saída:**

```text
 LISTA DE PILOTOS E CARROS:
Senna->McLaren MP4/4
```

---

### 👤 `sistema_cadastro.py` — Cadastro com menu

Sistema de cadastro com **menu interativo** que se repete até o usuário escolher sair:

```text
===MENU===
1. Cadastrar informações
2. Listar nomes cadastrados
3. Sair
```

- **1 – Cadastrar:** pede nome, CPF e telefone e guarda nas listas
- **2 – Listar:** mostra todos os registros ou avisa que não há nenhum cadastrado
- **3 – Sair:** encerra o programa
- Qualquer outra opção exibe "Opção inválida" e o menu volta

**Conceitos praticados:** menu com `while True`, `if` / `elif` / `else`, três listas paralelas, verificação de lista vazia (`if not lista`) e controle de fluxo.

---

## ▶️ Como executar

**Pré-requisito:** [Python 3](https://www.python.org/downloads/) instalado.

```bash
# Clone o repositório
git clone https://github.com/kayke7899-cmd/Projetos-de-cadastros.git
cd Projetos-de-cadastros

# Execute o projeto que quiser
python biblioteca.py
python piloto_e_carro.py
python sistema_cadastro.py
```

> No Linux e no macOS, use `python3` no lugar de `python`.

Os dados ficam apenas na memória: ao encerrar o programa, os cadastros são perdidos.

## 👨‍💻 Autor

**Kayke Augusto** — estudante de Análise e Desenvolvimento de Sistemas, com foco em desenvolvimento Back-End.

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kayke-augusto-473264413)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/kayke7899-cmd)
