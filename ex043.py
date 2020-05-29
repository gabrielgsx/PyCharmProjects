peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m)'))
IMC = (peso / (altura**2))
print(f'O IMC dessa pessoa é de {IMC:.1f}')
if IMC < 18.5:
    print('Você está abaixo do PESO normal')
elif IMC >= 18.5 and IMC <= 24.9:
    print('Você está com o PESO NORMAL')
elif IMC >= 25 and IMC <= 29.9:
    print('Você está em SOBREPESO')
elif IMC >= 30 and IMC <= 39.9:
    print('Você está em OBESIDADE')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado')
