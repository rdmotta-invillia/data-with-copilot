<h1 align="center">Data + GitHub Copilot para soluções avançadas de dados</h1>
<em align="center">The perfect pairing ™</em>

## Introdução

Este repositório contém o código-fonte do workshop completo. Você seguirá o guia passo a passo abaixo, concluindo todas as etapas enquanto trabalha com dados e GitHub Copilot dentro do Codespaces.

> [!NOTE]
> Este repo foi pensado para apresentar vários recursos do **GitHub Copilot**, como **Copilot Chat** e **inline chat**. Por isso, os guias passo a passo abaixo contêm uma descrição geral do que precisa ser feito, e o Copilot Chat ou o inline chat podem ajudar você a gerar os comandos necessários.
>
> Cada etapa, quando aplicável, também contém uma `Cheatsheet`, que pode ser usada para validar a(s) sugestão(ões) do Copilot em relação ao comando correto.
>
> 💡 Experimente prompts diferentes e observe como isso afeta a precisão das sugestões do GitHub Copilot. Por exemplo, ao usar inline chat, você pode usar um prompt adicional para refinar a resposta sem precisar reescrever o prompt inteiro.

## Recursos do projeto de dados

Neste workshop, você trabalhará com dados de um arquivo CSV incluído neste repositório, bem como com um arquivo de script Python que irá interagir com o arquivo CSV. Aqui estão alguns recursos do projeto com o qual você vai trabalhar:

1. Consumir um dataset CSV e realizar transformações
1. Identificar e implementar validações
1. Criar uma ferramenta de linha de comando que possa ser usada em ambientes de CI/CD

## Preparação

Este repositório está pronto para Codespaces e já vem pré-configurado para que você tenha todas as dependências instaladas, incluindo as extensões do Visual Studio Code necessárias para trabalhar com GitHub Copilot e Python:

- GitHub Copilot
- Python extension
- Dependências Python pré-instaladas com um Virtual Environment ativado

> [!NOTE]
> Se você estiver usando este repositório na sua conta ou em uma organização que não seja GitHub-Universe, poderá incorrer em cobranças ou no consumo da sua cota gratuita de Codespaces.

### 1. Crie um novo repositório a partir deste template

Progress: [🟢⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪] 1/12 (8%)

⏳ **~2min**

- Clique em `Use this template` :point_right: `Create a new repository`
- Defina o owner como a organização do GitHub Workshop: `githubuniverseworkshop`
- Dê um nome ao repositório
- Defina a visibilidade como `Private`
- Clique em `Create repository`

### 2. Crie um Codespace usando o template fornecido

Progress: [🟢🟢⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪] 2/12 (16%)

⏳ **~3min**

- No repo recém-criado, clique em `Code` :point_right: `Codespaces` :point_right: `[ellipsis menu]` :point_right: `New with options` :point_right: _Certifique-se de que `Dev container configuration` esteja definido como `Default project configuration`_ :point_right: `Create codespace`
- ❗Se você estiver tendo problemas para iniciar o Codespace, também pode clonar o repo e continuar a partir daqui na sua IDE:

    ```sh
    git clone https://github.com/<YOUR_NAME_SPACE>/<YOUR_REPO_NAME>.git
    cd <YOUR_REPO_NAME>
    ```

    > 📝 **Nota:** Não há necessidade de fazer push das alterações de volta para o repo durante o workshop

### 3. Verifique se o Python está instalado e configurado corretamente

Progress: [🟢🟢🟢⚪⚪⚪⚪⚪⚪⚪⚪⚪] 3/12 (25%)

⏳ **~2min**

- Use a command palette para abrir o terminal (procure por "Create new terminal")
- Execute `which python` e confirme que ele aponta para o Virtual Environment (`home/vscode/venv/bin/python`)
- Execute `which pip` e confirme que ele também aponta para o Virtual Environment (`home/vscode/venv/bin/pip`)

### 4. Execute os scripts Python

