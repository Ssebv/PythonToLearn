
print('')
print('Bienvenidos!!')
print('''
      
Este es el convertidor de divisas mas famoso de las redes. 
Ingresa la divisa que que quiere convertir ...

1 Si cuenta con Libras Esterlinas
2 Si cuenta con Euros
3 Si cuenta con Pesos Chilenos
''')
print('')
#Precios actualizados el dia 19/02/2022

option= int(input('Ingrse su opcion : '))
print('Perfecto ! ')
option2= int(input('Ahora ingrese la divisa que quieres obtener (recuerda son los mismos valores que el inicio) : '))
print('Perfecto! ')
currencies= int(input('Ingrese su total de divisas a convertir : '))

def convert(option, currencies):
    t= None
    if option == 3 and option2 ==1 :
        t= currencies * 0.00092
        t= ('Son {} Libras Esterlinas').format(t)
        
    elif option == 3 and option2 ==2 :
        t= currencies * 0.0011
        t= ('Son {} Euros').format(t)
        
    elif option == 2 and option2 ==1 :
        t= currencies * 0.83
        t= ('Son {} Libras Esterlinas').format(t)
    
    elif option == 2 and option2 ==3 :
        t= currencies * 906.73
        t= ('Son {} Pesos Chilenos').format(t)
        
    elif option == 1 and option2 ==2 :
        t= currencies * 1.20
        t= ('Son {} Euros').format(t)
        
    elif option == 2 and option2 ==3 :
        t= currencies * 1089.24
        t= ('Son {} Pesos Chilenos').format(t)
    
    
    return(t)

result= (convert(option, currencies))
print(result)
print('Gracias por probar el programa !!')