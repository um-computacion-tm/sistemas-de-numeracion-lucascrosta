#octal a decimal
def oct2dec(oct):

    oct = str(oct)

    oct = oct[::-1]

    octales = []

    suma = 0

    for o in oct:

        octales.append(o)

    for i in range(0,len(octales)):

        octales[i] = int(octales[i])

        suma += (octales[i])*(8**i)

    return suma

#octal a hexadecimal
def oct2hex(oct):

    bin = ""

    oct = str(oct)

    #primero pasamos de octal a binario
    for o in oct:
        if o == "0":
            bin += "000"
        elif o == "1":
            bin += "001"
        elif o == "2":
            bin += "010"
        elif o == "3":
            bin += "011"
        elif o == "4":
            bin += "100"
        elif o == "5":
            bin += "101"
        elif o == "6":
            bin += "110"
        elif o == "7":
            bin += "111"
    
    #ahora de binario a hexadecimal
    bin = bin[::-1]

    while True:
        if (len(bin)%4) != 0:
            bin += "0"
        else:
            break

    bin = bin[::-1]

    bina = []
    bin3 = ""

    cont = 0

    long = int(len(bin)/4)

    for i in range(0,long):
        for b in bin:
            bin3 += b
            cont += 1
            bin = bin.replace(b,"",1)
            if cont == 4:
                cont = 0
                break
        bina.append(bin3)
        bin3 = ""

    hex = ""

    if bina[0] == "0000":
        bina.remove("0000")


    for i in bina:

        if i == "0000":
            hex += "0"
        elif i == "0001":
            hex += "1"
        elif i == "0010":
            hex += "2" 
        elif i == "0011":
            hex += "3"
        elif i == "0100":
            hex += "4"
        elif i == "0101":
            hex += "5" 
        elif i == "0110":
            hex += "6"
        elif i == "0111":
            hex += "7"
        elif i == "1000":
            hex += "8"
        elif i == "1001":
            hex += "9"
        elif i == "1010":
            hex += "A"
        elif i == "1011":
            hex += "B"
        elif i == "1100":
            hex += "C"
        elif i == "1101":
            hex += "D"
        elif i == "1110":
            hex += "E"
        elif i == "1111":
            hex += "F"

    return hex

#octal a binario
def oct2bin(oct):

    bin = ""

    oct = str(oct)

    for o in oct:
        if o == "0":
            bin += "000"
        elif o == "1":
            bin += "001"
        elif o == "2":
            bin += "010"
        elif o == "3":
            bin += "011"
        elif o == "4":
            bin += "100"
        elif o == "5":
            bin += "101"
        elif o == "6":
            bin += "110"
        elif o == "7":
            bin += "111"

    return bin