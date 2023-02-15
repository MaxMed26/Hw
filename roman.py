def int_to_roman(a):
    result = ''
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
        'M CM D CD C XC L XL X IX V IV I'.split()):
        result += a // arabic * roman
        a %= arabic
    return result

def roman_to_int(t):
    table = [['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
    returnint = 0
    for pair in table:
        continueyes = True

        while continueyes:
            if len(t) >= len(pair[0]):

                if t[0:len(pair[0])] == pair[0]:
                    returnint += pair[1]
                    t = t[len(pair[0]):]

                else:
                    continueyes = False
            else:
                continueyes = False

    return returnint
