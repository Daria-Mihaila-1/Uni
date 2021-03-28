from tools import delay
from Funct_Zimmern import *


def menu():
    return "0.Zuruck\n1.Füge ein Zimmer hin\n2.Aktualisierung des " \
           "Preises eines Zimmers\n3.Löschung eines Zimmers\n4.Anzeige die Liste von Zimmern"


def menu_zimmern(liste_zimmern):

    print(menu())
    try:
        opt = int(input('Option-'))
    except ValueError:
        print('die Option muss Integer sein, versuche noch einmal')
        opt = int(input('Option-'))
    while opt != 0:
        if opt == 1:

            add_zim(liste_zimmern)

            delay()
            print(menu())
            opt = int(input("Option:"))

        elif opt == 2:

            aktualisiere_preis(liste_zimmern)

            delay()
            print(menu())
            opt = int(input("Option:"))

        elif opt == 3:

            losche_zimmer(liste_zimmern)

            delay()
            print(menu())
            opt = int(input("Option:"))

        elif opt == 4:

            print_liste_zimmern(liste_zimmern)

            delay()
            print(menu())
            opt = int(input("Option:"))
        else:
            print("Error! Kein verfugbarer Menu!")

