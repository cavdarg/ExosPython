#ex6
def tri_bulles(nbr):
    n = len(nbr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if nbr[j] > nbr[j + 1]:
                nbr[j], nbr[j + 1] = nbr[j + 1], nbr[j]

nbr = [5, 4, 3, 2, 1]
tri_bulles(nbr)
print(nbr)


