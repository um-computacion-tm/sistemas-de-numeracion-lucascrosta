#decimal a hexadecimal
def dec2hex(dec):

    rdo = ""

    if dec < 16:
        
        if dec == 10:
            rdo += "A"
        elif dec == 11:
            rdo += "B"
        elif dec == 12:
            rdo += "C"
        elif dec == 13:
            rdo += "D"
        elif dec == 14:
            rdo += "E"
        elif dec == 15:
            rdo += "F"
        else:
            rdo += str(dec)
    else:

        while dec >= 16:

            resto = dec % 16
            dec = dec // 16

            if resto == 10:
                rdo += "A"
            elif resto == 11:
                rdo += "B"
            elif resto == 12:
                rdo += "C"
            elif resto == 13:
                rdo += "D"
            elif resto == 14:
                rdo += "E"
            elif resto == 15:
                rdo += "F"
            else:
                rdo += str(resto)

        rdo= rdo + str(dec)

        rdo = rdo[::-1]

    return rdo

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
