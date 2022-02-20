
print('')
print('Bienvenidos')
print('Debes ingresar que quieres convertir para realizar el proceso.')
print('')

option= int(input('Ingrese 1 si desea convertir a Fahrenheits o 2 si desea convertir a Celsius : '))
print('')
degrees= int(input('Ingrese los grados a convertir : '))

def convert(option, degrees):
    t= None
    if option == 1 :
        t= (degrees * (9/5))+ 32 
        t= ('Son {} grados Fahrenjeits').format(t)
        
    else:
        t=(degrees -32)*(5/9)
        t= ('Son {} grados Celsius').format(t)
    
    return(t)

temperature= (convert(option, degrees))
print(temperature)