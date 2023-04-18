# Validar rut
def validar_rut(rut):
    """
    Valida si un RUT es válido.
    """
    rut = rut.upper().replace(".", "").replace("-", "")
    rut = rut[:-1]
    factor = 2
    suma = 0
    for i in range(len(rut)-1, -1, -1):
        suma += int(rut[i]) * factor
        factor += 1
        if factor > 7:
            factor = 2
    dv = 11 - (suma % 11)
    if dv == 10:
        dv = "K"
    elif dv == 11:
        dv = "0"
    else:
        dv = str(dv)
    return dv == rut[-1]

def getPrev(prevNum):
    valor = ""
    match prevNum:
        case 1:
           valor = "Fondo Nacional de Salud(Fonasa)"
        case 2:
           valor = "Isalud Isapre De Codelco"
        case 3:
           valor = "Isapre Banmédica"
        case 4:
           valor = "Isapre Colmena"
        case 5:
           valor = "Isapre Consalud"
        case 6:
           valor = "Isapre Cruz Blanca"
        case 7:
           valor = "Isapre Cruz Del Norte"
        case 8:
           valor = "Isapre Fundación Banco Estado"
        case 9:
           valor = "Isapre Nueva Másvida"
        case 10:
           valor = "Isapre Vida Tres"
        case 10:
           valor = "Particular"
    return valor
