nome = input('Digite seu nome completo: ').strip()
print('Analisando seu nome...')
#mai = nome.upper()
print(f'Seu nome em maiúsculas é {nome.upper()}.')
#min = nome.lower()
print(f'Seu nome em minúsculas é {nome.lower()}.')
nome2 = len(nome)-nome.count(' ')
print(f'Seu nome tem ao todo {nome2} letras.')
nom = nome.split()
print(f'Seu último nome é {nom[1]} e tem {len(nom[1])} letras.')
