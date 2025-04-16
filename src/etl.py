import pandas as pd

def carregar_dados(caminho_exp, caminho_pais):
    df_exp = pd.read_csv(caminho_exp)
    df_pais = pd.read_csv(caminho_pais)

    df_exp = df_exp.dropna(subset=['NO_PAIS'])
    return df_exp, df_pais
