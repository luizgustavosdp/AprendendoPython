#Manipular dodos em um arquivo de texto mostrando operações da escrita e leitura.
#Esse arquivo texto é conhecido como arquivo sequencial, porque a leitura tem de ser feita de forma sequencial, do início ao fim do arquivo.

#Função Open utilizada para abrir ou criar arquivo. Usamos o 'w' para indidicar que vamos fazer um gravação
#Atenção, ao criar o arquivo e caso esse arquivo já exista, o Python irá apago e reescrelo por cima.
arquivo = open('arqText.txt', 'w')
#Utilizado para escrever desntro do documento.txt
arquivo.write("Curso de Python \n")
arquivo.write("Aula Linguagem de Programação")
#Utilizado para fechar o documento.txt
arquivo.close()


#Leitura do Texto
leitura = open("arqText.txt", 'r')
print(leitura.read())
leitura.close()

#Outros modos

#r = usado apenas para ler arquivos já existentes
#r+ = abre arquivos existentes para leitura e escrita. Caso tenha algo será apagado e reescrito
#w =  abre ou criar arquivos text apenas para escrita
#w+ = abre o arquivo para leitura e escrita, apagando o conteúdo existente
#a = abre para escrita no final do arquivo. Não apaga conteúdos existentes
#a+ = abre arquivo para escrita no final do arquilo e leitura