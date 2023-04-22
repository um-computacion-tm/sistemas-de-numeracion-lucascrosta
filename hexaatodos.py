#hexadecimal a decimal
def hex2dec(hex):

    hex = hex[::-1]

    hexadec = []

    suma = 0

    for h in hex:

        hexadec.append(h)

    for i in range(0,len(hexadec)):

        if hexadec[i] == "A":
            suma += 10*(16**i)
        elif hexadec[i] == "B":
            suma += 11*(16**i)
        elif hexadec[i] == "C":
            suma += 12*(16**i)
        elif hexadec[i] == "D":
            suma += 13*(16**i)
        elif hexadec[i] == "E":
            suma += 14*(16**i)
        elif hexadec[i] == "F":
            suma += 15*(16**i)
        else:
            hexadec[i] = int(hexadec[i])
            suma += (hexadec[i])*(16**i)

    return suma

#hexadecimal a octal
def hex2oct(hex):

    #primero pasamos de hexadecimal a binario

    bin = ""

    for h in hex:
        if h == "0":
            bin += "0000"
        elif h == "1":
            bin += "0001"
        elif h == "2":
            bin += "0010"
        elif h == "3":
            bin += "0011"
        elif h == "4":
            bin += "0100"
        elif h == "5":
            bin += "0101"
        elif h == "6":
            bin += "0110"
        elif h == "7":
            bin += "0111"
        elif h == "8":
            bin += "1000"
        elif h == "9":
            bin += "1001"
        elif h == "A":
            bin += "1010"
        elif h == "B":
            bin += "1011"
        elif h == "C":
            bin += "1100"
        elif h == "D":
            bin += "1101"
        elif h == "E":
            bin += "1110"
        elif h == "F":
            bin += "1111"

    #pasamos de binario a octal
    bin = bin[::-1]

    while True:
        if (len(bin)%3) != 0:
            bin += "0"
        else:
            break

    bin = bin[::-1]

    bina = []
    bin3 = ""

    cont = 0

    long = int(len(bin)/3)

    for i in range(0,long):
        for b in bin:
            bin3 += b
            cont += 1
            bin = bin.replace(b,"",1)
            if cont == 3:
                cont = 0
                break
        bina.append(bin3)
        bin3 = ""

    oct = ""

    for i in bina:

        if i == "000":
            oct += "0"
        elif i == "001":
            oct += "1"
        elif i == "010":
            oct += "2" 
        elif i == "011":
            oct += "3"
        elif i == "100":
            oct += "4"
        elif i == "101":
            oct += "5" 
        elif i == "110":
            oct += "6"
        elif i == "111":
            oct += "7"

    return int(oct)

#hexadecimal a binario
def hex2bin(hex):

    bin = ""

    for h in hex:
        if h == "0":
            bin += "0000"
        elif h == "1":
            bin += "0001"
        elif h == "2":
            bin += "0010"
        elif h == "3":
            bin += "0011"
        elif h == "4":
            bin += "0100"
        elif h == "5":
            bin += "0101"
        elif h == "6":
            bin += "0110"
        elif h == "7":
            bin += "0111"
        elif h == "8":
            bin += "1000"
        elif h == "9":
            bin += "1001"
        elif h == "A":
            bin += "1010"
        elif h == "B":
            bin += "1011"
        elif h == "C":
            bin += "1100"
        elif h == "D":
            bin += "1101"
        elif h == "E":
            bin += "1110"
        elif h == "F":
            bin += "1111"

    return bin

