# em "http://turing.com.br/material/appy/cap3.html"
# despdom3.py - Calculadora de despesas domesticas - versao 3
# Com atualização de escrita...

print('Balanco de despesas domesticas')
ana = float(input('Quanto gastou Ana? '))
bia = float(input('Quanto gastou Bia? '))

print("")  # para criar uma linha em branco
total = ana + bia
print(f'Total de gastos: R$ {total}')
print("")
media = total/2
print(f'Gastos por pessoa: R$ {media}')
if ana < media:
    diferenca = media - ana
    print("")
    print(f'Ana deve pagar: R$ {diferenca}')
elif bia < media:
    diferenca = media - bia
    print("")
    print(f'Bia deve pagar: R$ {diferenca}')
else:
    print("")
    print('Ana e Bia gastaram a mesma Quantia.')
