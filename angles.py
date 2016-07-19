angleInput = input('Type in the space of your angle');
number = int(angleInput)

if number < 90:
    print('Your angle is acute')

if number == 90:
    print('Your angle is a right angle')

if number > 90 and number < 180:
    print('Your angle is obtuse')

if number == 180:
    print('Your angle is a straight angle')

if number > 180 and number < 360:
    print('Your angle is a reflex angle')

if number == 360:
    print('Your angle is a revolution')

elif number > 360 or number < 0:
    print('Sorry that is an invalid angle')
