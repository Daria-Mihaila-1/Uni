
import operator
def filtere(bez, y):
    ecnoua = 'x=y'
    x = 0
    pozitii = {}
    for i in range(len(bez)):
        pozitii[bez[i]] = i + 1
    p1 = pozitii['x']
    p2 = pozitii['y']
    pegal = pozitii['=']
    if ((p1 < pegal) and (p2 < pegal)) or ((p1 > pegal) and (p2 > pegal)):
        p3 = abs(p2 - p1) - 1
        if p1 < pegal:
            nr = int(bez[-1])
        else:
            nr = int(bez[0])
        if '+' in bez:
            ecnoua = 'x=nr-y'
            x = nr - y
        elif '-' in bez:
            ecnoua = 'x=nr+y'
            x = nr +y
        elif '*' in bez:
            ecnoua = 'x=nr/y'
            x = nr / y
        else:
            ecnoua = 'x=nr*y'
            x = nr * y
    else:



def main():
    bez = input("Beziehung=")
    y = 2
    filtere(bez,  y)

main()
