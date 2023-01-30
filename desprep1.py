# em "http://turing.com.br/material/appy/cap4.html"
# desprep1.py - calculo de despesas da republica
# Com atualização de escrita...

print('Balanco de despesas da Republica Recanto Suico')
print("")  # para criar uma linha em branco
print('Deixe um nome em branco para encerrar')
print("")
total = 0
contas = {}
while True:
    pessoa = input('Digite o nome da pessoa: ')
    if not pessoa:
        break
    while True:
        resp = input('Quanto gastou %s? ' % pessoa)
        try:
            gasto = float(resp)
            break
        except:
            print('Numero invalido.')
    contas[pessoa] = gasto
    total = total + gasto

num_pessoas = len(contas)
print
print(f'Numero de pessoas: {num_pessoas}')
print(f'Total de gastos: R$ {total:.2f}')
media = total/num_pessoas
print(f'Gastos por pessoa: R$ {media:.2f}')
print
for nome in contas.keys():
    saldo = contas[nome] - media
    print(f'Saldo de {nome}: {saldo:.2f}')
