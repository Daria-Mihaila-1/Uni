from Zimmer import Zimmer


def add_zim(liste_zimmern):
    liste_zimmern.append(Zimmer(int(input("Zimmernummer:")), int(input("Anzahl moglichen Gasten:")),
                                int(input("Preis:")), input("Farbe:"), bool(input("Meerblick:")), bool(input('Frei'))))


def remove_zim(liste_zimmern, z):
    liste_zimmern.remove(z)


def aktualisiere_preis(liste_zimmern):
    nr = int(input("Zimmernummer:"))
    found = False
    for zimmer in liste_zimmern:

        if zimmer.nummer == nr:
            zimmer.preis = int(input("Neuer Preis:"))
            found = True

    if not found:
        print("Kein Zimmer mit diesem Nummer gefunden")


def print_liste_zimmern(liste_zimmern):
    if not liste_zimmern:
        print("Die Liste ist leer")
    else:
        for zimmer in liste_zimmern:
            print(zimmer)


def losche_zimmer(liste_zimmern):
    num = int(input("Zimmernummer:"))
    out = False
    for nr in range(len(liste_zimmern)):
        if liste_zimmern[nr].nummer == num:
            liste_zimmern.pop(nr)
            out = True
            break
    if not out:
        print("Kein Zimmer mit dieser Nummer gefunden")
