#i matrix[a][b] så är a rader(>) och b kolummner(v)
#len(M) antal rader
#len(M[a]) antal kolumner


def transpose(M):
    n = 0
    m = 0
    new_matrix = []
    for n in range(0 , len(M)):
        if len(M[n]) != len(M[0]):          #Kollar så att alla rader är lika långa
            return "Not a matrice"
    if M == []:                             #Ifall det är en tom matris går det inte att göra något med den
        return M
    for n in range(0, len(M[n])):           
        new_row = []
        for m in range(0, len(M)):
            new_row.append(M[m][n])         #Skiftar så att rad-kolumnvärde blir kolumn-radvärde i den nya matrisen
        new_matrix.append(new_row)
    return new_matrix

def powers(list, power1, power2):
    new_matrix = []
    for n in range(len(list)):
        new_list = []
        for m in range(power1, power2 + 1): #Tar alla värden mellan power1 och power2
             new_list.append(list[n]**m)    
        new_matrix.append(new_list)
    return new_matrix

def matmul(M1, M2):
    new_matrix = []
    if M1 == [] or M2 == []:                #Ifall någon av "matriserna" är tomma så fungerar det inte
        return []                           
    elif len(M1[0]) == len(M2):             #Kolumnera i M1 måste vara lika långa som raderna i M2
        for n in range(len(M1)):
            new_row = []
            for m in range(len(M2[0])):
                value = 0
                for p in range(len(M2)):                    #Kan ha antingen len(M2) eller len(M1[0]), eftersom de är samma
                    value = value + M1[n][p] * M2[p][m]     #Räknar ut värdet på positionen
                new_row.append(value)
            new_matrix.append(new_row)      #Lägger till de nya värderna i den rya raden och sedan raden in i matrisen
        return new_matrix
    else:                                   #Kommer den hit så matchar inte matriserna
        return "Wrong size on matrices"

def invert(M):
    if M == []:                             #Ifall "matrisen" är tom så fungerar det inte
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
        return "It's not a 2x2 matrice"

def loadtxt(file):
    new_matrix = []
    file_open = open(file)                  #Öppnar filen, läser den och sparar den i lines
    lines = file_open.readlines()
    file_open.close()
    for line in lines:
        line = line.replace("\n", "")       #Tar bort alla \n i texten
        list = line.split("\t")             #Splittar den till listor 
        for n in range(0,2):
            list[n] = float(list[n])        #Gör om allt från strings till decimaltal
        new_matrix.append(list)
    return new_matrix
