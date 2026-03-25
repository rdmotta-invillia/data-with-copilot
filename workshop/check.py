import pandas as pd


def verify_drop_notes(df):
    """
    Verifica se a coluna 'notes' foi removida.
    """
    return 'notes' not in df.columns

def verify_high_ratings(df):
    """
    Verifica se todos os ratings são 90 ou maiores.
    """
    if 'rating' in df.columns:
        return df['rating'].min() >= 90
    return False

def verify_one_hot_encoding(df):
    """
    Verifica se a coluna 'Red_Wine' recebeu one-hot encoding.
    """
    return 'Red_Wine' in df.columns and df['Red_Wine'].isin([0, 1]).all()

def verify_remove_newlines_carriage_returns(df):
    """
    Verifica se não há newlines ou caracteres de retorno nas colunas de texto.
    """
    for col in df.select_dtypes(include=['object']).columns:
        if df[col].str.contains('\n').any() or df[col].str.contains('\r').any():
            return False
    return True

def verify_ratings_to_int(df):
    """
    Verifica se a coluna 'rating' foi convertida para integer.
    """
    if 'rating' in df.columns:
        return pd.api.types.is_integer_dtype(df['rating'])
    return False

# Exemplo de uso
if __name__ == "__main__":
    df = pd.read_csv('transformed_train.csv')
    functions = [
        [verify_drop_notes, "A coluna 'notes' não foi removida corretamente."],
        [verify_high_ratings, "Nem todos os ratings são 90 ou maiores."],
        [verify_one_hot_encoding, "A coluna 'Red_Wine' não recebeu one-hot encoding corretamente."],
        [verify_remove_newlines_carriage_returns, "Newlines ou caracteres de retorno não foram removidos corretamente."],
        [verify_ratings_to_int, "A coluna 'rating' não foi convertida para integer corretamente."]
    ]
     
    for func, message in functions:
        if func(df):
            print(f"[OK  ]\t {str(func.__name__)}")
        else:
            print(f"[FAIL]\t {str(func.__name__)} - {message}")
