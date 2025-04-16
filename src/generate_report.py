import pandas as pd

def gerar_relatorio(df, caminho_saida="relatorio.md"):
    with open(caminho_saida, "w", encoding="utf-8") as f:
        f.write("# 📄 Relatório de Exportações Brasileiras (1996-2023)\n\n")

        # Total de registros
        total_registros = len(df)
        f.write(f"- Total de registros analisados: **{total_registros:,}**\n")

        # Período da análise
        anos = df["CO_ANO"].unique()
        f.write(f"- Período coberto: **{anos.min()} - {anos.max()}**\n")

        # Top 5 países
        top_paises = df.groupby("NO_PAIS")["VL_FOB"].sum().sort_values(ascending=False).head(5)
        f.write("\n## 🌍 Top 5 Países Importadores:\n")
        for pais, valor in top_paises.items():
            f.write(f"- {pais}: US${valor:,.2f}\n")

        # Valor total exportado
        valor_total = df["VL_FOB"].sum()
        f.write(f"\n## 💰 Valor Total Exportado:\n- US$ {valor_total:,.2f}\n")

        # Valor médio por ano
        media_anual = df.groupby("CO_ANO")["VL_FOB"].sum().mean()
        f.write(f"\n## 📈 Valor Médio Anual Exportado:\n- US$ {media_anual:,.2f}\n")

        f.write("\n---\nRelatório gerado automaticamente por `generate_report.py`\n")

