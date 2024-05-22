#9
for i in range(1, 10):
    motif = '[' * i + ' ' + ']' * i
    # centrer le motif
    print(motif.center(10 * 3))