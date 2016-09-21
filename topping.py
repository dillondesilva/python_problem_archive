topping = input('Topping: ')
list = []
counter = 0

while topping:

    if topping in list:
        print('You already have that!')

    topping = input('Topping: ')

    elif topping != '':
        list.append(topping)
        counter = counter + 1

for i in list:
    print('You have ' + i)

print('That is a total of ' + str(counter) + ' topping(s)')
