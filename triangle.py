side1 = int(input('Side 1 '));
side2 = int(input('Side 2 '));
side3 = int(input('Side 3 '));

hypotenuse = side1;
opposite = side2;
adjacent = side3;

if side1 > side2 and side1 > side3:
    hypotenuse = side1
    opposite = side2;
    adjacent = side3;

if side2 > side1 and side2 > side3:
    hypotenuse = side2
    opposite = side1;
    adjacent = side3;

if side3 > side1 and side3 > side2:
    hypotenuse = side3
    opposite = side1;
    adjacent = side2;

if hypotenuse > opposite + adjacent:
    print('Oops. You need to work on the lengths of that triangle')

else:
    print('That is a perfect triangle')
