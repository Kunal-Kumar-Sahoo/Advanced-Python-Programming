def abs(x):
    return x if x > 0 else -x

def A(height):
    width = height // 2 + 1
    for i in range(height):
        if i == 0 or i == width-1:
            print('* ' * width)
        else:
            print('* ' + '  ' * (width-2) + '* ')
    print()

def B(height):
    width = height // 2 + 1
    for i in range(height):
        if i == 0 or i == width-1 or i == height-1:
            print('* ' * (width-1))
        else:
            print('* ' + '  ' * (width-2) + '*')
    print()

def C(height):
    width = height // 2 + 1
    for i in range(height):
        if i == 0 or i == height-1:
            print('* ' * width)
        else:
            print('* ')
    print()

def D(height):
    width = height // 2 + 1
    for i in range(height):
        if i == 0 or i == height-1:
            print('* ' * (width-1))
        else:
            print('* ' + '  ' * (width-2) + '* ')
    print()

def E(height):
    width = height // 2 + 1
    for i in range(height):
        if i == 0 or i == height-1:
            print('* ' * width)
        elif i == height // 2 - 1:
            print('* ' * (width // 2 + 2))
        else:
            print('* ')
    print()

def F(height):
    width = height // 2 + 1
    for i in range(height):
        if i == 0:
            print('* ' * width)
        elif i == height // 2 - 1:
            print('* ' * (width // 2 + 2))
        else:
            print('* ')
    print()


if __name__ == '__main__':
    A(8)
    B(8)
    C(8)
    D(8)
    E(8)
    F(8)