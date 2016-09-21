count = 1
list = [1, 2, 3, 5,7,2,4,5,6,4]
maximum = 0

while count < len(list):
    if list[count] > maximum:
        maximum = list[count]

    count = count + 1

print(maximum)
