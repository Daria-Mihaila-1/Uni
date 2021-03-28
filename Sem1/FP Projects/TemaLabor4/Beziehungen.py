def filtere(bez, el, l_neu):
    """
    untersucht was fur eine Art von Beziehung angegeben wird und basierend darauf untersucht sie ob ein Element(el) die
    Bedingung erfullt
    :param bez: angegebene Beziehung
    :param el: ein Element aus einer Liste
    :param l_neu: eine neue Liste mit den Elementen die die Bedingung erfullen
    :return: neue Liste
    """
    x = el // 10
    y = el % 10
    pegal = bez.index("=")
    px = bez.index("x")
    py = bez.index("y")
    if px < pegal:
        if py > pegal:
            # Beziehung der Art: x = y [Operator] Zahl]
            if "+" in bez:
                nr = int(bez[-1])
                if x == y + nr:
                    l_neu.append(el)
            if "-" in bez:
                nr = int(bez[-1])
                if x == y - nr:
                    l_neu.append(el)
            if "*" in bez:
                nr = int(bez[-1])
                if x == y * nr:
                    l_neu.append(el)
            if "/" in bez:
                nr = int(bez[-1])
                if x == y + nr:
                    l_neu.append(el)
        else:
            # Beziehung der Art: x [Operator] y = [Zahl]
            if "+" in bez:
                nr = int(bez[-1])
                if x + y == nr:
                    l_neu.append(el)
            elif "-" in bez:
                nr = int(bez[-1])
                if x - y == nr:
                    l_neu.append(el)
            elif "*" in bez:
                nr = int(bez[-1])
                if x * y == nr:
                    l_neu.append(el)
            elif "/" in bez:
                nr = int(bez[-1])
                if x / y == nr:
                    l_neu.append(el)

    return l_neu
