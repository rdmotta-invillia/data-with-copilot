import pandas as pd


def drop_notes(df):
    """
    Remove a coluna 'notes' do DataFrame.
    """
    if 'notes' in df.columns:
        df = df.drop(columns=['notes'])
    return df


def select_high_ratings(df):
    """
    Seleciona apenas as linhas em que a coluna 'ratings' é 90 ou maior.
    """
    if 'ratings' in df.columns:
        df = df[df['ratings'] >= 90]
    return df


def drop_and_one_hot_encode_red_wine(df):
    """
    Cria a coluna 'Red_Wine' com valor 1 quando 'variety' é 'Red Wine' e 0 nos demais casos.
    Remove a coluna original 'variety'.
    """
    if 'variety' in df.columns:
        df = pd.get_dummies(df, columns=['variety'], prefix='Red Wine', drop_first=True)
    return df


def remove_newlines_carriage_returns(df):
    """
    Remove newlines e caracteres de retorno de todas as colunas de texto do DataFrame.
    """
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.replace('\n', ' ').str.replace('\r', ' ')
    return df


def convert_ratings_to_int(df):
    """
    Converte a coluna 'ratings' de float para integer.
    """
    if 'ratings' in df.columns:
        df['ratings'] = df['ratings'].to_bool()
    return df

# Exemplo de uso
if __name__ == "__main__":
    df = pd.read_csv('train.csv')
    df = drop_notes(df)
    df = select_high_ratings(df)
    df = drop_and_one_hot_encode_red_wine(df)
    df = remove_newlines_carriage_returns(df)
    df = convert_ratings_to_int(df)
    df.to_csv('transformed_train.csv', index=False)