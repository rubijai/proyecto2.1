'''l = [1,2,3,4,5,6,7,8,9]
l1 = [n**3 for n in l if n%2 != 0]
print(l1)

cad = 'forever'
print(cad.upper())
print(cad.find('e'))
lista = []
for l in cad:
    if l in lista:
        # continue
        pass
    lista.append(l)

print(lista)




n = int(input('entre un entero n = '))
if n%2 == 0:
    print(f'n = {n} is even')

else:
    print(f'n = {n} is odd')


height = int(input('height = '))
age = int(input('age = '))
if height > 150:
    if age >= 21:
        print('you pay: $12')
    else:
        print('you pay: $7')
else:
    print('you are not allowed    in')


string = input('write your name: ')
print(f'su nombre tiene {len(string)} caracteres')
print(string[1])

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if (year % 4 == 0 and year % 100 == 0 and year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f'The year {year} is leap year')
else:
    print(f'The year {year} is not leap year')


#https://ascii.co.uk/art/dog'''

pizza_size = (input('size : input S for small pizza, M for medium or L for large')).capitalize()
add_pepperoni = (input('Pepperoni : Y or N ')).capitalize()
extra_cheese = (input('Extra cheese: Y or N ')).capitalize()
#print(pizza_size)
bill = 0
if extra_cheese == 'Y':
    bill += 1
if add_pepperoni == 'Y' and pizza_size == 'S':
    bill += 2
if add_pepperoni == 'Y' and (pizza_size == 'L' or pizza_size == 'M'):
    bill += 3
if pizza_size == 'S':
    bill += 15
elif pizza_size == 'M':
    bill += 20
else:
    bill += 25

print(f'Your final bill is: ${bill}.')

cad = 'forever'
print(cad[4])