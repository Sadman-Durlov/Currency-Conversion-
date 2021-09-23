lpv = None
spv = None

while True:

    val = input('Enter number:')

    if val == 'done':
        break

    try:
        inp = int (val)
    except:
        print('Invalid input')
        continue


    for x in [inp]:
        if lpv is None:
            lpv = x
        elif x>lpv:
            lpv = x

    for y in [inp]:
        if spv is None:
            spv = y
        elif y<spv:
            spv = y
print('Maximum is', lpv)
print('Minimum is', spv)
