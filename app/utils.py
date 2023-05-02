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
