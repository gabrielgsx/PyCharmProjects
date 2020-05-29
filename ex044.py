n1 = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão ')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opção = int(input('Qual é a opção? '))
#OPÇÕES 1,2 e 3
if opção == 1:
    print(f'Sua compra de R${n1:.2f} vai custar R${(n1 - (n1 * 10)/100):.2f} no final.')
elif opção == 2:
    print(f'Sua compra de R${n1:.2f} vai custar R${(n1 - (n1 * 5) / 100):.2f} no final.')
elif opção == 3:
    print(f'Sua compra será parcelada em 2x de R${n1/2:.2f}')
    print(f'Sua compra será de {n1} vai custar {n1} no final')
elif opção == 4:
    parcelas = float(input('Quantas parcelas?'))
    valor = n1 / parcelas
    juros = (valor * 20 / 100)
    print(f'Sua compra será parcelada em {parcelas:.0f}x de R${valor + juros:.2f} COM JUROS.')
    print(f'SUA COMPRA DE R${n1:.2f} vai custar {n1 + (n1 * 20 / 100):.2f} no final')
else:
    print('OPÇÂO INVÁLIDA')



'''#OPÇÃO 4
if opção == 4:
    parcelas = float(input('Quantas parcelas?' ))
    valor = n1 / parcelas
    juros = (valor * 20 / 100)
    if parcelas >= 3:
        print(f'Sua compra será parcelada em {parcelas:.0f}x de R${valor + juros:.2f} COM JUROS.')
        print(f'SUA COMPRA DE R${n1:.2f} vai custar {n1 + (n1 * 20/100):.2f}')'''
















