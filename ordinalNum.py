ui = input('Number: ')

if ui == '1':
    print(ui + 'st')

elif ui == '2':
    print(ui + 'nd')

elif ui == '3':
    print(ui + 'rd')

elif ui[-1] == '1' and ui[-2] != '1':
    print(ui + 'st')

elif ui[-1] == '2' and ui[-2] != '1':
    print(ui + 'nd')

elif ui[-1] == '3' and ui[-2] != '1':
    print(ui + 'rd')

else:
    print(ui + 'th')
