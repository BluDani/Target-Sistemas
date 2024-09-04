faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcula o faturamento total
faturamento_total = sum(faturamento.values())

# Calcula o percentual de representação de cada estado
percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento.items()}

# Exibe os percentuais
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")