# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçoes possivel sobre ele
n = input('Digite algo para saber o tipo primitivo do que foi escrito: ')
print('O tipo primirtivo deste valor é: ', type(n))
print('Ele tem numeros ou letras ? Tru ou False: ',(n.isalnum()))
print('Ele é alfabetico ? Tru ou False:',(n.isalpha()))
print('Ele tem numeros decimais ? Tru ou False: ',n.isdecimal())
print('', n.isdigit())
print('',n.isidentifier())
print('Ele tem espaço ? Tru ou False: ', n.isspace())
print('Ele esta com letra minuscula ? Tru ou False:',n.islower())
print('Ele tem letras maiusculas ? Tru ou False:', n.isupper())
print('Ele está capitalizado ? Tru ou False:',n.istitle())
print('Ele tem acento ? Tru ou False:',n.isprintable())
print('Ele tem numero ? Tru ou False:', n.isnumeric())