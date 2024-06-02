# Usando Declaraciones Condicionales
# Las declaraciones condicionales son necesarias para
# que un programa tome decisiones basadas en un conjunto
# de condiciones lógicas.
# Existen tres construcciones principales en Python para esto:
# la declaración if, las declaraciones if-else y la declaración if-elif.

avalue = int(input('Enter an integer greater than 10: ')) #variable entera entrada por teclado
if avalue > 10:                                           # si avalue es mayor a 10 se ejecuta la parte indentada
    print('Thank you')
    avalue = avalue / 2
    print('This is your value divided by 2: ', avalue)
print('Did your if code execute?')                        #si no se cumple la condición se ejecuta esta parte
print()

# Observa la sintaxis requerida para que la declaración "if" funcione:
# La expresión lógica que sigue a "if" debe terminar con dos puntos (:)
# El código que se ejecutará si la condición lógica es verdadera debe tener sangría.
# La sangría es la forma en que Python sabe que tienes un grupo de comandos
# dentro de la declaración if.

avalue = int(input('Enter an integer greater than 10: '))
if avalue > 10:
    print('Thank you')
    avalue = avalue / 2
    print('This is your value divided by 2: ', avalue)
else:                                                     #si no se cumple la condición se ejecuta esta otraparte
    avalue = avalue / 5
    print('This is your value divided by 5: ', avalue)
    print('Which code group executed?')
print()

avalue = int(input('Enter an integer greater than 10: '))  # elif se usa cuando hay diversas posobilidades
if avalue >= 10:
    print('Thank you')
    avalue = avalue / 2
    print('This is your value divided by 2: ', avalue)
elif (avalue < 10) and (avalue > 4):
    avalue = avalue / 5
    print('This is your value divided by 5: ', avalue)
else:
    avalue = avalue * 100
    print('This is your value times 100: ', avalue)
print('Which code group executed?')
print()

# Bucles e Iteraciones
# Usando bucles "while"

# Los bucles son necesarios cuando necesitamos realizar un conjunto de operaciones varias veces.
# El primer tipo de bucle del que hablaremos se llama bucle while.
# El bucle while verifica una condición lógica al igual que la declaración if.
# Si la condición es verdadera, el código dentro del bucle while se ejecutará
# hasta que la condición que se está verificando se vuelva falsa.


avalue = int(input('Please enter the number 10: '))
while (avalue != 10):                                # mientras el valor de avalue sea diferente de 10
    print('Your input value is not equal to 10')
    print('Please try again: ')
    avalue = int(input('Enter the number 10: '))     # si entramosun valor diferente de 10 se repite el proceso
print('Thank you')
print('You entered a value of 10')

# Las reglas de sintaxis son similares a las de las declaraciones "if":
# La expresión lógica que sigue a "while" debe terminar con dos puntos (:)
# El código que se ejecutará si la condición lógica se cumple debe tener sangría.
# La sangría es la forma en que Python sabe que tienes un grupo de comandos dentro
# de la declaración while.


# Usando el bucle "for"
# El bucle for es útil cuando sabemos cuántas veces se debe ejecutar un bucle.
# En lugar de basar el número de iteraciones en una condición lógica, el bucle for
# controla la cantidad de veces que se iterará un bucle contando o avanzando
# a través de una serie de valores.


for i in range(11):  # i empieza en 0 y termina en 11-1=10 el número de valores que toma i es 11 (0,1,2,3,4,5,6,7,8,9,10)
    print(f'Value of i is {i}')  # se imprime el valor de i)
print('Otro ejemplo ')

for j in range(4, 11):  # j empieza en 4 y termina en 11-1=10
    print(f'Value of j is {j}')  # se imprime el valor de j
print('Otro ejemplo ')
for k in range(4, 11, 3):  # k empieza en 4 y termina en 11-1=10 (el paso es 3 --> 4+3, 7+3)
    print(f'Value of k is {k}')  # se imprime el valor de k (4,7,10)
print('Otro ejemplo ')
for i in range(0, -11, -1):  # i empieza en 0 y termina en -11+1=-10 el paso es -1
    print(f'Value of i is {i}')  # se imprime el valor de i
print('Otro ejemplo ')

for i in range(-3, -11, -3):  # i empieza en -3 y termina en -11+1= -10 el paso es -3
    print(i)
print()
# El comando range(5) crea una serie de cinco valores del 0 al 4
# para que la variable i los recorra.
# La declaración for i in range(5) significa efectivamente usar
# la variable i para contar a través de cinco valores,
# comenzando en 0 y deteniéndose en 4 (Python, por diseño,
# comienza a contar con el valor 0).
# Además, una vez más, presta mucha atención a la colocación
# de los dos puntos (:) al final de la declaración for,
# así como a la sangría.....(range(m,n,s) m es el primero,
# a n le quita 1(se resta si es positivo, se suma si es negativo)
# s es el paso)

n = 8
sumval = 0
for i in range(n):
    sumval = sumval + i  # Esta sentencia tambien se puede escribir: sumval +=  i
    print('Adding ', i, 'to the previous sum = ', sumval)
print()

