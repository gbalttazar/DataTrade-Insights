def limpar_csv_quebrado(caminho_original, caminho_saida):
    with open(caminho_original, 'r', encoding='latin1') as arquivo_in:
        linhas_validas = []
        for i, linha in enumerate(arquivo_in):
            # Verifica se há número ímpar de aspas → pode indicar quebra de linha incorreta
            if linha.count('"') % 2 == 0:
                linhas_validas.append(linha)
            else:
                print(f"⚠️ Linha {i + 1} ignorada (aspas quebradas): {linha[:100]}")

    with open(caminho_saida, 'w', encoding='latin1') as arquivo_out:
        arquivo_out.writelines(linhas_validas)
        print(f"\n✅ CSV limpo salvo em: {caminho_saida}")


if __name__ == "__main__":
    limpar_csv_quebrado("data/BRAZIL_EXP_COMPLETE.csv", "data/BRAZIL_EXP_CLEAN.csv")
