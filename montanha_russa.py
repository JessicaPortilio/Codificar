print('Bem-vindo à montanha-russa!')

altura = int(input('Qual é a sua altura em cm? '))

conta = 0
if altura >= 120:
    print('Você pode andar na montanha-russa!')
    idade = int(input('Qual é a sua idade? '))
    if idade < 12:
        conta += 25
        print('Ingressos infantis são R$ 25.')
    elif idade <= 18:
        conta += 35
        print('Ingressos para jovens são R$ 35.')
    elif idade >= 45 and idade <= 55:
        print('Everything is going to be ok. Have a free ride on us!')
    else:
        conta += 60
        print('Ingressos para adultos são R$ 60.')
    
    quer_foto = input('Você quer uma foto? S ou N ')
    if quer_foto == 'S' or quer_foto == 's':
        conta += 15
        print(conta)
    
    print(f'Seu valor final é R$ {conta}')
else:
    print('Desculpe, você precisa crescer mais antes de andar na montanha-russa.')
