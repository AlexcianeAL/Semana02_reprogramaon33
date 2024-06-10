#Solicite ao usuário digitar dois números
num1 = int(input('digite o primeiro numero:'))
num2 = int(input('digite o segundo numero:'))

#operações aritméticas
soma = num1+num2
subtracao = num1-num2
mutiblicacao = num1*num2
divisão = num1/num2
divisãointeira = num1//num2
modulo = num1 % num2
potencia = num1**num2

#exibir resultados

print('\n Resultados dos operacoes aritmeticos:')
print('Soma:', soma)
print('Subtracao:', subtracao)
print('Multiplicacao:', mutiblicacao)
print('Divisao:', divisão)
print('Divisaointerira:', divisãointeira)
print('Modulo:', modulo)
print('Potencia:', potencia)

#Comparações com operadores

print('\n Resultados das operações de comparação:')
print('Igualdade:', num1 == num2)
print('Diferenca:', num1 != num2)
print('Maior:', num1 > num2)
print('Maior ou igual:', num1 >= num2)
print('Menor:', num1 < num2)
print('Menor ou igual:', num1 <= num2)

#Verificar presença na lista de elementos
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if num1 in lista_numeros:
    print(f'o número {num1} está na lista de numeros')
else:
    print(f'o número {num1} não está na lista de números')

    # Compare a identidade de objetos
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print('\n Resultados das operações de identidade de objetos:')
print('x is z:', x is z)
print('x is y:', x is y)
print('x is not y:', x is not y)