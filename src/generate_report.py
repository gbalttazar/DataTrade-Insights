from etl import carregar_dados

print("🚀 Iniciando script...")
python

def gerar_relatorio():
    df = carregar_dados()

    # Período analisado
    ano_inicio = int(df['CO_ANO'].min())
    ano_fim = int(df['CO_ANO'].max())

    # Valor total exportado
    total_exportado = df['VL_FOB'].sum()

    # Top países importadores
    top_paises = df.groupby('NO_PAIS')['VL_FOB'].sum().sort_values(ascending=False).head(5)

    # Valor médio anual
    media_anual = df.groupby('CO_ANO')['VL_FOB'].sum().mean()

    with open("relatorio_exportacoes.md", "w", encoding="utf-8") as f:
        f.write("# Relatório de Exportações do Brasil\n\n")
        f.write(f"**Período Analisado:** {ano_inicio} - {ano_fim}\n")
        f.write(f"**Valor Total Exportado:** R$ {total_exportado:,.2f}\n")
        f.write(f"**Valor Médio Anual:** R$ {media_anual:,.2f}\n\n")
        f.write("## Top 5 Países Importadores:\n")
        for pais, valor in top_paises.items():
            f.write(f"- {pais}: R$ {valor:,.2f}\n")

    print("✅ Relatório gerado com sucesso em 'relatorio_exportacoes.md'")