from tools import delay
from Funct_Gaste import *


def menu():
    return "0.Zuruck \n1.Füge ein neuer Gast hin \n2.Aktualisierung der Nachname eines Gastes \n3.Löschung " \
           "eines Gastes \n4.Anzeige die Liste von Gästen"


def menu_gaste(liste_gaste, liste_res):

    print(menu())
    try:
        opt = int(input('Option-'))
    except ValueError:
        print('die Option muss Integer sein, versuche noch einmal')
        opt = int(input('Option-'))

    while opt != 0:
        if opt == 1:

            add_gast(liste_gaste)

            delay()
            print(menu())
            opt = int(input("Option:"))

        elif opt == 2:

            aktualisiere(liste_gaste)
            delay()
            print(menu())
            opt = int(input("Option:"))

        elif opt == 3:

            loschen_eines_gastes(liste_gaste, liste_res)
            delay()
            print(menu())
            opt = int(input("Option:"))

        elif opt == 4:

            print_liste_gaste(liste_gaste)
            delay()
            print(menu())
            opt = int(input("Option:"))
        else:
            print("Error! Kein verfugbarer Menu!")
