def primz_kleiner_als_n(n):
    for i in range(2, n):
        if i == 2:
            print(i)
        else:
            for t in range(2, int(i**(1/2))+1):
                if i % t == 0:
                    break
            else:
                    print(i)

"""def langste_folge(lst):

    lmax = 1
    for i in range(len(lst)-2):
        la = 0
        while lst[i] < lst[i+1]:
            if la == 0:
                st = lst[i]
            la += 1
            dr = i+1
            i +=1
        else:
            la = 0
        if la > lmax:
            print(la)
            lmax = la
            stanga = st
            dreapta =  dr
    print(lmax)

"""
def main():
    n = int(input('n = '))
    primz_kleiner_als_n(n)
    """
    lst = [1, 2, 3, 3, 3, 4, 5, 6, 7]
    langste_folge(lst)
"""
main()





