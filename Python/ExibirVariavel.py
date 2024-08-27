codigo = 105
salario = 1500.00
name = "Luiz Gustavo"
active= True

#Nesse exmplos utilizamos identificadores para representar cada tipo de dado
print("Código é : %d"% codigo)
print("Nome: %s" %name)
print("Salario: %.2f" %salario)
print("Active: %d \n" %active)

#Para entrada de dados tipo strings utilizamos o input. Peceba que já declaramos a fruta no codigo, e o input grava a entrada do dado e já exibi uma mensagem
fruta = input("Digite o nome da fruta:")
print("Resposta: ",fruta,"\n")

#Quando a entrada é de dados de valores numericos/não Strings, nesse caso temos que converto-los.
codigo = int(input("Digite o codigo: "))
nome = input("Digite o nome do funcionario: ")
salario = float(input("Infome o salario: "))

print("Codigo: %d"%codigo)
print("Nome: %s" %nome) 
print("Salario: %.2f"% salario)
print("Ativo: %r" %active)