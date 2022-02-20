import random
from tkinter import N

# Numero aleatorio 
num_win = random.randint(1,10)

print('Bienvenidos!!')
print('''
      
Este es el juego de las adivinanzas, tendra que elegir un numero del 1 al 10.
Ojo que tines solo un intento de acertar. Mucha suerte !!

[ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]

''')
print('')
num_selected = int(input('Ingrese un numero del 1 al 10 : '))

if num_selected == num_win:
    print ('Felicidades le acertaste al numero correcto : {}'.format(num_selected))
    
if num_selected > 10 or num_selected < 1 :
    print('El rango de numero es del 1 al 10. Lea las instrucciones!!')
    
else:
    print('Haz fallado, mejor suerte para la proxima, el numero ganador era {}'.format(num_win))