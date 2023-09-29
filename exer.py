sinonimos= {'Problema':'Impedimento',
            'Verdadeiro':'Genuino',
            'Importante':'Vultoso',
            'Alegria':'Felicidade',
            'Tranquilo':'Calmo',
            'Rapido':'Veloz',
            'Dificil':'Arduo',
            'Gostoso':'Delicioso',
            'Certo':'Correto',
            'Bonito':'Belo',
            'Baixo':'Pequeno',
            'Corajoso':'Valente',
            'Indispensavel':'Necessario',
            'Cheio':'Lotado'}

print('Descubra o sinonimos das palavras :')
pergunta= input('Digite uma palavra')


if pergunta in sinonimos:
    print(sinonimos[pergunta])
else:
    print('Não temos essa palavra')