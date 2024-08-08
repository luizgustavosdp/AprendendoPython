#Nesse codigo temos como exemplo a bela funcioanalide do python de detectar os tipos de variaveis.

codigo = 10
salario = 1500.00
nome = "Luiz"
situacao = True

tipo = type(salario)

print(salario)
print(tipo, "\n")

#Usamos acima um print para cada informação. Para exibir varias com um comando print print usamos virgulas. (Concatenar/Unir varias informações)
print("Codigo: ", codigo, "Nome: ", nome,"salario atual é de: ",salario)
#Também Podemos utilizar o sinal (+) para concatenar, porém temos converte tipos não string para strings. Para isso usamos str.
print("Codigo: "+ str(codigo)+ " Nome: "+ nome, "salario atual é: "+ str(salario), "\n")

