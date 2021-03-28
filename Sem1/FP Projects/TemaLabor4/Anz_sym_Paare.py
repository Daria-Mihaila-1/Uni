"""
2. Schreiben Sie die Anzahl von symmetrischen Paaren (xy) und (yx).
"""


def symetrisch(x, y):
    """
    bestimmt weder zwei zweistellige Zahlen x und y symetrisch sind
    :param x: ein Element der Liste
    :param y: ein Element der Liste
    :return: True- wenn x und y symetrisch
            False - sonst
    """
    if ((x % 10) == (y // 10)) and ((x // 10) == (y % 10)):
        return True
    else:
        return False


def anz_von_sym(lst):
    """
    mit 2 For-Schleifen durchquert die Funktion die Liste und untersucht je ein Element mit der restlichen Liste
    :param lst: die Liste
    :return: Anzahl der symetrischen Paaren der Liste
    """
    anz = 0
    for i in range(len(lst) - 1):
        for j in range(i, len(lst)):
            if symetrisch(lst[i], lst[j]):
                anz += 1
    print("Anzahl symmetrischer Paaren:", anz)
