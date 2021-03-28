"""Gegeben  sei eine  Listevon  Zahlenin  der  Form  xy.Schreiben  Sie  eine PythonKonsolenanwendung,
welche jededer folgenden Aufgabenlöst.
JedeAufgabe soll in einer Funktion umgesetzt sein.
1.Enfernen Sie die Zahlen die sich wiederholen.
"""


def entferne(lst):
    """
    -entfernt alle Zahlen aus der Liste die sich wiederholen
    :param lst: die Liste aus der man entfernt
    :return: eine neue Liste die alle Elemente nur ein Mal enthalt
    """
    d = {}
    # ein "Erscheinungs"- dictionary
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    lst2 = []
    for i in d:
        if d[i] == 1:
            lst2.append(i)
    print("neue Liste:", lst2)
