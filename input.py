from tkinter import N

print('Bienvenidos al juego !')
numero1= int(input('Ingrese el primer numero:   '))
numero2= int(input('Ingrase el segundo numero:   '))
numero3= int(input('Ingrase el tercer numero:   '))

mayor=max(numero1,numero2, numero3) 
minimo=min(numero1,numero2, numero3) 

print('El numero menor es {}'.format(minimo) + ' y el numero mayor es {}'.format(mayor)) 

print('El numero mayor entre {}, {} y {} es : {}, y el mas pequeño es : {}'.format(numero1,numero2,numero3,mayor,minimo)) 

print('Gracias por jugar !')

