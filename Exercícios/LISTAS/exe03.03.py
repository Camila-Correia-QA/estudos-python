ordered = []

for i in range(5):
    num = int(input("Type in an int: "))

    for idx, val in enumerate(ordered):
        if val >= num:
            ordered.insert(idx, num)

            if idx: print('Added', num, 'at index:', idx)
            else: print('Added', num, 'at the beginning of the list')

            break

    else: ordered.append(num); print('Added', num, 'at the end of the list')

print(ordered)