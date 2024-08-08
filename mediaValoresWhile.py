qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while(valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1
    #Entrada de valores
    valor = float(input("Digite um valor: "))

#Caso seja um numero negativo o laço encerrar
media = soma/qtd
print("\n Toda da soma: ", soma)
print("\n Quantidade de valores digitados: ", qtd)
print("Média dos valores ", media)

#Nesse while enquanto o valor for maior que 0, o comando é executado e continuamos digitados valor. Para parar o loop colocamos um numero negativo
#Soma é igual o valor digitado + valor que eu digitar novamente enquanto eu estiver no loop.
#qtd é o numero de vezes que o loop foi incrementado. E  para que continuar colocando valores, temos um "scanner" dentro do blobo do while.