print('')
print('Bienvenidos!!')
print('''
      
En esta aplicacion elegiremos el mejor celular para el usuario : 

-Debes ingrasar siempre el nombre de la seleccion en cuestion
-Dan lo mismo las mayusculas en este programa

''')
print('')

system  =input('Que sistema operativo prefieres,  IOS o Android ? : ')

if system == 'Android' or system == 'android' :
    money = input('Tienes dinero o prefieres un celular de gama baja ? (1 si tienes dinero y 2 si quieres uno de gama baja): ')
    if money == '2' :
        print('Tu celular indicado es el Android Chino de 100 dollares')
    else: 
        camera = input('Te importa la camara del movil ? (si o no) : ')
        if camera == 'si' or camera == 'SI':
            print('Tu celular indicado es el Google Pixel con una super camara ')
        else:
            print('Tu celular indicado es un Android calidad precio ')

elif system == 'IOS' or system == 'ios' or system == 'Ios':
    money = input('Tienes dinero o prefieres un celular de gama baja ? (1 si tienes dinero y 2 si quieres uno de gama baja): ')
    if money == '1' :
        print('Tu celular indicado es un Iphone Ultra Pro Max')
    else: 
        print('Tu celular indicado es un iphone de segunda mano')
else: 
    print('Por favor lea bien las instrucciones !')