Progress: [🟢🟢🟢🟢⚪⚪⚪⚪⚪⚪⚪⚪] 4/12 (33%)

⏳ **~2min**

- Execute o script `main.py` e confirme que nenhum erro ocorre:

    ```shell
    python3 main.py
    ```

- Execute o script `check.py` e confirme que nenhum erro ocorre:

    ```shell
    python3 check.py
    ```

    Deve haver algumas linhas com OK e algumas com FAIL:

    ```shell
    [OK  ]   verify_drop_notes
    [FAIL]   verify_high_ratings - Not all ratings are 90 or higher.
    [FAIL]   verify_one_hot_encoding - The 'Red Wine' column was not one-hot encoded correctly.
    [OK  ]   verify_remove_newlines_carriage_returns
    [FAIL]   verify_ratings_to_int - The 'ratings' column was not converted to integers correctly.
    ```

### 5. Abra os arquivos relevantes

Progress: [🟢🟢🟢🟢🟢⚪⚪⚪⚪⚪⚪⚪] 5/12 (41%)

⏳ **~2min**

O GitHub Copilot se beneficia de ter contexto. Uma forma de melhorar esse contexto é abrir arquivos relevantes.

- Abra os arquivos `main.py`, `check.py`, `train.csv` e `transformed_train.csv`

## Desenvolvimento

### 1. Veja o quanto você consegue aprender sobre o projeto e os dados

Progress: [🟢🟢🟢🟢🟢🟢⚪⚪⚪⚪⚪⚪] 6/12 (50%) - Metade do caminho!

⏳ **~5min**

- Abra o GitHub Copilot Chat
- Use o agent `@workspace` para perguntar ao Copilot o que os arquivos `main.py` e `check.py` estão fazendo
- Novamente, com o agent `@workspace`, pergunte ao Copilot qual é a natureza dos dados com os quais você vai trabalhar

#### 2. Corrija a função de high ratings

Progress: [🟢🟢🟢🟢🟢🟢🟢⚪⚪⚪⚪⚪] 7/12 (58%)

⏳ **~3min**

- Em `main.py`, encontre a função `select_high_ratings()`
- Posicione o cursor na assinatura da função ou em algum ponto do corpo
- Abra o inline chat com `Ctrl-i` ou `Cmd-i` (no Mac)
- Prefixe seu prompt com o slash command `/explain`
- Pergunte por que essa função pode não estar funcionando e implemente as correções sugeridas
- Gere novamente `transformed_train.csv` executando `python3 main.py`
- Verifique a correção executando `python3 check.py` até que essa função retorne `OK`

<details>
<summary>Cheatsheet</summary>

##### Prompt

```sh
/explain por que esta função pode não estar funcionando corretamente?
```

##### Saída esperada

```sh
Com base no código fornecido, existem alguns motivos possíveis pelos quais a função `select_high_ratings` pode não estar funcionando corretamente:

1. Erro de digitação no nome da coluna: a função verifica se o nome da coluna 'ratings' existe no DataFrame `df.columns`. Se houver um erro de digitação no nome da coluna, como 'rating' em vez de 'ratings', a condição `if 'ratings' in df.columns`

```

</details>

> [!NOTE]
> Sinta-se à vontade para usar o GitHub Copilot Chat para implementar ou corroborar a correção

#### 3. Corrija o problema de one-hot encoding

Progress: [🟢🟢🟢🟢🟢🟢🟢🟢⚪⚪⚪⚪] 8/12 (66%)

⏳ **~3min**

- Selecione a função `drop_and_one_hot_encode_red_wine()` e abra o inline chat (`Ctrl-i`/ `Cmd-i`)
- Use o slash command `/fix` para pedir ao GitHub Copilot que sugira uma possível correção
- Gere novamente `transformed_train.csv` executando `python3 main.py`
- Verifique a correção executando `python3 check.py` até que essa função retorne `OK`

<details>
<summary>Cheatsheet</summary>

