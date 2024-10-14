import math

def volume_cubo(lato):
    return lato ** 3

def area_cubo(lato):
    return 6 * lato ** 2

def volume_parallelepipedo(base1, base2, altezza):
    return base1 * base2 * altezza

def area_parallelepipedo(base1, base2, altezza):
    area_base = base1 * base2
    area_laterale = 2 * (base1 * altezza + base2 * altezza)
    return 2 * area_base + area_laterale

def volume_piramide(base_larghezza, base_lunghezza, altezza):
    return (1/3) * base_larghezza * base_lunghezza * altezza

def area_piramide(base_larghezza, base_lunghezza, altezza):
    area_base = base_larghezza * base_lunghezza
    # Calcolare l'area delle facce laterali
    slant_height = math.sqrt((base_larghezza / 2) ** 2 + altezza ** 2)
    area_laterale = 2 * (base_larghezza * slant_height / 2) + 2 * (base_lunghezza * slant_height / 2)
    return area_base + area_laterale

def volume_prisma_triangolare(base, altezza):
    return (1/2) * base * altezza

def area_prisma_triangolare(base, lato1, lato2, lato3, altezza):
    area_base = (1/2) * base * altezza
    perimetro_base = lato1 + lato2 + lato3
    area_laterale = perimetro_base * altezza
    return 2 * area_base + area_laterale

def volume_cilindro(raggio, altezza):
    return math.pi * raggio ** 2 * altezza

def area_cilindro(raggio, altezza):
    area_base = math.pi * raggio ** 2
    area_laterale = 2 * math.pi * raggio * altezza
    return 2 * area_base + area_laterale

def volume_cono(raggio, altezza):
    return (1/3) * math.pi * raggio ** 2 * altezza

def area_cono(raggio, altezza):
    generatrice = math.sqrt(raggio ** 2 + altezza ** 2)
    area_base = math.pi * raggio ** 2
    area_laterale = math.pi * raggio * generatrice
    return area_base + area_laterale

def volume_sfera(raggio):
    return (4/3) * math.pi * raggio ** 3

def area_sfera(raggio):
    return 4 * math.pi * raggio ** 2

def volume_toro(raggio_interno, raggio_esterno):
    return 2 * math.pi ** 2 * raggio_interno * raggio_esterno ** 2

def area_toro(raggio_interno, raggio_esterno):
    return 4 * math.pi ** 2 * raggio_interno * raggio_esterno

def volume_tronco_cono(raggio_base_superiore, raggio_base_inferiore, altezza):
    return (1/3) * math.pi * altezza * (raggio_base_superiore ** 2 + raggio_base_inferiore ** 2 + raggio_base_superiore * raggio_base_inferiore)

def area_tronco_cono(raggio_base_superiore, raggio_base_inferiore, altezza):
    generatrice = math.sqrt((raggio_base_inferiore - raggio_base_superiore) ** 2 + altezza ** 2)
    area_base_superiore = math.pi * raggio_base_superiore ** 2
    area_base_inferiore = math.pi * raggio_base_inferiore ** 2
    area_laterale = math.pi * (raggio_base_superiore + raggio_base_inferiore) * generatrice
    return area_base_superiore + area_base_inferiore + area_laterale

def area_base_trapezio(base_maggiore, base_minore, altezza_trapezio):
    return (base_maggiore + base_minore) * altezza_trapezio / 2

def volume_prisma_trapezoidale(base_maggiore, base_minore, altezza_trapezio, altezza_prisma):
    area_base = area_base_trapezio(base_maggiore, base_minore, altezza_trapezio)
    return area_base * altezza_prisma

def area_superficie_prisma_trapezoidale(base_maggiore, base_minore, altezza_trapezio, altezza_prisma):
    area_base = area_base_trapezio(base_maggiore, base_minore, altezza_trapezio)
    area_laterale = (base_maggiore + base_minore) * altezza_prisma
    return area_base + 2 * area_laterale

