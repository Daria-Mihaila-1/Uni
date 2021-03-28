from Gast import Gast


def add_gast(liste_gaste):
    liste_gaste.append(Gast(input("Vorname:"), input("Nachname:")))


def aktualisiere(liste_gaste):
    nachname = input("Aktueller Nachname:")
    found = False

    for gast in liste_gaste:

        if gast.nachname == nachname:
            gast.nachname = input("Neuer Name:")
            found = True
            break

    if not found:
        print("Kein Gast mit diesem Nachname gefunden")


def loschen_eines_gastes(liste_gaste, liste_res_hotel):
    vorname = input("Vorname:")
    nachname = input("Nachname:")
    out = False
    gast_zum_loschen = Gast(vorname, nachname)

    for gast in range(len(liste_gaste)):
        if liste_gaste[gast].vorname == vorname and liste_gaste[gast].nachname == nachname:

            for g in range(len(gast_zum_loschen.liste_res)):

                for r in liste_res_hotel:

                    if gast_zum_loschen.liste_res[g] == liste_res_hotel[r]:
                        liste_res_hotel.pop(liste_res_hotel[r])
            out = True
            liste_gaste.pop(gast)
            break

    if not out:
        print("Kein Gast mit diesen Daten gefunden")


def print_liste_gaste(liste_gaste):
    if not liste_gaste:
        print("Die Liste ist leer")
    else:
        for guest in liste_gaste:
            print(guest)
