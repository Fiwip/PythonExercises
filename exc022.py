f = input('Digite seu nome completo: ')
print('Seu nome em maiúsculo é: ', f.upper())
print('Seu nome em minúsculo é: ', f.lower())
f1 = f.replace(' ', '')
print(f1)
print('Seu nome tem', len(f1), 'letras')
f2 = f.split()
print('Seu primeiro nome é', f2[0], 'e tem', len(f2[0]), 'letras.')