#Perceba novamente que no Python não há {}, e sim Indentações
idade = int(input("Digite Sua Idade: "))

if idade>=18:
    print("Entrada Permitida")
elif idade >= 16:
    print("Entrada Permitida Apenas com Responsável")
else:
    print("Entrada Negada")
    