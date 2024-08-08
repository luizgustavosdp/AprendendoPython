#Criamos aqui uma estrutura de repetição utilizando o for. Range é utilizado para gerar uma sequencia de numeros inteiros para ser usados em loops e iterações
#No Python 'n' já é iniciada com o valor padrão 0. Enquanto n for menor que 10, o comando print é executado
for n in range (10):
    print(n)

#O Padrão o valor é iniciado a 0 e para alterar se alterar dentro do 'range'
#Nesse caso n já irá iniciar com 5 e irá imprimir apenas os 5 restantes
for n in range (5, 10):
    print(n)

#Desse maneira é imprimido de forma decrescente
for n in range (10, 0, -1):
    print(n)
