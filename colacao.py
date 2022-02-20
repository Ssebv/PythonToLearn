
from tracemalloc import stop

# Estructura de control 
print('')
print('Bienvenidos!!')
print('''
      
Nos encontramos en la cocina hipoteticamente
Vamos a realizar una preparacion de un Colacao para desayunar

Nos dirigimos a la nevera para preguntarnos ...
''')
print('S or N')

milk= input('Hay leche ? : ')

if milk == 'S' or milk == 's':
    print('Sacamos la leche de la nevera para realizar la preparacion')
    print('Perfecto ! ')
    colacao =input('Hay colacao ? : ')
    if colacao == 'S' or milk == 's':
        print('Perfecto ! ')
        print('Podemos realizar la preparacion')
        print('''
              El desayuno queda perfecto con un buen colacao !!!
              ''')
    else: 
        print('Tendre que ir al supermercado :c ')
        stop
    
if milk == 'N' or milk == 'n':
    print('Tendre que ir al supermercado :c ')
    print('Tambien tendre que asegurarme de que si hay colacao ')
    stop
    