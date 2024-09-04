import json

def ler_json(caminho_arquivo):

    """
    Lê dados de um arquivo JSON e os retorna como um dicionário ou lista.
    
    :parametro caminho_arquivo: Caminho para o arquivo JSON.
    :return: Dados carregados do JSON (pode ser um dicionário ou lista).
    """

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        return dados
    
    except FileNotFoundError:
        print(f"Erro: O arquivo {caminho_arquivo} não foi encontrado.")

    except json.JSONDecodeError:
        print(f"Erro: O arquivo {caminho_arquivo} não contém um JSON válido.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

caminho = "dados.json"
faturamento = ler_json(caminho)

menorValor = min(item["valor"] for item in faturamento)
maiorValor = max(item["valor"] for item in faturamento)
numDiaSuperior = numDiaSemFaturamento = 0

# Verifica quantos dias não possui faturamento
for item in faturamento:

    if(item["valor"] == 0):
        numDiaSemFaturamento += 1

# Calcula a média mensal
mediaMensal = sum(item["valor"] for item in faturamento) / (len(faturamento)-numDiaSemFaturamento)

# Verifica quantos dias tiveram um valor maior que a media
for item in faturamento:

    if(item["valor"] > mediaMensal):
        numDiaSuperior += 1

print(f"\nO menor valor de faturamento ocorrido em um dia do mês foi R${menorValor:.2f}")
print(f"O maior valor de faturamento ocorrido em um dia do mês foi de R${maiorValor:.2f}")
print(f"{numDiaSuperior} dias no mês tiveram o valor maior que a média mensal que é R${mediaMensal:.2f}")