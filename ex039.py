from time import sleep
from datetime import date
print('DIGITE [ 1 ] SE SEU SEXO FOR MASCULINO e [ 2 ] SE FOR FEMININO')
sexo = int(input('Qual o seu sexo? '))
print('Digite um valor entre 1 e 2')
nascimento = int(input('\033[2;31mAno de nascimento: \033[m'))
print('Processando...')
sleep(2)
#CALCULOS
anoatual = date.today().year
idade = date.today().year - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {anoatual}')
if sexo == 1:
    if idade > 18:
        print(f'Você já deveria ter se alistado há {idade - 18} ano(s).')
        print(f'Seu alistamento foi em {nascimento + 18}')
    elif idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE')
    else:
        print(f'Ainda faltam {18 - idade} anos para o alistamento')
        print(f'Seu alistamento será em {nascimento + 18}')
else:
        print('Pessoas do sexo feminino não precisam')
        print('obrigatoriamente se alister, para mais informações acesse eb.com.br')











