count = 0
list = ['Hello', 'World', 'Linear', 'Algorithm', 'Basic', 'Program']
itemToFind = 'Al'

while count < len(list):
    if list[count] == itemToFind:
        print('Found')
        break

    else:
        print('Not Found This Turn')

    count = count + 1
