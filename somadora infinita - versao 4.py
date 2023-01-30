# em "http://turing.com.br/material/appy/cap4.html"
# somadora4.py - somadora infinita - versao 4
# Com atualização de escrita...

print("Somadora Infinita")
print("")  # para criar uma linha em branco
print('Digite os valores a somar seguidos de ENTER')
print('Para encerrar apenas ENTER')
print("")
total = 0
while True:
    try:
        linha = input(':')
        n = float(linha)
        total = total + n
    except:
        if len(linha) == 0:
            break
        elif ',' in linha:
            print('Use o . (ponto) como separador decimal.')
        else:
            print('Isso nao parece um numero valido.')
print("")
print(f'TOTAL: {total}')
