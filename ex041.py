from datetime import date
nasc = int(input('Ano de nascimento: '))
idade =  date.today().year - nasc
print(f'O atleta tem {idade} anos')
if idade <= 9:
    classe = 'MIRIM'
elif idade > 9 and idade <= 14:
    classe = 'INFANTIL'
elif idade > 14 and idade <= 19:
    classe = 'JUNIOR'
elif idade > 19 and idade <= 25:
    classe = 'SÊNIOR'
else:
    classe = 'MASTER'
print(f'Classificação: {classe}')



