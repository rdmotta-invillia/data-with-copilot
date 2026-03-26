import sqlite3
import pandas as pd


def run_sql_examples(df: pd.DataFrame) -> None:
    """
    Executa exemplos de consultas SQL usando SQLite em memoria.
    """
    conn = sqlite3.connect(":memory:")
    try:
        df.to_sql("wines", conn, index=False, if_exists="replace")

        select_top_10_wines_by_rating(conn)

        


    finally:
        conn.close()


def select_top_10_wines_by_rating(conn: sqlite3.Connection) -> None:
    """
    Monte uma consulta SQL que traga os top 10 vinhos por rating, mostrando as colunas name, region, rating e Red_Wine.
        - Ordene por rating desc e name asc.
    """
        
    query_top_10 = """
    """

    if not query_top_10.strip():
        print("Consulta SQL para top 10 vinhos por rating não foi implementada.")
        return
    
    top_10 = pd.read_sql_query(query_top_10, conn)
    print("\nTop 10 vinhos por rating:")
    print(top_10.to_string(index=False)) 


def select_wines_with_high_rating_and_red_wine(conn: sqlite3.Connection) -> None:
    """
    Monte uma consulta SQL que traga os vinhos com rating 95 ou maior e que sejam Red Wine, mostrando as colunas name, region, rating e Red_Wine.
        - Ordene por rating desc e name asc.
    """
        
    query_high_rating_red_wine = """
    """

    if not query_high_rating_red_wine.strip():
        print("Consulta SQL para vinhos com rating 95 ou maior e que sejam Red Wine não foi implementada.")
        return
    
    high_rating_red_wine = pd.read_sql_query(query_high_rating_red_wine, conn)
    print("\nVinhos com rating 95 ou maior e que sejam Red Wine:")
    print(high_rating_red_wine.to_string(index=False))

def select_average_rating_by_region(conn: sqlite3.Connection) -> None:
    """
    Monte uma consulta SQL que traga a média de rating por região, mostrando as colunas region e average_rating.
        - Ordene por average_rating desc e region asc.
    """
        
    query_average_rating_by_region = """
    """

    if not query_average_rating_by_region.strip():
        print("Consulta SQL para média de rating por região não foi implementada.")
        return
    
    average_rating_by_region = pd.read_sql_query(query_average_rating_by_region, conn)
    print("\nMédia de rating por região:")
    print(average_rating_by_region.to_string(index=False))

if __name__ == "__main__":
    data = pd.read_csv("transformed_train.csv")
    run_sql_examples(data)
