n = input('Enter the number : ')

def arm(n):
    v = 0
    g = len(n)
    for i in n:
        v += int(i)**g
    if v == int(n):
        print('The given number {} is Armstrong'.format(n))
    else:
        print('The given number {} is not Armstrong'.format(n))

arm(n)


