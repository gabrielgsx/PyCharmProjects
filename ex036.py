from math import trunc
vcasa = float(input('Valor da casa: R$'))
scomprador = float(input('Salário do comprador: R$'))
financiamento = int(input('Quantos anos de financiamento? '))
#CONVERTE O ANO EM DIAS
conversão = financiamento * 12
#CALCULA O VALOR DO FINANCIAMENTO E A PORCENTAGEM DO SALÁRIO
financiamento1 = (vcasa/conversão)
porcentagemsalário = (scomprador * 30)/100
print(f'Para pagar a uma casa de R${vcasa:.2f} em {trunc(financiamento)} anos a prestação será de R${financiamento1:.2f}')
if financiamento1 >= porcentagemsalário:
    print('\033[1;31mEmpréstimo NEGADO!')
else:
    print('\033[1;32mEmpréstimo CONCEDIDO!')