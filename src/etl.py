import pandas as pd

def carregar_dados():
    caminho_arquivo = "data/BRAZIL_EXP_COMPLETE.csv"
    try:
        df = pd.read_csv(
            caminho_arquivo,
            sep=";",
            encoding="latin1",
            on_bad_lines="skip",
            engine="python",
            dtype=str
        )
        print("✅ Arquivo carregado com sucesso (linhas ruins ignoradas automaticamente).")

        # Conversões e limpezas
        df = df.dropna(subset=['CO_PAIS'])
        df = df[df['VL_FOB'].notnull()]
        df['VL_FOB'] = pd.to_numeric(df['VL_FOB'], errors='coerce')

        return df
    except Exception as e:
        print(f"❌ Erro ao carregar CSV: {e}")
        return pd.DataFrame()
