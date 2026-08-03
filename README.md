# NOWS Picture

Aplicativo para renomear, reordenar, redimensionar e aplicar marca-d'água em imagens.

## Requisitos

- Windows
- Python 3.13 ou 3.14
- PowerShell
- Poetry

## 1. Instalar o Python

1. Acesse [python.org/downloads](https://www.python.org/downloads/).
2. Baixe e execute o instalador do Python 3.14.
3. Se o instalador exibir a opção **Add Python to PATH**, marque-a.
4. Conclua a instalação.
5. Feche e abra novamente o PowerShell.

Confirme a instalação:

```powershell
py -3.14 --version
```

O resultado deverá ser semelhante a:

```text
Python 3.14.x
```

> O projeto requer Python 3.13 ou 3.14. Os comandos abaixo usam o Python 3.14.

## 2. Instalar o Poetry

Primeiro, instale o `pipx`:

```powershell
py -3.14 -m pip install --user pipx
```

Adicione os comandos instalados pelo `pipx` ao `PATH`:

```powershell
py -3.14 -m pipx ensurepath
```

Instale o Poetry:

```powershell
py -3.14 -m pipx install poetry
```

Feche e abra novamente o PowerShell. Em seguida, verifique a instalação:

```powershell
poetry --version
```

## 3. Baixar ou abrir o projeto

Abra o PowerShell na pasta do projeto. Se o projeto já estiver no computador:

```powershell
cd "C:\caminho\para\NOWS-Picture"
```

Substitua o caminho do exemplo pela localização real do projeto.

## 4. Selecionar o Python do ambiente virtual

Na pasta do projeto, execute:

```powershell
poetry env use 3.14
```

O Poetry criará ou selecionará um ambiente virtual com essa versão do Python.

## 5. Instalar as dependências

Execute:

```powershell
poetry install --no-root
```

O Poetry instalará as bibliotecas definidas em `pyproject.toml`, incluindo as dependências necessárias para processar imagens. A opção `--no-root` é usada porque este projeto é executado diretamente pelo arquivo `main.py`, em vez de ser instalado como um pacote Python.

## 6. Executar o programa

Ainda na pasta do projeto, execute:

```powershell
poetry run python main.py
```

Não é necessário ativar manualmente o ambiente virtual quando se utiliza `poetry run`.

## Uso diário

Depois que a instalação inicial estiver concluída, basta abrir o PowerShell na pasta do projeto e executar:

```powershell
poetry run python main.py
```

## Comandos úteis

Exibir informações sobre o ambiente virtual:

```powershell
poetry env info
```

Listar os ambientes virtuais do projeto:

```powershell
poetry env list
```

Verificar a versão do Python usada pelo projeto:

```powershell
poetry run python --version
```

Atualizar ou reinstalar as dependências após alterações no projeto:

```powershell
poetry install --no-root
```

## Solução de problemas

### O comando `py` não foi encontrado

O Python não está instalado corretamente ou o inicializador do Python não está disponível. Reinstale o Python e marque a opção para adicioná-lo ao `PATH`.

### O comando `poetry` não foi encontrado

Feche e abra novamente o PowerShell depois de executar `pipx ensurepath`.

Se o problema continuar, reinstale o Poetry:

```powershell
py -3.14 -m pipx install poetry
```

### O Poetry está usando uma versão incorreta do Python

Selecione novamente o Python 3.14:

```powershell
poetry env use 3.14
poetry install --no-root
```

### Recriar o ambiente virtual

Liste os ambientes existentes:

```powershell
poetry env list
```

Remova o ambiente associado ao projeto:

```powershell
poetry env remove --all
```

Depois, crie-o novamente e reinstale as dependências:

```powershell
poetry env use 3.14
poetry install --no-root
```
