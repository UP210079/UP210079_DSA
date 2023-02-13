def calcular_boletos(cantidad):
    precio_boleto = 1
    boletos = 0
    while cantidad >= precio_boleto:
        cantidad -= precio_boleto
        boletos += 1
        precio_boleto += 1
    return boletos

cantidad_dinero = int(input("¿Cuánto dinero tienes?: "))
boletos = calcular_boletos(cantidad_dinero)
print(f"Con ${cantidad_dinero}, se pueden comprar {boletos} boletos.")
