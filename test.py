from cgitb import reset
from pdb import Restart
from tracemalloc import stop


print('')
print('Bienvenidos!!')
print('''
Este es un test para saber que tanto sabes de mecanica.
Constara de 5 preguntas.
Cada pregunta consta de 3 alternativas.
Aprobara con mas del 75% correctas.

Mucho exito !

''')

one = input('''
    1. El aceite de su motor debe de estar ...
    
    a) Siempre el maximo nivel
    b) Por encima del valor maximo 
    c) Entre el maximo y minimo   
            
:  ''')
if one != ('a','b','c','A','B','C'):
    print('Debes seguir instrucciones. ')
    quit()
 
two = input('''
    2. Si estamos circulando con nuestro vehiculo y llevamos una marcha puesta. ¿ Cuando
    gira el disco de embrague?
    
    a) Cuando tengamos el pedal pisado  
    b) Cuando no tengamos el pedal pissado 
    c) Estara en todo momento girando, este o no este pisado
            
:  ''')
if two != ('a','b','c','A','B','C'):
    print('Debes seguir instrucciones. ')
    quit()

three = input('''
    3. Que piesa es la encargada de reallizar la union de: el arbol de transmision 
    y el eje secundario.
    
    a) Por la junta homocinetica
    b) Por la junta cardam
    c) Por la junta culata
            
:  ''')
if three != ('a','b','c','A','B','C'):
    print('Debes seguir instrucciones. ')
    quit()

For = input('''
    4. Que mision tiene la gemela o la biela de suspension ?
    
    a) Absorver las oscilaciones y alargamientos de las ballestas
    b) Aminoran las oscilaciones de la suspension
    c) Absorven las oscilaciones de la suspension. 
            
:  ''')
if For != ('a','b','c','A','B','C'):
    print('Debes seguir instrucciones. ')
    quit()

five = input('''
    5. La parte del neumatico que esta en contacto con el pavimento es ...
    
    a) La banda de rodadura
    b) Los flancos del neumatico 
    c) La carcasa del neumatico
            
:  ''')
if five != ('a','b','c','A','B','C'):
    print('Debes seguir instrucciones. ')
    quit()
    
lista= [one,two,three,For,five]
score = 0
i=0

for i in lista[i] :
    if one == 'c' or one == 'C':
        score+= 3
    if two == 'b' or two == 'B':
        score+= 3
    if three == 'b' or three == 'B':
        score+= 3
    if For == 'a' or For == 'A':
        score+= 3
    if five == 'a' or five == 'A':
        score+= 3

percentage = round(((score / 15 )*100), 2)
    
print('Tu porsentaje obtenido es {}'.format(percentage))

if percentage >= 75 :
    print('Has aprobado el curso. Felicitaciones !! ')

if 50 <= percentage < 75 :
    print('No aprobo el curso pero cuenta con un buen puntaje, siga mejorando !')

else:
    print('Debes seguir mejorando. Animo!!')