##### Prompt

```sh
Esta função não está fazendo one-hot encoding na coluna variety
```

##### Saída esperada

```python
def drop_and_one_hot_encode_red_wine(df):
    """
    Create a 'Red_Wine' column that is 1 if 'variety' is 'Red Wine' and 0 otherwise.
    Drop the original 'variety' column.
    """
    if 'variety' in df.columns:
        df['Red_Wine'] = df['variety'].apply(lambda x: 1 if x == 'Red Wine' else 0)
        df = df.drop(columns=['variety'])
    return df
```

</details>

#### 4. Corrija a conversão de ratings para int

Progress: [🟢🟢🟢🟢🟢🟢🟢🟢🟢⚪⚪⚪] 9/12 (75%)

⏳ **~3min**

- Se a validação `verify_ratings_to_int` já estiver como "OK", então o Copilot pode já ter corrigido esse problema para você. Caso contrário, continue com as etapas abaixo.
- Selecione a função `convert_ratings_to_int()` e abra o inline chat (`Ctrl-i` / `Cmd-i`)
- Use o slash command `/explain` para perguntar ao GitHub Copilot por que essa função pode não estar funcionando corretamente
- Identifique o problema e implemente a correção
- Gere novamente `transformed_train.csv` executando `python3 main.py`
- Verifique a correção executando `python3 check.py` até que essa função retorne `OK`

<details>
<summary>Cheatsheet</summary>

##### Prompt

```sh
Esta função não está convertendo os ratings para inteiros
```

##### Saída esperada

```python
def convert_ratings_to_int(df):
    """
    Convert the 'rating' column from float to integer.
    """
    if 'rating' in df.columns:
        df['rating'] = df['rating'].to_int()
    return df
```

</details>

## Testes

Um projeto Python robusto pode se beneficiar de testes. Você adicionará alguns unit tests e aprenderá mais sobre como executá-los com a ajuda do GitHub Copilot.

Certifique-se de que o terminal está aberto usando a command palette e digitando `toggle terminal`

### 1. Teste sua CLI

Progress: [🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢⚪⚪] 10/12 (83%)

⏳ **~5min**

- Este projeto já tem o test runner e framework Pytest pré-instalados; confirme que ele está disponível executando `pytest --version`
- Execute os testes dentro do diretório `workshop` usando o seguinte comando: `pytest -v`

A saída deve mostrar uma falha.

#### 2. Corrija o teste com falha

Progress: [🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢⚪] 11/12 (91%)

⏳ **~5min**

- Selecione a saída no terminal e cole-a no GitHub Copilot Chat, prefixando com um pedido de correção e explicação
- Use a saída do chat para implementar uma correção em `test_main.py`

<details>
<summary>Cheatsheet</summary>

##### Prompt

```sh
Corrija o teste e explique a correção:
// Copie e cole aqui a saída do terminal
```

##### Saída esperada

O erro ocorre porque a função `drop_notes` provavelmente está modificando o DataFrame in place, em vez de retornar um novo DataFrame sem a coluna 'notes'. Para corrigir o teste, precisamos garantir que a função `drop_notes` retorne um novo DataFrame sem a coluna 'notes' e então verificar as colunas desse novo DataFrame.

Aqui está a função de teste corrigida:

```python
def test_drop_notes_column_dropped():
    # Cria um DataFrame de exemplo com a coluna 'notes'
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'notes': ['note1', 'note2', 'note3']})

    # Chama a função drop_notes e obtém o resultado
    result = main.drop_notes(df)
    
    # Verifica se a coluna 'notes' foi removida do DataFrame de resultado
    columns = result.columns.to_list()
    assert columns == ['A', 'B']
```

Ao armazenar o resultado da função `drop_notes` em uma nova variável e verificar suas colunas, garantimos que o teste valide corretamente o comportamento da função.

</details>

#### 3. Adicione testes para a função de one hot encoding

