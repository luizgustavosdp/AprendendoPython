#Perceba a indentação que organiza e cria os blocos de comandos em Python (Sem usar {})

A=input("Informe um valor A: ")
B=input("Informe um valor B: ")

#Nesse comando será executado se 'A' for maior 'B'. Nesse caso aux atribui valor de A, A atribui valor de B, e B atribui valor de aux (Antigo valor de A)
if(A>B):
    aux = A
    A=B
    B=aux
print("O valor de A agora é: ", A);
print("O valor de A agora é: ", B);
