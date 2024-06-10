def calcular_media_ponderada(nota1, peso1, nota2, peso2):
    #calcular média ponderada
    media = (nota1 * peso1 * nota2 * peso2) / (peso1 + peso2)
    return media
nota1 = float(input('Digite a primeira nota:'))
peso1 = float(input('Digite o peso da primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
peso2 = float(input('Digite o peso da segunda nota:'))

media = calcular_media_ponderada(nota1, peso1, nota2, peso2)
print('A media ponderada é: ', media)
