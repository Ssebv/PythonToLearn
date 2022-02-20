print('Bienvenidos al Zoo')
print('''
      
Verificaremos su edad para saber que tipo de descuento tiene ...

''')
print('')
age = int(input('Ingrese su edad : '))
print('''
En nuestros servidores nos encontramos con 4 tipos de DNI

Estudiante -> E
Pensionista -> P
Familia numerosa -> F
Nada -> N

''')
tipe_DNI = input('Ingrese su tipo de DNI segun su letra correspondiente : ')

if  25 <= age <= 35 and tipeDNI == 'E' or tipeDNI == 'e':
    print('Se te aplica el descuento de Estudiante')
    
elif  age >= 65 and tipeDNI == 'P' or tipeDNI == 'p':
    print('Se te aplica el descuento de Pensionista')
    
elif 21 <= age <= 90 and tipeDNI == 'F' or tipeDNI == 'f':
    print('Se te aplica el descuento de Familia numerosa')

else:
    print('No se te puede aplicar el descuento :c ')