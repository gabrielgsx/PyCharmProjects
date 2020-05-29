pnota = float(input('Primeira nota: '))
snota = float(input('Segunda nota: '))
média = (pnota + snota)/2
print(f'Tirando {pnota:.1f} e {snota:.1f}, a média do aluno é {média:.1f}')
if média >= 7.0 and média <= 10:
    print('O alino foi APROVADO')
elif média < 5.0:
    print('O aluno foi REPROVADO')
elif média >= 5 and média <=6.9:
    print('O aluno está de recuperação')