Progress: [🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢] 12/12 (100%) - 🎉 Comemore!

⏳ **~5min**

- Garanta que `python check.py` retorne apenas resultados com OK; caso contrário, esta etapa pode não funcionar.
- Selecione a função `drop_and_one_hot_encode_red_wine` em `main.py`
- Abra o inline chat com `Ctrl-i`/`Cmd-i`
- Use o slash command `/tests` para obter sugestões de testes
- Revise a saída, aceite-a e valide com o comando `pytest -v`. Todos os testes devem passar, e você deverá ter mais testes do que antes. Às vezes, o Copilot indenta os testes sugeridos incorretamente, colocando-os dentro de uma função de teste existente; então, confirme que a indentação está correta antes de executá-los.

<details>
<summary>Cheatsheet</summary>

##### Prompt

```sh
/tests
```

##### Saída esperada

```python
def test_drop_and_one_hot_encode_red_wine_red_wine_column_created():
    # Cria um DataFrame de exemplo com a coluna 'variety'
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'variety': ['Red Wine', 'White Wine', 'Red Wine']})

    # Chama a função drop_and_one_hot_encode_red_wine
    result = main.drop_and_one_hot_encode_red_wine(df)

    # Verifica se a coluna 'Red_Wine_Red Wine' foi criada
    assert 'Red_Wine_Red Wine' in result.columns

def test_drop_and_one_hot_encode_red_wine_red_wine_column_encoded():
    # Cria um DataFrame de exemplo com a coluna 'variety'
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'variety': ['Red Wine', 'White Wine', 'Red Wine']})

    # Chama a função drop_and_one_hot_encode_red_wine
    result = main.drop_and_one_hot_encode_red_wine(df)

    # Verifica se a coluna 'Red_Wine_Red Wine' foi codificada corretamente
    assert result['Red_Wine_Red Wine'].tolist() == [1, 0, 1]

def test_drop_and_one_hot_encode_red_wine_variety_column_dropped():
    # Cria um DataFrame de exemplo com a coluna 'variety'
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'variety': ['Red Wine', 'White Wine', 'Red Wine']})

    # Chama a função drop_and_one_hot_encode_red_wine
    result = main.drop_and_one_hot_encode_red_wine(df)

    # Verifica se a coluna 'variety' foi removida
    assert 'variety' not in result.columns

def test_drop_and_one_hot_encode_red_wine_dataframe_unchanged():
    # Cria um DataFrame de exemplo com a coluna 'variety'
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'variety': ['Red Wine', 'White Wine', 'Red Wine']})

    # Chama a função drop_and_one_hot_encode_red_wine
    result = main.drop_and_one_hot_encode_red_wine(df)

    # Verifica se o shape do DataFrame permaneceu inalterado
    assert result.shape == (3, 3)

    # Verifica se o DataFrame original não foi modificado
    assert 'variety' in df.columns
    assert df.shape == (3, 3)
```

</details>

## Bônus

Há alguns desafios bônus caso você tenha concluído todas as tarefas e seus scripts estejam em bom estado.

### Desafio Bônus 1 - Crie uma ferramenta CLI robusta

Progress: [🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢] 12/12 (100%) 🎉  
Optional: [🚀 Turbo Boost! (1/2) 33%]  

- Use o GitHub Copilot chat com o prefixo `@workspace` para converter o projeto em uma CLI com opções e um menu de ajuda
- Garanta que o prompt especifique que não devem ser usadas dependências externas e que apenas a standard library seja utilizada

<details>
<summary>Cheatsheet</summary>

#### Prompt

```shell
@workspace Quero converter este projeto em uma CLI com um menu de ajuda. Ajude-me a fazer isso sem usar dependências, apenas com a Python standard library
```

#### Saída esperada