# Aggiornamento nel main
def main():
    while True:
        print("\nMenu:")
        print("1. Cubo")
        print("2. Parallelepipedo")
        print("3. Piramide a Base Rettangolare")
        print("4. Prisma a Base Triangolare")
        print("5. Cilindro")
        print("6. Cono")
        print("7. Sfera")
        print("8. Toro")
        print("9. Tronco di Cono")
        print("10. Prisma Trapezoidale")
        print("0. Esci")

        scelta = input("Scegli una figura (inserisci il numero corrispondente): ")

        if scelta == '0':
            break
        elif scelta == '1':
            lato = float(input("Inserisci il lato del cubo: "))
            print("Volume:", volume_cubo(lato))
            print("Area:", area_cubo(lato))
        elif scelta == '2':
            base1 = float(input("Inserisci la lunghezza della prima base del parallelepipedo: "))
            base2 = float(input("Inserisci la lunghezza della seconda base del parallelepipedo: "))
            altezza = float(input("Inserisci l'altezza del parallelepipedo: "))
            print("Volume:", volume_parallelepipedo(base1, base2, altezza))
            print("Area:", area_parallelepipedo(base1, base2, altezza))
        elif scelta == '3':
            base_larghezza = float(input("Inserisci la larghezza della base della piramide: "))
            base_lunghezza = float(input("Inserisci la lunghezza della base della piramide: "))
            altezza = float(input("Inserisci l'altezza della piramide: "))
            print("Volume:", volume_piramide(base_larghezza, base_lunghezza, altezza))
            print("Area:", area_piramide(base_larghezza, base_lunghezza, altezza))
        elif scelta == '4':
            base = float(input("Inserisci la lunghezza della base del prisma triangolare: "))
            altezza = float(input("Inserisci l'altezza del prisma triangolare: "))
            lato1 = float(input("Inserisci la lunghezza del primo lato del triangolo: "))
            lato2 = float(input("Inserisci la lunghezza del secondo lato del triangolo: "))
            lato3 = float(input("Inserisci la lunghezza del terzo lato del triangolo: "))
            print("Volume:", volume_prisma_triangolare(base, altezza))
            print("Area:", area_prisma_triangolare(base, lato1, lato2, lato3, altezza))
        elif scelta == '5':
            raggio = float(input("Inserisci il raggio del cilindro: "))
            altezza = float(input("Inserisci l'altezza del cilindro: "))
            print("Volume:", volume_cilindro(raggio, altezza))
            print("Area:", area_cilindro(raggio, altezza))
        elif scelta == '6':
            raggio = float(input("Inserisci il raggio del cono: "))
            altezza = float(input("Inserisci l'altezza del cono: "))
            print("Volume:", volume_cono(raggio, altezza))
            print("Area:", area_cono(raggio, altezza))
        elif scelta == '7':
            raggio = float(input("Inserisci il raggio della sfera: "))
            print("Volume:", volume_sfera(raggio))
            print("Area:", area_sfera(raggio))
        elif scelta == '8':
            raggio_interno = float(input("Inserisci il raggio interno del toro: "))
            raggio_esterno = float(input("Inserisci il raggio esterno del toro: "))
            print("Volume:", volume_toro(raggio_interno, raggio_esterno))
            print("Area:", area_toro(raggio_interno, raggio_esterno))
        elif scelta == '9':
            raggio_base_superiore = float(input("Inserisci il raggio della base superiore del tronco di cono: "))
            raggio_base_inferiore = float(input("Inserisci il raggio della base inferiore del tronco di cono: "))
            altezza = float(input("Inserisci l'altezza del tronco di cono: "))
            print("Volume:", volume_tronco_cono(raggio_base_superiore, raggio_base_inferiore, altezza))
            print("Area:", area_tronco_cono(raggio_base_superiore, raggio_base_inferiore, altezza))
        elif scelta == '10':  # Aggiunto il blocco per il prisma trapezoidale
            base_maggiore = float(input("Inserisci la lunghezza della base maggiore del trapezio: "))
            base_minore = float(input("Inserisci la lunghezza della base minore del trapezio: "))
            altezza_trapezio = float(input("Inserisci l'altezza del trapezio: "))
            altezza_prisma = float(input("Inserisci l'altezza del prisma trapezoidale: "))
            print("Volume:", volume_prisma_trapezoidale(base_maggiore, base_minore, altezza_trapezio, altezza_prisma))
            print("Area Superficiale:", area_superficie_prisma_trapezoidale(base_maggiore, base_minore, altezza_trapezio, altezza_prisma))
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()
