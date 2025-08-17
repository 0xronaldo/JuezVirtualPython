

def es_bisiesto(año):
    if año % 4 != 0:
        return False
    if año % 100 == 0 and año % 400 != 0:
        return False
    return True
def dias_en_mes(mes, año):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 29 if es_bisiesto(año) else 28
    else:
        return 0
def validar_fecha(dia, mes, año):
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > dias_en_mes(mes, año):
        return False
    return True


if __name__ == "__main__":
    n = int(input())
    exac = []
    for _ in range(n):
        dia, mes, año = map(int, input().split())
        if validar_fecha(dia, mes, año):
            exac.append("Correcta")
        else:
            exac.append("Incorrecta")

        #print(resultado)
    for _ in exac:
        print( _ )
    