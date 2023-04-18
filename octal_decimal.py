#decimal a octal
def dec2oct(dec):

    rdo = ""

    while dec >= 8:
        
        resto = dec % 8
        dec = dec // 8

        rdo += str(resto)
    
    rdo= rdo + str(dec)

    rdo = int(rdo[::-1])

    return rdo

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
