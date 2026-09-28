def pasos_para_limpiar(nivel_desorden: int, objetos_anidados: int) -> int:
    """
    Calcula los pasos totales para limpiar una habitación con cajas dentro de cajas.
    - nivel_desorden: Cuán profundo están guardadas las cosas (cuántas cajas/muebles hay una dentro de otra).
    - objetos_anidados: Cantidad de ítems o sub-cajas por revisar.
    """
    # Caso base 1: Si no hay cajas ni niveles, solo limpias el objeto directamente (+1 paso)
    if nivel_desorden == 0:
        return objetos_anidados + 1

    # Caso base 2: Si el nivel es profundo pero no quedan objetos en este sub-nivel,
    # pasas al nivel anterior revisando el contenedor principal
    if nivel_desorden > 0 and objetos_anidados == 0:
        return pasos_para_limpiar(nivel_desorden - 1, 1)

    # Caso de Recursividad Anidada:
    # Para saber cuántas acciones requiere el nivel superior (llamada externa),
    # primero necesitas el RESULTADO de cuántos pasos tomó vaciar el contenedor interno (llamada interna).
    if nivel_desorden > 0 and objetos_anidados > 0:
        return pasos_para_limpiar(
            nivel_desorden - 1,
            pasos_para_limpiar(nivel_desorden, objetos_anidados - 1)  # <- Llamada anidada
        )


# --- Ejemplo cotidiano ---
if __name__ == "__main__":
    print("--- Calculadora de Pasos para Limpieza Doméstica ---\n")

    # Ejemplo 1: Cajón del escritorio (1 cajón con 2 compartimentos adentro)
    pasos_cajon = pasos_para_limpiar(1, 2)
    print(f"Pasos para organizar un cajón con 2 compartimentos: {pasos_cajon}")

    # Ejemplo 2: Armario (2 niveles de cajas, 2 cajas por nivel)
    pasos_armario = pasos_para_limpiar(2, 2)
    print(f"Pasos para organizar el armario principal: {pasos_armario}")

    # Ejemplo 3: Bodega/Trastero (3 niveles de cajas de mudanza)
    pasos_bodega = pasos_para_limpiar(3, 1)
    print(f"Pasos para organizar una bodega guardada por años: {pasos_bodega}")