```python
def main():
    parser = argparse.ArgumentParser(description="DataFrame manipulation CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("drop_notes", help="Drop the 'notes' column from the DataFrame")
    subparsers.add_parser("select_high_ratings", help="Select rows where the 'rating' column is 90 or higher")
    subparsers.add_parser("drop_and_one_hot_encode_red_wine", help="One-hot encode 'Red Wine' and drop 'variety' column")
    subparsers.add_parser("remove_newlines_carriage_returns", help="Remove newlines and carriage returns from string columns")
    subparsers.add_parser("convert_ratings_to_int", help="Convert the 'rating' column from float to integer")

    args = parser.parse_args()

    # Load your DataFrame here
    df = pd.read_csv('workshop/train.csv')

    if args.command == "drop_notes":
        df = drop_notes(df)
    elif args.command == "select_high_ratings":
        df = select_high_ratings(df)
    elif args.command == "drop_and_one_hot_encode_red_wine":
        df = drop_and_one_hot_encode_red_wine(df)
    elif args.command == "remove_newlines_carriage_returns":
        df = remove_newlines_carriage_returns(df)
    elif args.command == "convert_ratings_to_int":
        df = convert_ratings_to_int(df)
    else:
        parser.print_help()

    # Save the transformed DataFrame
    df.to_csv('workshop/transformed_train.csv', index=False)

if __name__ == "__main__":
    main()
```

</details>

### Desafio Bônus 2 - Documente seu projeto

Progress: [🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢] 12/12 (100%) 🎉  
Optional: [🚀 Turbo Boost! (1/2) 33%]  
Optional: [🌟 Extra Points! (2/2) 66%]  

- Crie uma nova pasta `docs/` e um arquivo chamado `README.md`
- Use o GitHub Copilot chat com o prefixo `@workspace` para começar a documentar seu projeto usando Markdown em um `README.md`
- No prompt, peça ajuda para documentar os objetivos do projeto, a natureza dos dados nos arquivos CSV e o funcionamento da CLI.

<details>
<summary>Cheatsheet</summary>

#### Prompt

```shell
@workspace ajude-me a criar um bom arquivo README.md em Markdown para documentar este projeto e ajudar outras pessoas a entender como ele funciona e a natureza dos dados
```

#### Saída esperada

```markdown
# DataFrame Manipulation CLI

Este projeto fornece uma command-line interface (CLI) para manipular um DataFrame usando várias operações. A CLI é construída com a Python standard library e não requer dependências externas.

## Sumário

- [Installation](#installation)
- [Usage](#usage)
  - [Commands](#commands)
- [Data](#data)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone o repositório:
    ```sh
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Configure um virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instale os pacotes necessários:
    ```sh
    pip install -r workshop/requirements.txt
    ```

## Usage

Para usar a CLI, navegue até o diretório `workshop` e execute o script `main.py` com o comando desejado.

### Commands

- `drop_notes`: Remove a coluna 'notes' do DataFrame.
- `select_high_ratings`: Seleciona as linhas em que a coluna 'rating' é 90 ou maior.
- `drop_and_one_hot_encode_red_wine`: Aplica one-hot encoding em 'Red Wine' e remove a coluna 'variety'.
- `remove_newlines_carriage_returns`: Remove newlines e carriage returns das colunas de texto.
- `convert_ratings_to_int`: Converte a coluna 'rating' de float para integer.

### Exemplos

1. Remover a coluna 'notes':
    ```sh
    python3 main.py drop_notes
    ```

2. Selecionar linhas com ratings altos:
    ```sh
    python3 main.py select_high_ratings
    ```

3. Aplicar one-hot encoding em 'Red Wine' e remover a coluna 'variety':
    ```sh
    python3 main.py drop_and_one_hot_encode_red_wine
    ```

4. Remover newlines e ajustar os caractere de retorno das colunas de texto:
    ```sh
    python3 main.py remove_newlines_carriage_returns
    ```

5. Converter a coluna 'rating' para integer:
    ```sh
    python3 main.py convert_ratings_to_int
    ```

## Data

