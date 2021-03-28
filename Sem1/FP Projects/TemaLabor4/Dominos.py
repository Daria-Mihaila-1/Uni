"""
6. Finden Sie die längste zusammenhängendeDominoTeilfolge.
Eine Domino Teilfolge ist definiert als x1y1, x2y2, wo y1=x2. (z.B: 89, 95, 54)
"""


def domino(lst):
    """
    :param lst: eine Liste
    :return:die Langste Folge von einanderfolgenden Domino-Elementen aus einer Liste
    """
    lmax = 1
    l = 1
    stanga = -1
    dreapta = -1

    for i in range(len(lst)-1):
        y1 = lst[i] % 10
        x2 = lst[i+1] // 10
        if y1 == x2:
            if l == 1:
                st = i
            l += 1
            dr = i+1
            if l > lmax:
                lmax = l
                stanga = st
                dreapta = dr
        else:
            l = 0

    print(lst[stanga:dreapta+1])

