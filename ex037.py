n1 = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
#FÓRMULAS
binário = bin(n1)
octal = oct(n1)
hexadecimal = hex(n1)
n2 = int(input('Sua opção: '))
if n2 == 1:
    print(f'{n1} convertido para BINÁRIO é igual a {binário[2:]}')
elif n2 == 2:
    print(f'{n1} convertido para OCTAL é igual a {octal[2:]}')
elif n2 == 3:
    print(f'{n1} convertido para HEXADECIMAL é igual {hexadecimal[2:]}')
else:
    print('Opção inválida, tente novamente')











