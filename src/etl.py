import pandas as pd
 
def carregar_dados():
    caminho_arquivo = "data/BRAZIL_EXP_COMPLETE.csv"
    df = pd.read_csv(caminho_arquivo, sep=";", encoding="latin1")
    
    # Tratamento básico
    df = df.dropna(subset=['NO_PAIS'])  # Remove linhas sem país
    df = df[df['VL_FOB'].notnull()]     # Remove valores nulos em VL_FOB
    df['VL_FOB'] = pd.to_numeric(df['VL_FOB'], errors='coerce')  # Garante tipo numérico
    
    return df
