#Python 3
#Programa que muestra animales 


cat = '''
      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)  
'''
dog= '''
    ___
 __/_  `.  .-"""-.
 \_,` | \-'  /   )`-')
  "") `"`    \  ((`"`
 ___Y  ,    .'7 /|
(_,___/...-` (_/_/ 
'''
monkey='''
           ."`".
       .-./ _=_ \.-.
      {  (,(oYo),) }}
      {{ |   "   |} }
      { { \(---)/  }}
      {{  }'-=-'{ } }
      { { }._:_.{  }}
      {{  } -:- { } }
      {_{ }`===`{  _}
     ((((\)     (/))))
'''
while(True):
    print('_'*50)
    print("Bienvenido")
    print("1. Dog ")
    print("2. Cat ")
    print("3. Monkey")
    print("4. Exit")
    opcion = int(input("Elige una opción:  "))

    if opcion == 1:
        print(dog)
    elif opcion == 2:
        print(cat) 
    elif opcion == 3:
        print(monkey)
    elif opcion == 4:
        break
    else:
        print("Error, opción inválida")