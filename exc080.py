lista = list()
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > lista[len(lista)-1]:
        lista.append(valor)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f'Adicionado na posição {pos}...')
                break
            pos += 1
print('=-' * 30)
print(f'Os números digitados em ordem crescente foram: {lista}')
