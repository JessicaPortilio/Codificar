# Se a conta for de R$ 150,00, divida entre 5 pessoas, com gorjeta de 12%.
# Cada pessoa deverá pagar (150,00 / 5) * 1,12 = 33,6
# Formate o resultado com 2 casas decimais = 33,60
# Dica: Existem 2 maneiras de contornar um bumber. 
# Talvez você precise pesquisar no Google para resolver isso.
#Escreva seu código abaixo desta linha

print('Bem-vindo à calculadora de gorjetas!')
conta_total = float(input('Qual foi a conta total? R$'))
gorjeta = int(input('Quanta gorjeta você gostaria de dar? 10, 12 ou 15?'))
pessoas_dividir = int(input('Quantas pessoas para dividir a conta?'))
total = (conta_total / pessoas_dividir) * (gorjeta / 100 + 1) 
print(f'Cada pessoa deverá pagar: R${round(total,2)}')