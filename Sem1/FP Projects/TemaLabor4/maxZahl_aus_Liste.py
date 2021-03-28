def lista_aparitii(l):
    """
    generiert eine Erscheinungsliste mit die Erscheinungen aller Ziffern die sich in der Liste l befinden
    :param l: eine Liste
    :return: eine Erscheinungsliste
    """
    la = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(l)):
        x = l[i]
        while x != 0:
            la[x % 10] += 1
            x = x // 10
    return la


def max_zahl(l):
    """
    baut die grosstmogliche Zahl mz(max Zahl) aus allen Ziffern der Zahlen der Liste l
    :param l: eine Liste
    :return: die grosstmogliche Zahl
    """
    mz = 0
    la = lista_aparitii(l)

    for i in range(len(la)-1, -1, -1):
        # die Erscheinungsliste wird von rechts nach liks durchquert
        j = 1
        while j <= la[i]:
            # die Schleife wiederholt sich la[i] Mal, la[i] sei die Anz der Erscheinungen der Ziffer i in der Liste
            mz = mz * 10 + i
            j += 1
    return mz
