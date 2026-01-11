def calcular_ahorro_total(monto_mensual, numero_meses):
    ahorro_total = monto_mensual * numero_meses
    return ahorro_total


def verificar_meta(ahorro_total, meta_ahorro):
    meta_alcanzada = ahorro_total >= meta_ahorro
    return meta_alcanzada


def main():
    nombre_usuario = input("Ingrese su nombre: ")
    monto_mensual = float(input("Ingrese el monto que ahorra cada mes: "))
    numero_meses = int(input("Ingrese la cantidad de meses que ha ahorrado: "))
    meta_ahorro = float(input("Ingrese su meta de ahorro: "))

    ahorro_total = calcular_ahorro_total(monto_mensual, numero_meses)
    meta_alcanzada = verificar_meta(ahorro_total, meta_ahorro)

    print("\n--- Resumen de Ahorro ---")
    print(f"Usuario: {nombre_usuario}")
    print(f"Ahorro total: ${ahorro_total:.2f}")

    if meta_alcanzada:
        print("¡Felicidades! Has alcanzado tu meta de ahorro ")
    else:
        print("Aún no alcanzas tu meta. Sigue ahorrando ")


if __name__ == "__main__":
    main()
