import os
print('')
print('Bienvenidos!!')
print('''
Juego de la mazmorra 
------------------------

Te encuentras en una prision con diferentes objetos a tu alrededor, algunos de ellos
te podran ayudar a escapar de la celda para posteriormente salir de la prision sin que te capture la policia.
Tambien te pueden capturar al instante asi que ve bien cual es tu decision.

- Recuerda tendras diferentes selecciones a lo largo del juego.
- Aegurate de marcar A , B , C o en los diferentes casos para su ejecucion.

-------------------------

Miras a tu alrededor y te encuentras con los siguientes objetos :

A. Un desatornillador
B. Una pala
C. Una lima
D. Una motosierra

''')
print('')

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)

option = None
while option != 'A' and option != 'B' and option != 'C' and option != 'D' and option != 'E' and option != 'F':
    option = input('Ingrese la opcion que mas estime conveniente :  ').capitalize()

if option == 'A' or option == 'a' :
    
    clearConsole()
    print('Abres una escotilla que se encuentra por debajo del escusado y encuentras otros dos objetos :')
    print('''
    B. Una pala
    C. Una lima
    D. Una motosierra
    E. Cuerda
    F. Palanca
    ''')
    option = input('Que deseas hacer ? Ocupar la cuerda o la palanca o tambien puedes elegir objetos aun no seleccionados : ')
    
    if option == 'C' or option == 'c' :
        
        clearConsole()
        print('Logras limar una de los pilares de la ventana dejando justo un espacio para lograr salir')
        print('''
            B. Una pala
            D. Una motosierra
            E. Cuerda
            F. Palanca
        ''')
        option = input('Que haces ahora ? : ')
        if option == 'E' or option == 'e' :
            print('Logras atarla a uno de los pilares para poder hacer un descenso perfecto')
            print('Escapas con exito !!')
            exit()
        else: 
            print('Te han descubierto intentando escapar :( ')
            exit()
                
    elif option == 'E' or option == 'e' :
        clearConsole()
        print('La cuerda me podria servir para escapar por la ventana')
        print('Pero primero tengo que buscar la forma de como romper los pilares, de todas maneras atas la cuerda a la ventana')
        print('''
            B. Una pala
            C. La lima
            D. Una motosierra
            F. Palanca
        ''')
        option = input('Que haces ahora ? : ')
        if option == 'C' or option == 'c' :
            clearConsole()
            print('Logras limar una de los pilares de la ventana dejando justo un espacio para lograr salir')
            print('Al tener la cuerda atada tienes mas tiempo para salir')
            print('Escapas con exito !!')
            exit()
        else: 
            clearConsole()
            print('Te han descubierto :c ')
            exit()
        
    elif option == 'F' or option == 'f' :
        clearConsole()
        print('La palanca me podria servir para intentar romper los pilares de la ventana')
        print('Te encuentran :c ')
        exit()
 
    else:
        clearConsole()
        print('Te encuentran :c ')
        exit()
        
elif option == 'D' or option == 'd' :
    clearConsole()
    print('La motosierra hace mucho ruido, es una pesima idea amigx ')
    print('Te han descubierto :( ')
    exit()

elif option == 'C' or option == 'c' :
    clearConsole()
    print('Logras limar una de los pilares de la ventana dejando justo un espacio para lograr salir')
    print('''
            A. Desatornillador
            B. Una pala 
            D. Una motosierra
        ''')
    option = input('Que haces ahora ? : ')
    
    if option == 'A' or option == 'a' :
        
        clearConsole()
    
        print('Abres una escotilla que se encuentra por debajo del excusado y encuentras otros dos objetos :')
        elements.append('Cuerda')
        elements.append('Palanca')
        print('''
        B. Una pala
        D. Una motosierra
        E. Cuerda
        F. Palanca
        ''')
        option = input('Que haces ahora ? : ')
        if option == 'E' or option == 'e' :
            clearConsole()
            print('Atas la cuerda en uno de los pilares de la ventana ')
            print('Logras escapar !! ')
            exit()
        else:  
            clearConsole()
            print('Te han descubierto :c ')
            exit()
    else: 
        clearConsole()
        print('Te han descubierto :c ')
        exit()
        
else: 
    clearConsole()
    print('Al elegir la pala, cabas un agujero y te descubren por todo el tiempo que te demoras !')
    exit()
    

