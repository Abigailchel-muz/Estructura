import secuencial
import binaria
import hash as festival

def main():
    opciones = {'1': secuencial.ejecutar, '2': binaria.ejecutar, '3': festival.ejecutar}
    while True:
        print('\n' + '='*48)
        print('       SEARCHVERSE | Laboratorio de búsqueda')
        print('='*48)
        print('1. Expediente 404   [Secuencial]')
        print('2. Órbita perdida   [Binaria]')
        print('3. Festival Eclipse [Hash]')
        print('0. Salir')
        opcion = input('Selecciona una misión: ').strip()
        if opcion == '0':
            print('Misiones finalizadas. ¡Hasta pronto!')
            break
        if opcion in opciones: opciones[opcion]()
        else: print('Opción inválida. Intenta nuevamente.')

if __name__ == '__main__': main()