Os dados usados neste projeto estão armazenados em arquivos CSV localizados no diretório `workshop`. O arquivo principal é `train.csv`, que contém as seguintes colunas:

- `notes`: Notas de texto sobre os dados.
- `ratings`: Avaliações numéricas dos dados.
- `variety`: A variedade dos dados, por exemplo, 'Red Wine'.

Os dados transformados são salvos em `transformed_train.csv` após a aplicação dos comandos da CLI.

## Contributing

Contribuições são bem-vindas. Siga estas etapas para contribuir:

1. Faça um fork do repositório.
2. Crie uma nova branch (`git checkout -b feature-branch`).
3. Faça suas alterações.
4. Faça commit das alterações (`git commit -m 'Add new feature'`).
5. Faça push para a branch (`git push origin feature-branch`).
6. Abra um pull request.

## License

Este projeto está licenciado sob a MIT License. Consulte o arquivo [LICENSE](../LICENSE) para mais detalhes.
```

</details>

### Desafio Bônus 3 - Automatize a transformação de dados

Progress: [🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢] 12/12 (100%) 🎉  
Optional: [🚀 Turbo Boost! (1/2) 33%]  
Optional: [🌟 Extra Points! (2/2) 66%]  
Optional: [🏆 Triple Threat! (2/2) 100%]  

- Crie um novo arquivo chamado `transform-data.yaml` no diretório `.github/workflows/`.
- Use o GitHub Copilot chat com o prefixo `@workspace` para criar uma GitHub Action que transformará os dados sempre que um push ou pull request for feito no repositório.
- Abra um pull request para testar a action. Se ocorrer algum erro, use o GitHub Copilot chat para ajudar a corrigi-lo.

<details>
<summary>Cheatsheet</summary>

#### Prompt

```shell
@workspace Gere uma GitHub Action que transforme os dados a cada push e pull request
```

#### Saída esperada

```markdown
Para criar uma GitHub Action que transforme os dados usando sua CLI, você pode criar um arquivo de workflow no diretório `.github/workflows`. Aqui está um exemplo de um arquivo de workflow do GitHub Actions chamado `transform-data.yml`:

    ```yaml
    // Workflow omitido, já que este é o bônus final!
    ```

Este workflow irá:

* Ser acionado em pushes para a branch principal e em manual dispatch.
* Fazer checkout do repositório.
* Configurar o Python.
* Instalar as dependências necessárias (neste caso, pandas).
* Executar a transformação dos dados usando o comando `run_all` da sua CLI.
* Enviar os dados transformados como artifact.
```

</details>

### Desafio Bônus - Trabalhando com consultas SQL
- Acesse o arquivo  `sql_samples.py` no diretório `workshop`.
- Usando o Copilot Chat, peça para o GitHub Copilot ajudar a construir cada consulta SQL conforme está sendo sugerido.
- No seu terminal execute o arquivo `python3 sql_samples.py` para garantir que as consultas estão corretas e retornando os resultados esperados.

## Limpeza

### 1. Exclua seu Codespace

⏳ **~1min**

Antes de excluir, se desejar, você pode fazer push das suas alterações. Lembre-se de que os repositórios do workshop também são temporários.

Vá para [https://github.com/codespaces](https://github.com/codespaces), encontre o seu Codespace em execução e exclua-o.

## Recursos adicionais

Se você quiser aprender mais sobre como usar o GitHub Copilot, consulte estes recursos:

* [GitHub Copilot Documentation](https://docs.github.com/copilot)
* [VS Code video series: GitHub Copilot](https://www.youtube.com/playlist?list=PLj6YeMhvp2S7rQaCLRrMnzRdkNdKnMVwg)
* [Blog: Best practices for prompting Copilot](http://blog.pamelafox.org/2023/06/best-practices-for-prompting-github.html)

Consulte também a [trilha de aprendizado GitHub Foundations](https://learn.microsoft.com/training/paths/github-foundations/) para mais recursos sobre GitHub e GitHub Copilot.