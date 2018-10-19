def convert(c):
    F = c*1.8+32
    return F

def table():
    print('{:>8}'.format('F'), '{:>10}'.format('C'))
    x = -30.0
    for i in range(8):
        print('{:>10}'.format(convert(x)), '{:>10}'.format(x))
        x += 10.0

table()