n = 8
sumval = 0
for i in range(n):
    sumval += i
    print('Adding ', i, 'to the previous sum = ', sumval)
# Este bucle cuenta desde 0 hasta n-1, donde n ha sido
# establecido con un valor de 8.
# el valor inicial de suma se establece en cero y luego
# se van sumando los valores sucesivos de la variable i a
# la suma cada vez que se realiza una iteración del bucle.
print()
strval = 'forever'
e_count = 0
for letter in strval:
    if letter == 'e':
        e_count = e_count + 1
print('The letter e occurred ', e_count, 'times')
print()

# Observa cómo la declaración "if" está "anidada" (y, por lo tanto,
# tiene sangría) dentro del bucle "for".
# La variable letter recorre cada carácter en la cadena strval,
# que ha sido inicializada como la cadena "forever". Si se encuentra
# una "e" mientras se itera a través de cada carácter,
# la variable count se incrementa. Cuando el bucle termina,
# el número de ocurrencias se muestra en pantalla.

# También es posible anidar bucles dentro de bucles


m = 4
n = 3
for i in range(m):
    for j in range(n):
        print('i=', i, ' j=', j)
print()
# Esto se llama bucle "for" anidado porque el bucle "for" interno,
# dependiendo de la variable j, está anidado dentro del bucle "for"
# externo, que depende de la variable i.
# Esto debería ser claro por la sangría del bucle interno con respecto
# al bucle externo. Para cada iteración de la variable i, la variable j
# recorre todos sus valores posibles que dependen de range(m).
# Para que se actualice a su próximo valor, el bucle interno debe
# iterar a través de todos sus valores.

# A veces es necesario salir abruptamente de un bucle cuando se cumple
# una cierta condición.
# La declaración "break" es a veces útil para tal aplicación.


strval = 'forever'
for letter in strval:
    print(letter)
    if letter == 'e':
        break
print('The letter e has been found')
print()

# en este ejemplo, la variable letter recorre cada carácter
# en la cadena y se detiene cuando se encuentra el carácter "e".

# De otro modo, encontrar una condición en un bucle puede requerir
# que se salte un conjunto de comandos y efectivamente se avance
# más rápido a la siguiente iteración.
# La función continue puede ser usada para esta aplicación.

# Finalmente, la función pass dentro de un bucle es una función
# nula que no hace nada.
# A veces es útil cuando se coloca en un programa donde se
# pretende continuar con código  que aun no ha sido escrito.


aval = 4
for i in range(9):
    print('i = ', i)
    if i > aval:                 # si el valor de i es mayor que 4 se para el bucle
        print('stopping here ...')
        break
print('Program terminating')
print()
aval = 4
for i in range(9):
    if i == aval:
        continue    # si el valor de i es igual a 4 se continua el bucle sin imprimir i = 4
    print('i=', i)
print()
aval = 4
for i in range(9):
    if i == aval:
        pass        # si el valor de i es igual a 4 pass no hace nada
        print('What does the pass instruction do?')
    print('i=', i)
print('ASCII-art example')
print('''
        ,--._______,-.
       ,','  ,    .  ,_`-.
      / /  ,' , _` ``. |  )       `-..
     (,';'""`/ '"`-._ ` \/ ______    '\'
       : ,o.-`- ,o.  )\` -'      `---.))
       : , d8b ^-.   '|   `.      `    `.
       |/ __:_     `. |  ,  `       `    '\'
       | ( ,-.`-.    ;'  ;   `       :    ;
       | |  ,   `.      /     ;      :    '\'
       ;-'`:::._,`.__),'             :     ;
      / ,  `-   `--                  ;     |
     /  \                   `       ,      |
    (    `     :              :    ,\      |
     \   `.    :     :        :  ,'  \    :
      \    `|-- `     \ ,'    ,-'     :-.-';
      :     |`--.______;     |        :    :
       :    /           |    |         |   '\'
       |    ;           ;    ;        /     ;
     _/--' |   -hrr-   :`-- /         \_:_:_|
   ,',','  |           |___ '\'
   `^._,--'           / , , .)
                      `-._,-'


                             ;'\'
                            |' '\'
         _                  ; : ;
        / `-.              /: : |
       |  ,-.`-.          ,': : |
       \  :  `. `.       ,'-. : |
        \ ;    ;  `-.__,'    `-.|
         \ ;   ;  :::  ,::'`:.  `.
          \ `-. :  `    :.    `.  '\'
           \   \    ,   ;   ,:    ('\'
            \   :., :.    ,'o)): ` `-.
           ,/,' ;' ,::"'`.`---'   `.  `-._
         ,/  :  ; '"      `;'          ,--`.
        ;/   :; ;             ,:'     (   ,:)
          ,.,:.    ; ,:.,  ,-._ `.     '\'""'/
          '::'     `:'`  ,'(  \`._____.-'"'
             ;,   ;  `.  `. `._`-.  '\''\'
             ;:.  ;:       `-._`-.\  \`.
              '`:. :        |' `. `\  ) '\'
                 ` ;:       |    `--\__,'
                   '`      ,'
                        ,-''')
