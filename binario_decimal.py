def bin2dec(bin):

    bin2 = bin[::-1]

    bina = []

    suma = 0

    for bi in bin2:

        bina.append(bi)

    for i in range(0,len(bin2)):

        if bina[i] != "0":

            suma += (2**i)

    return suma

def dec2bin(dec):

    rdo = ""

    while dec >= 2:
        
        resto = dec % 2
        dec = dec // 2

        div2 = str(resto)

        rdo += div2

    if dec == 1:
        rdo += "1"
    else:
        rdo += "0"   

    if len(rdo)<8:

        cant = 8-len(rdo)
        
        rdo += "0"*cant

    rdo2 = rdo[::-1]

    return rdo2      
    


