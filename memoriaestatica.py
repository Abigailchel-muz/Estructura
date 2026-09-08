def main():
    calificaciones = [0] * 5

    for i in range(5):
        calificaciones[i] = int(input(f"Captura la calificacion {i+1}: "))

    print(calificaciones)

if __name__ == "__main__":
    main()