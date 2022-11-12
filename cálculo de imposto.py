# Faça um programa em Python com uma função chamada soma_imposto. A função possui dois parâmetros formais:
# a) taxa_imposto, que é a quantia de imposto sobre vendas expressa em porcentagem; e
# b) custo, que é o custo de um item antes do imposto. A função altera o valor de custo para incluir o imposto sobre vendas.
# O programa principal deve pedir os dados e usar a função para calcular preço do produto

def soma_imposto(taxa_imposto, custo):
    return (1 + taxa_imposto/100)*custo

print("Informe os Dados a Seguir para Gerar o Imposto sobre o Valor da Venda...")
taxa_imposto = float(input("Digite a taxa de imposto: "))
custo = float(input("Digite o custo: "))
print("-----------------------------------------------------")
print("Valor com imposto:", soma_imposto(taxa_imposto,custo))
print("-----------------------------------------------------")