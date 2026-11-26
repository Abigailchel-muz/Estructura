"""Expediente 404: búsqueda secuencial de pistas."""
SOSPECHOSOS = [('Luna','llave roja'), ('Atlas','reloj roto'), ('Vega','pluma azul'), ('Nox','mapa lunar'), ('Sol','llave roja')]
def buscar(pista):
    hallados = []
    for i, (nombre, evidencia) in enumerate(SOSPECHOSOS, 1):
        print(f'[{i}/{len(SOSPECHOSOS)}] Revisando expediente de {nombre}: {evidencia}')
        if evidencia == pista.strip().casefold():
            hallados.append(nombre)
            print('  >>> Coincidencia encontrada')
    return hallados

def ejecutar():
    print('\n=== EXPEDIENTE 404 | Agencia de detectives ===')
    print('Pistas disponibles: llave roja, reloj roto, pluma azul, mapa lunar')
    pista = input('Introduce la pista encontrada: ')
    resultado = buscar(pista)
    print('Sospechosos:', ', '.join(resultado) if resultado else 'Sin coincidencias')
    print(f'Expedientes revisados: {len(SOSPECHOSOS)}')
    input('Enter para regresar...')

if __name__ == '__main__':
    ejecutar()
