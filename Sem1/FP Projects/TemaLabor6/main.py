from MenuGaste import menu_gaste
from Menu_Zimmern import menu_zimmern
from Menu_Gemeinsam import menu_r
from Gast import Gast
from Zimmer import Zimmer


def menu():
    return "0. Exit\n1. Menu Gaste \n2. Menu Zimmern \n3. Menu Reservierungen"


def main_menu():

    g1 = Gast('Ana', 'Blandiana')
    g2 = Gast('Mickey', 'Mouse')
    g3 = Gast("Minnie", "Mouse")
    g4 = Gast('Donald', 'Duck')
    g5 = Gast('Goofy', 'Goof')
    g6 = Gast('Daisy', 'Duck')
    liste_gaste = [g1, g2, g3, g4, g5, g6]

    z1 = Zimmer(13, 5, 100, 'blau', True, True)
    z2 = Zimmer(10, 2, 250, 'rot', False, True)
    z3 = Zimmer(201, 4, 300, 'rosa', True, True)
    z4 = Zimmer(712, 2, 250, 'grun', False, True)
    liste_zimmern = [z1, z2, z3, z4]

    liste_res = []

    print(menu())
    try:
        opt = int(input("Menu:"))
    except ValueError:
        print('Option muss eine Zahl sein, versuche noch einmal!')
        opt = int(input("Menu:"))
    finally:
        while opt != 0:
            if opt == 1:
                menu_gaste(liste_gaste, liste_res)
                print(menu())
                opt = int(input("Menu:"))
            elif opt == 2:
                menu_zimmern(liste_zimmern)
                print(menu())
                opt = int(input("Menu:"))
            elif opt == 3:
                menu_r(liste_gaste, liste_zimmern, liste_res)
                print(menu())
                opt = int(input("Menu:"))
            else:
                print("Error! Kein verfugbarer Menu! versuche noch einmal")
                opt = int(input("Menu:"))


main_menu()
