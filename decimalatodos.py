#decimal a binario
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