import datetime
from Mach_Res import mach_reservierung
from Filtere import gefilterte_zimmern
from MenuGaste import *
from AktuellerGast import aktuelle_res


def menu():
    return """
0. Zuruck 
1. Mach eine Reservierung
2. Anzeige die Liste von Gästen, die aktuelle Reservierungen haben
3. Anzeige alle Zimmer gefiltert mit Preis und Meerblick Kriterien 
4. Anzeige alle Zimmer, die heute frei sind
"""


def menu_r(liste_gaste, liste_zimmern, liste_res):

    print(menu())

    try:
        opt = int(input('Option-'))
    except ValueError:
        print('die Option muss Integer sein, versuche noch einmal')
        opt = int(input('Option-'))

    while opt != 0:
        if opt == 1:

            try:
                heute = datetime.datetime.now()

                gast = Gast(input('Vorname: '), input('Nachname: '))
                print('Beginn des Aufenthalts:')
                check_in = datetime.datetime(int(input('Jahr: ')), int(input('Monat: ')), int(input('Tag: ')))
                print('Ende des Aufenthalts')
                check_out = datetime.datetime(int(input('Jahr: ')), int(input('Monat: ')), int(input('Tag: ')))
                if check_out < check_in or check_in < heute:
                    raise ValueError

            except ValueError:
                print('Die Daten die eingegeben wurden sind falsch:'
                      '\n\n-die Daten mussen in Format Jahr/Monat/Tag eingegeben werden'
                      '\n-Sie konnen nicht eine Reservierung fur die Vergangenheit machen'
                      '\n\n versuchen Sie noch einmal hier:\n')
                print('Beginn des Aufenthalts:')
                check_in = datetime.datetime(int(input('Jahr: ')), int(input('Monat: ')), int(input('Tag: ')))
                print('Ende des Aufenthalts')
                check_out = datetime.datetime(int(input('Jahr: ')), int(input('Monat: ')), int(input('Tag: ')))
            finally:

                try:
                    nr_gaste = int(input('Anzahl der Gaste die bei uns bleiben wollen: '))
                except ValueError:
                    print()
                    print('Anzahl der Gaste muss Integer sein, versuche noch einmal:')
                    print()
                    nr_gaste = int(input('Anzahl der Gaste die bei uns bleiben wollen: '))

                finally:
                    mach_reservierung(gast, nr_gaste, check_in, check_out, liste_gaste, liste_zimmern, liste_res)

            delay()
            print(menu())

            try:
                opt = int(input('Option-'))
            except ValueError:
                print('die Option muss Integer sein, versuche noch einmal')
                opt = int(input('Option-'))

        elif opt == 2:

            aktuelle_res(liste_gaste, liste_res)
            delay()
            print(menu())

            try:
                opt = int(input('Option-'))
            except ValueError:
                print('die Option muss Integer sein, versuche noch einmal')
                opt = int(input('Option-'))

        elif opt == 3:

            lz = []
            gefilterte_zimmern(liste_zimmern, lz)
            if lz:
                print('Gefilterte Zimmern:')
                for zimmer in lz:
                    print(zimmer.nummer)
            else:
                print('Keine Zimmern gefunden')

            delay()
            print(menu())
            try:
                opt = int(input('Option-'))
            except ValueError:
                print('die Option muss Integer sein, versuche noch einmal')
                opt = int(input('Option-'))

        elif opt == 4:

            heute = datetime.datetime.now()
            l = []

            for zimmer in range(len(liste_zimmern)):  # caut in lista de camere pe cele care sa fie libera azi

                inlist = False

                for r in range(len(liste_res)):  # caut in lista de rezervari toate rezervarile pe camera
                    # liste_zimmern[zimmer]

                    if liste_res[r].zimmer == liste_zimmern[zimmer].nummer:
                        inlist = True

                        if (heute < liste_res[r].check_in) or (heute > liste_res[r].check_out):
                            # daca pt o rezervare pe camera liste_zimmern[zimmer] data de azi e mai mica decat data de
                            # checkin sau mai mare decat data de checkout atunci camera e azi libera
                            l.append(liste_zimmern[zimmer])

                        else:
                            if liste_zimmern[zimmer] in l:
                                while liste_zimmern[zimmer] in l:
                                    l.remove(liste_zimmern[zimmer])
                if not inlist:
                    l.append(liste_zimmern[zimmer])

            if not l:
                print('Alle Zimmern sind heute besetzt')
            else:
                print('Diese Zimmer sind heute frei:')
                for i in l:
                    print(i, " ")

            delay()
            print(menu())
            try:
                opt = int(input('Option-'))
            except ValueError:
                print('die Option muss Integer sein, versuche noch einmal')
                opt = int(input('Option-'))
        else:
            print('Sorry, diese Option gibt es nicht')
            try:
                opt = int(input('Option-'))
            except ValueError:
                print('die Option muss Integer sein, versuche noch einmal')
                opt = int(input('Option-'))


