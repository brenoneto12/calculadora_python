print("="*70)
print(" "*25 + " Calculadora Python " + " "*25)
print("="*70)
print("\n")
print("Selecione o número da operação desejada!")
print("\n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Exponênciação - '1º Digite o número que deseja calcular | 2º Digite o expoênte ' ")
print("6 - Raiz - '1º Digite o número que deseja calcular | 2º Tipo Raiz (Ex: 2 é raiz quadrada, 3 é raiz cúbica)' ")
print("\n")

lista_operacoes = [1,2,3,4,5,6]

operacao = int(input(print("Digite o número da operação desejada!")))

while operacao not in lista_operacoes:
    operacao = int(input(print("Digite um número de operação válido!")))

num1 = float(input(print("Digite o primeiro número :")))

num2 = float(input(print("Digite o segundo número :")))

if operacao == 1:
    print(f'A soma dos números {num1:.2f} e {num2:.2f} é igual a: {num1 + num2:.2f}!')
elif operacao == 2:
    print(f'A subtração dos números {num1:.2f} e {num2:.2f} é igual a: {num1 - num2:.2f}!')
elif operacao == 3:
    print(f'A multiplicação dos números {num1:.2f} e {num2:.2f} é igual a: {num1 * num2:.2f}!')
elif operacao == 4:
    print(f'A divisão dos números {num1:.2f} e {num2:.2f} é igual a: {num1 / num2:.2f}!')
elif operacao == 5:
    print(f'A exponênciação dos números {num1:.2f} e {num2:.2f} é igual a: {num1 ** num2:.2f}!')
else:
    print(f'A Raiz dos números {num1:.2f} e {num2:.2f} é igual a: {num1 ** (1/num2):.2f}!')

print("\n")
print("="*70)
print(" "*25 + " By Breno Teodomiro " + " "*25)
print("="*70)
print("\n")
print('Saindo...')
print("\n")
exit()

#print("Deseja fazer outra operação?")

#print("\n")
#print("1 - Sim")
#print("Caso contrário digite qualquer tecla")
#print("\n")

#operacao = int(input(print("Deseja fazer outra operação?")))

#if operacao == 1:
#    operacao = int(input(print("Digite um número de operação válido!")))
#else:
#    print('Saindo...')
#    exit()