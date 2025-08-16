num = int(input())
casos = []

for _ in range(num):
    horas, salario = map(float, input().split())
    if horas <= 40:
        pago_total = horas * salario
    else:
        pago_regular = 40 * salario
        horas_extra = horas - 40
        pago_extra = horas_extra * salario * 1.5
        pago_total = pago_regular + pago_extra
    pagofinal = f"{pago_total:.2f}"
    casos.append(pagofinal) 

for _ in casos:
    print(_, end='\n')
