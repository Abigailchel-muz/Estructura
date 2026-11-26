"""Festival Eclipse: tabla hash con encadenamiento."""
TAM = 7
class Festival:
    def __init__(self):
        self.tabla = [[] for _ in range(TAM)]
        for codigo, nombre in [('A12','Mia'),('B11','Leo'),('C24','Noa'),('VIP9','Ari')]:
            self.tabla[self.indice(codigo)].append([codigo,nombre,False])
    def indice(self, codigo):
        return sum(ord(c) for c in codigo) % TAM
    def validar(self, codigo):
        codigo = codigo.strip().upper()
        indice = self.indice(codigo)
        print(f'Escáner: suma ASCII = {sum(map(ord,codigo))}; cubeta = {indice}')
        for boleto in self.tabla[indice]:
            print('  Comparando con', boleto[0])
            if boleto[0] == codigo:
                if boleto[2]:
                    return 'Acceso rechazado: boleto ya utilizado.'
                boleto[2] = True
                return f'Acceso autorizado. Bienvenido/a, {boleto[1]}.'
        return 'Acceso rechazado: código inexistente.'

def ejecutar():
    festival = Festival()
    while True:
        print('\n=== FESTIVAL ECLIPSE | Control de acceso ===')
        print('1. Escanear boleto  2. Ver mapa hash  0. Regresar')
        opcion = input('Opción: ')
        if opcion == '0': return
        if opcion == '1':
            print('Boletos de prueba: A12, B11, C24, VIP9')
            print(festival.validar(input('Código: ')))
        elif opcion == '2':
            for i, cubeta in enumerate(festival.tabla):
                print(f'[{i}]', ' -> '.join(b[0]+(' (usado)' if b[2] else '') for b in cubeta) or 'Vacía')
        else: print('Opción inválida.')

if __name__ == '__main__':
    ejecutar()
