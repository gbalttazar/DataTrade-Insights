import pandas as pd

def carregar_dados():
    caminho_arquivo = "data/BRAZIL_EXP_CLEAN.csv"
    
    # Carregar os dados
    df = pd.read_csv(caminho_arquivo, sep=";", encoding="latin1")
    
    # Excluir linhas onde 'CO_PAIS' ou 'VL_FOB' são nulos
    df = df.dropna(subset=['CO_PAIS', 'VL_FOB'])
    
    # Garantir que 'VL_FOB' seja numérico, forçando a conversão e tratando valores inválidos como NaN
    df['VL_FOB'] = pd.to_numeric(df['VL_FOB'], errors='coerce')
    
    # Remover linhas com valores inválidos ou NaN após conversão
    df = df.dropna(subset=['VL_FOB'])
    
    # Garantir que o tipo da coluna 'CO_ANO' seja inteiro
    df['CO_ANO'] = df['CO_ANO'].astype(int)
    
    return df
