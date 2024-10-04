#i matrix[a][b] så är a rader(>) och b kolummner(v)
#len(M) antal rader
#len(M[a]) antal kolumner


def transpose(M):
    n = 0
    m = 0
    new_matrix = []
    for n in range(0 , len(M)):
        if len(M[n]) != len(M[0]):
            return "Not a matrice"
    if M == []:
        return M
    for n in range(0, len(M[n])):
        new_row = []
        for m in range(0, len(M)):
            new_row.append(M[m][n])
        new_matrix.append(new_row)
    return new_matrix

def powers(list, power1, power2):
    new_matrix = []
    for n in range(len(list)):
        new_list = []
        for m in range(power1, power2 + 1):
             new_list.append(list[n]**m)
        new_matrix.append(new_list)
    return new_matrix

def matmul(M1, M2):
    new_matrix = []
    if M1 == [] or M2 == []:
        return []
    elif len(M1[0]) == len(M2):
        for n in range(len(M1)):
            new_row = []
            for m in range(len(M2[0])):
                value = 0
                for p in range(len(M2)):
                    value = value + M1[n][p] * M2[p][m] 
                new_row.append(value)
            new_matrix.append(new_row)
        return new_matrix
    else:
        return "Wrong size on matrices"

def invert(M):
    if M == []:
        return M
    elif len(M) == 2 and len(M[0]) == 2:
        det = M[0][0] * M[1][1] - M[1][0] * M[0][1]
        new_matrix = []
        new_row1 = [M[1][1]/det, -M[0][1]/det]
        new_row2 = [-M[1][0]/det, M[0][0]/det]
        new_matrix.append(new_row1)
        new_matrix.append(new_row2)
        return new_matrix
    else:
        print("Det är inte en 2x2 matris")

def loadtxt(file):
    new_matrix = []
    file_open = open(file)
    lines = file_open.readlines()
    file_open.close()
    for line in lines:
        line = line.replace("\n", "")
        list = line.split("\t")
        for n in range(0,2):
            list[n] = float(list[n])
        new_matrix.append(list)
    return new_matrix
