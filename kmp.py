
def calcular_lps(padrao):
    lps = [0] * len(padrao)
    k = 0

    for i in range(1, len(padrao)):
        while k > 0 and padrao[i] != padrao[k]:
            k = lps[k - 1]

        if padrao[i] == padrao[k]:
            k += 1

        lps[i] = k

    return lps


def kmp(texto, padrao):
    if not padrao:
        raise ValueError("O padrão não pode ser vazio")

    lps = calcular_lps(padrao)
    ocorrencias = []
    k = 0

    for i in range(len(texto)):
        while k > 0 and texto[i] != padrao[k]:
            k = lps[k - 1]

        if texto[i] == padrao[k]:
            k += 1

        if k == len(padrao):
            ocorrencias.append(i - len(padrao) + 1)
            k = lps[k - 1]

    return ocorrencias


# Exemplo de busca
texto = "ABABDABACDABABCABAB"
padrao = "ABABCABAB"

resultado = kmp(texto, padrao)

print("Texto:", texto)
print("Padrão:", padrao)
print("Ocorrências encontradas:", resultado)

# Teste do resultado
assert resultado == [10]
print("Teste aprovado!")

# Teste de sobreposição
assert kmp("AAA", "AA") == [0, 1]
print("Teste de sobreposição aprovado!")
