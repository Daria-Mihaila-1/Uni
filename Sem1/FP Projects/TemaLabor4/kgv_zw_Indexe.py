from math import gcd


def kleinste_gemeinsamer_vielfach(lst, frm, to):
    """
    die Funktion gibt den kleinsten gemeinsamen Vielfachen aller Elemente der Liste, die zwischen
    den Indexen "frm"(from) und "to" liegen, zuruck
    :param lst: die Liste die gegeben wird
    :param frm: der Index von dem man das Bestimmen des kgv's beginnt
    :param to:  der Index bis zu welchem das kgv bestimmt wird
    :return: kleinste gemeinsame Vielfache aller Elemente der Liste,
    die zwischen den Indexen "frm"(from) und "to" liegen
    """
    kgv = lst[frm]

    prod = lst[frm]
    # das Produkt zw dem kgv zweier Zahlen und einer neuen Zahl

    for i in range((frm+1), (to+1)):

        d = gcd(lst[i], prod)
        # das ggt zw dem Produkt und einer neuen Zahl
        prod *= lst[i]
        kgv = prod // d

        prod = kgv
        # weiter arbeite ich mit dem kgv der vorigen Zahlen

    return kgv
