"""Órbita perdida: búsqueda binaria de planetas ficticios."""
PLANETAS = [(101,'Aurora'),(205,'Nébula'),(310,'Ícaro'),(420,'Kepler'),(530,'Titania'),(640,'Zenit'),(750,'Nova')]
def buscar(codigo):
    izquierda, derecha = 0, len(PLANETAS)-1
    pasos = 0
    while izquierda <= derecha:
        medio = (izquierda + derecha)//2
        actual, nombre = PLANETAS[medio]
        pasos += 1
        print(f'Radar {pasos}: sector {izquierda+1} a {derecha+1} | señal central {actual}')
        if actual == codigo:
            return nombre, pasos
        if actual < codigo:
            print('  >>> Descartando mitad inferior')
            izquierda = medio + 1
        else:
            print('  >>> Descartando mitad superior')
            derecha = medio - 1
    return None, pasos

def ejecutar():
    print('\n=== ÓRBITA PERDIDA | Radar espacial ===')
    print('Señales registradas:', ' | '.join(str(c) for c,_ in PLANETAS))
    try:
        codigo = int(input('Código de señal a localizar: '))
    except ValueError:
        print('Introduce un código numérico válido.')
        return
    nombre, pasos = buscar(codigo)
    print('Destino:', nombre or 'Señal desconocida', '| Comparaciones:', pasos)
    input('Enter para regresar...')

if __name__ == '__main__':
    ejecutar()
