#Função sem parametro que recebe/solicita o valor de 'n'
def lernotas():
    n=float(input("Digite um nota para o aluno: "))
    return n

#Contém como parametro n1 e n2. Imprimi valor da n1 e n2, calcular a media e retorna o print com a verificação de aprovado ou não aprovado
def resultado(n1, n2):
    media = (n1+n2)/2
    print("Nota 1: ", n1)
    print("Nota 2: ", n2)
    print ("Media: ", media, "Resultado: ", end="")
    if media >= 7:
        print("Aprovado")
    else: 
        print("Reprovado")

#Chamada da função. Ela é chamada duas vezes. 
#Quando chamada ela solicita que ao usuario insira uma nota, e o valor será armazenado nas variaveis.
a = lernotas()
b = lernotas()

#Chamando a função resultado. Após a função lernotas ser executada, os resultados  de 'a' e 'b' são passados como parâmetro para n1 e n2
resultado(a,b)

#Parametro é o valor que a função espera recebe quando é chamada, permitindo que ela passe essas informações para processamento dentro do bloco
#funções permitem a separação do programa em blocos, facilitando, assim, o desenvolvimento de programações mais robustas.