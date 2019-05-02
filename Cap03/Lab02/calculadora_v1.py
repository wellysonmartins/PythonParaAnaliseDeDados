# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print("\nSelecione o número da operação desejada")
print("\n1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

while True:
    op = int(input("\nDigite sua opção (1/2/3/4): "))
    
    if op < 1 or op > 4:
        print("\nOpção inválida!\n\n\n")
        break

    num_01 = int(input("\nDigite o primeiro número: "))
    num_02 = int(input("\nDigite o segundo número: "))

    def soma(num_01, num_02):
        print("\n{} + {} = {}\n\n\n".format(num_01, num_02, num_01+num_02))
        return

    def subtracao(num_01, num_02):
        print("\n{} - {} = {}\n\n\n".format(num_01, num_02, num_01-num_02))
        return

    def multiplicacao(num_01, num_02):
        print("\n{} * {} = {}\n\n\n".format(num_01, num_02, num_01*num_02))
        return

    def divisao(num_01, num_02):
        print("\n{} / {} = {:.1f}\n\n\n".format(num_01, num_02, float(num_01/num_02)))
        return

    if op == 1: soma(num_01, num_02)
    elif op == 2: subtracao(num_01, num_02)
    elif op == 3: multiplicacao(num_01, num_02)
    else: divisao(num_01, num_02)
    
    break
    