def calcular_btus(area, pessoas, equipamentos, insolacao):
    # Definindo o fator de insolação baseado na entrada
    if insolacao == 'direta':
        fator_insolacao = 800
        btus = (area * fator_insolacao) + (pessoas * fator_insolacao) + (equipamentos * fator_insolacao) + fator_insolacao
        return btus
    else:
        fator_insolacao = 600
        btus = (area * fator_insolacao) + (pessoas * fator_insolacao) + (equipamentos * fator_insolacao) + fator_insolacao
        return btus

def calcular_numero_ar_condicionado(capacidade_total_necessaria, capacidade_ar_condicionado):
    # Calculando o número de unidades de ar condicionado necessárias
    return capacidade_total_necessaria / capacidade_ar_condicionado

def calcular_area(largura, comprimento):
    # Calculando a área do ambiente
    return largura * comprimento

# Obtendo os dados do ambiente
opcao_area = input("Você quer fornecer a área do ambiente (A) ou as dimensões (largura e comprimento) (D)? ").lower()

if opcao_area == 'a':
    area = float(input("Informe a área do ambiente em metros quadrados: "))
else:
    largura = float(input("Informe a largura do ambiente em metros: "))
    comprimento = float(input("Informe o comprimento do ambiente em metros: "))
    area = calcular_area(largura, comprimento)

# Obtendo o número de pessoas e equipamentos no ambiente
pessoas = int(input("Informe o número de pessoas no ambiente: "))
equipamentos = int(input("Informe o número de equipamentos no ambiente: "))

# Obtendo a informação sobre a insolação do ambiente
insolacao = input("A insolação é direta ou indireta? ").lower()

# Capacidades disponíveis dos aparelhos de ar condicionado
capacidades_ar_condicionado = [9000, 12000, 18000, 24000, 30000, 32000, 36000]

# Calculando a capacidade total necessária em BTUs
capacidade_total_necessaria = calcular_btus(area, pessoas, equipamentos, insolacao)

# Exibindo a capacidade total necessária
print("A capacidade de refrigeração necessária é de aproximadamente", capacidade_total_necessaria, "BTUs.")

# Calculando quantos aparelhos de ar condicionado são necessários para cada capacidade disponível
for capacidade_ar_condicionado in capacidades_ar_condicionado:
    numero_ar_condicionado = calcular_numero_ar_condicionado(capacidade_total_necessaria, capacidade_ar_condicionado)
    numero_ar_condicionado_arredondado = round(numero_ar_condicionado)
    print("Serão necessários aproximadamente", numero_ar_condicionado_arredondado, "aparelhos de ar condicionado de", capacidade_ar_condicionado, "BTUs.")

