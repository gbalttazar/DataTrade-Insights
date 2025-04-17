from etl import carregar_dados

print("🚀 Iniciando script...")

def gerar_relatorio():
    df = carregar_dados()

    print("🔍 Dados carregados:")
    print(df.head())  # Exibe as primeiras linhas para verificar o conteúdo
    print(f"📊 Quantidade de linhas: {len(df)}\n")

    if df.empty:
        print("⚠️ DataFrame está vazio. Verifique se o arquivo foi carregado corretamente.")
        return

    # Verifica os valores únicos na coluna 'CO_ANO' para garantir que todos os anos estão presentes
    anos_unicos = df['CO_ANO'].unique()
    print(f"📅 Anos disponíveis: {anos_unicos}")

    # Período analisado
    ano_inicio = int(df['CO_ANO'].min())
    ano_fim = int(df['CO_ANO'].max())
    print(f"📅 Período analisado: {ano_inicio} - {ano_fim}")

    # Valor total exportado
    total_exportado = df['VL_FOB'].sum()

    # Top países importadores
    top_paises = df.groupby('CO_PAIS')['VL_FOB'].sum().sort_values(ascending=False).head(5)

    # Valor médio anual
    media_anual = df.groupby('CO_ANO')['VL_FOB'].sum().mean()

    # Geração do relatório
    try:
        with open("relatorio_exportacoes.md", "w", encoding="utf-8") as f:
            f.write("# Relatório de Exportações do Brasil\n\n")
            f.write(f"**Período Analisado:** {ano_inicio} - {ano_fim}\n")
            f.write(f"**Valor Total Exportado:** R$ {total_exportado:,.2f}\n")
            f.write(f"**Valor Médio Anual:** R$ {media_anual:,.2f}\n\n")
            f.write("## Top 5 Países Importadores:\n")
            for pais, valor in top_paises.items():
                f.write(f"- {pais}: R$ {valor:,.2f}\n")

        print("✅ Relatório gerado com sucesso em 'relatorio_exportacoes.md'")
    except Exception as e:
        print(f"❌ Erro ao gerar o relatório: {e}")

if __name__ == "__main__":
    gerar_relatorio()
