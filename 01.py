#  1 -Escreva um programa que imprima "Olá, nome_do_usuario!" na tela.


# utilizamos o argumento 'def' para iniciarmos uma função, e dentro
# do parênteses podemos passar os parâmetros que essa função pode receber,
# por exemplo, vamos esperar receber um nome, para que ele seja
# exibido ao executar o código abaixo, alterando o parâmetro no 
# momento que a função for executada, a informação será exibida de forma
# diferente.

def printHelloName(name):
    print("Olá",name)

printHelloName("Vitor")