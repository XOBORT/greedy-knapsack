
P = 100
pack = [[1, 1, 5],
        [2, 29, 14],
        [3, 23, 14],
        [4, 16, 22],
        [5, 2, 30],
        [6, 17, 8],
        [7, 8, 17],
        [8, 1, 28],
        [9, 17, 19],
        [10, 21, 12],
        [11, 28, 25],
        [12, 16, 10],
        [13, 18, 16],
        [14, 27, 22],
        [15, 6, 10]]

#
def greedy_algorithm():
    Si = []
    Cmax = 0
    Pmax = 0
    pack.sort(key=lambda x: x[2])
    pack.sort(key=lambda x: x[1], reverse=True)
    for i in range(0, L):
        if Pmax <= P:
            pop = Pmax + pack[i][2]
            if pop > P:
                continue
            else:
                Si.insert(i, pack[i][0])
                Pmax += pack[i][2]
                Cmax += pack[i][1]
                print(f"Step № {i+1}")
                print(f"    № {pack[i][0]}, Price {pack[i][1]}, Weight {pack[i][2]}")
                print(f"    Cmax = {Cmax}, Pmax {Pmax}")
    return Si, Cmax, Pmax
#

L = len(pack)
#
print("№ | Price | Weight")
for i in range(0, L):
    print(pack[i])
print(f"Max weight = {P}")
print("####################################################################################")
test = greedy_algorithm()
print("####################################################################################")
print(f"№ items {test[0]}, Cmax = {test[1]}, Pmax {test[2]}")
#
