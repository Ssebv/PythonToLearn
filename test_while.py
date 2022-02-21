
respuesta= None

while respuesta != 'A' and respuesta != 'B' and respuesta != 'C':
    respuesta= input('Que opcion prefieres [A, B, C] ? :  ').capitalize()

if respuesta == 'A':
    print('Elegiste bien')
    
elif respuesta == 'B':
    print('Podrias haber elegido mejor ')

elif respuesta == 'A':
    print('Elegiste mal')

else:
    print('No me has dado una respuesta con sentido ')


numero = 12

while numero > 1 :
    print('Mi numero {} es mayor que 1'.format(numero))
    numero -=1