import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def draw_cube(ax, size):
    # Definisci i vertici del cubo
    vertices = [[0, 0, 0], [size, 0, 0], [size, size, 0], [0, size, 0], [0, 0, size], [size, 0, size], [size, size, size], [0, size, size]]

    # Definisci le facce del cubo
    faces = [[vertices[0], vertices[1], vertices[5], vertices[4]],
             [vertices[7], vertices[6], vertices[2], vertices[3]],
             [vertices[0], vertices[4], vertices[7], vertices[3]],
             [vertices[1], vertices[5], vertices[6], vertices[2]],
             [vertices[4], vertices[5], vertices[6], vertices[7]]]

    # Crea una collezione di facce e aggiungila all'asse
    ax.add_collection3d(Poly3DCollection(faces, edgecolor='black', linewidths=1, alpha=0.1))

def draw_parallelepipedo(ax, base, altezza, lunghezza):
    # Definisci i vertici del parallelepipedo
    vertices = [[0, 0, 0], [base, 0, 0], [base, altezza, 0], [0, altezza, 0], [0, 0, lunghezza], [base, 0, lunghezza], [base, altezza, lunghezza], [0, altezza, lunghezza]]

    # Definisci le facce del parallelepipedo
    faces = [[vertices[0], vertices[1], vertices[5], vertices[4]],
             [vertices[7], vertices[6], vertices[2], vertices[3]],
             [vertices[0], vertices[4], vertices[7], vertices[3]],
             [vertices[1], vertices[5], vertices[6], vertices[2]],
             [vertices[4], vertices[5], vertices[6], vertices[7]]]

    # Crea una collezione di facce e aggiungila all'asse
    ax.add_collection3d(Poly3DCollection(faces, edgecolor='black', linewidths=1, alpha=0.1))

def draw_piramide(ax, base, altezza):
    # Definisci i vertici della piramide
    vertices = [[0, 0, 0], [base, 0, 0], [base, 0, base], [0, 0, base], [base/2, altezza, base/2]]

    # Definisci le facce della piramide
    faces = [[vertices[0], vertices[1], vertices[2], vertices[3]],
             [vertices[0], vertices[1], vertices[4]],
             [vertices[1], vertices[2], vertices[4]],
             [vertices[2], vertices[3], vertices[4]],
             [vertices[3], vertices[0], vertices[4]]]

    # Crea una collezione di facce e aggiungila all'asse
    ax.add_collection3d(Poly3DCollection(faces, edgecolor='black', linewidths=1, alpha=0.1))

def draw_prisma_triangolare(ax, base, altezza):
    # Definisci i vertici del prisma triangolare
    vertices = [[0, 0, 0], [base, 0, 0], [base/2, base * 3**0.5/2, 0], [0, 0, altezza], [base, 0, altezza], [base/2, base * 3**0.5/2, altezza]]

    # Definisci le facce del prisma triangolare
    faces = [[vertices[0], vertices[1], vertices[2]],
             [vertices[3], vertices[4], vertices[5]],
             [vertices[0], vertices[1], vertices[4], vertices[3]],
             [vertices[1], vertices[2], vertices[5], vertices[4]],
             [vertices[2], vertices[0], vertices[3], vertices[5]]]

    # Crea una collezione di facce e aggiungila all'asse
    ax.add_collection3d(Poly3DCollection(faces, edgecolor='black', linewidths=1, alpha=0.1))

def draw_cilindro(ax, raggio, altezza, risoluzione=100):
    # Crea un array di angoli per la circonferenza del cilindro
    theta = np.linspace(0, 2*np.pi, risoluzione)
    
    # Calcola le coordinate x e y dei punti sulla circonferenza
    x = raggio * np.cos(theta)
    y = raggio * np.sin(theta)

    # Costruisci la superficie laterale del cilindro
    ax.plot_surface(np.outer(x, np.ones_like(y)), np.outer(y, np.ones_like(x)), np.outer(np.ones_like(theta), np.linspace(0, altezza, risoluzione)), color='b', alpha=0.5)

    # Aggiungi le basi del cilindro
    ax.plot(x, y, 0, color='b', alpha=0.5)
    ax.plot(x, y, altezza, color='b', alpha=0.5)

def draw_cono(ax, raggio, altezza, risoluzione=100):
    # Calcola le coordinate del cono
    theta = np.linspace(0, 2*np.pi, risoluzione)
    x = raggio * np.cos(theta)
    y = raggio * np.sin(theta)
    z_base = np.zeros_like(x)
    z_apice = np.full_like(x, altezza)

    # Disegna la superficie laterale del cono (triangolo)
    vertices = [list(zip(x, y, z_base))]
    ax.add_collection3d(Poly3DCollection(vertices, facecolors='b', linewidths=1, edgecolors='r', alpha=0.1))

    # Disegna la base del cono (circonferenza)
    ax.plot(x, y, z_base, color='r')

    # Collega la circonferenza al bordo del triangolo
    for i in range(risoluzione):
        ax.plot([x[i], 0], [y[i], 0], [z_base[i], z_apice[i]], color='r')

    # Disegna l'apice del cono
    ax.plot([0], [0], [altezza], marker='o', markersize=5, color='g')

def draw_sfera(ax, raggio, risoluzione=100):
    # Crea un array di angoli per la sfera
    phi = np.linspace(0, np.pi, risoluzione)
    theta = np.linspace(0, 2 * np.pi, risoluzione)

    # Calcola le coordinate x, y, z della sfera
    x = raggio * np.outer(np.sin(phi), np.cos(theta))
    y = raggio * np.outer(np.sin(phi), np.sin(theta))
    z = raggio * np.outer(np.cos(phi), np.ones_like(theta))

    # Disegna la superficie della sfera
    ax.plot_surface(x, y, z, color='r', alpha=0.5)

def draw_toro(ax, raggio_toro, raggio_tubo, risoluzione=100):
    # Crea un array di angoli per il toro
    theta = np.linspace(0, 2 * np.pi, risoluzione)
    phi = np.linspace(0, 2 * np.pi, risoluzione)

    # Calcola le coordinate x, y, z del toro
    theta, phi = np.meshgrid(theta, phi)
    x = (raggio_toro + raggio_tubo * np.cos(phi)) * np.cos(theta)
    y = (raggio_toro + raggio_tubo * np.cos(phi)) * np.sin(theta)
    z = raggio_tubo * np.sin(phi)

    # Disegna la superficie del toro
    ax.plot_surface(x, y, z, color='g', alpha=0.5)
def draw_tronco_cono(ax, raggio_inf, raggio_sup, altezza, risoluzione=100):
    # Crea un array di angoli per il tronco di cono
    theta = np.linspace(0, 2 * np.pi, risoluzione)
    
    # Calcola le coordinate x, y, z del tronco di cono
    x_inf = raggio_inf * np.cos(theta)
    y_inf = raggio_inf * np.sin(theta)
    x_sup = raggio_sup * np.cos(theta)
    y_sup = raggio_sup * np.sin(theta)

    # Costruisci la superficie laterale del tronco di cono
    ax.plot_surface(np.outer(x_inf, np.ones_like(y_inf)), np.outer(y_inf, np.ones_like(x_inf)), np.outer(np.ones_like(theta), np.zeros_like(theta)), color='b', alpha=0.5)
    ax.plot_surface(np.outer(x_sup, np.ones_like(y_sup)), np.outer(y_sup, np.ones_like(x_sup)), np.outer(np.ones_like(theta), np.full_like(theta, altezza)), color='b', alpha=0.5)

    # Connetti la superficie laterale
    for i in range(risoluzione):
        ax.plot([x_inf[i], x_sup[i]], [y_inf[i], y_sup[i]], [0, altezza], color='b')


def draw_trapezio(ax, base_maggiore, base_minore, altezza):
    # Definisci i vertici del trapezio
    vertices = [
        [0, 0, 0],  # Vertice in basso a sinistra
        [base_maggiore, 0, 0],  # Vertice in basso a destra
        [base_minore, altezza, 0],  # Vertice in alto a destra
        [0, altezza, 0],  # Vertice in alto a sinistra
        [0, 0, altezza],  # Vertice in basso a sinistra (superiore)
        [base_maggiore, 0, altezza],  # Vertice in basso a destra (superiore)
        [base_minore, altezza, altezza],  # Vertice in alto a destra (superiore)
        [0, altezza, altezza]  # Vertice in alto a sinistra (superiore)
    ]

    # Definisci le facce del trapezio
    faces = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],  # Base inferiore
        [vertices[4], vertices[5], vertices[6], vertices[7]],  # Base superiore
        [vertices[0], vertices[3], vertices[7], vertices[4]],  # Lato sinistro
        [vertices[1], vertices[5], vertices[6], vertices[2]],  # Lato destro
        [vertices[3], vertices[2], vertices[6], vertices[7]],  # Faccia anteriore
        [vertices[0], vertices[1], vertices[5], vertices[4]]   # Faccia posteriore
    ]

    # Crea una collezione di facce e aggiungila all'asse
    ax.add_collection3d(Poly3DCollection(faces, edgecolor='black', linewidths=1, alpha=0.1))

# Aggiungi l'opzione per disegnare il trapezio nel main
def main():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    print("Benvenuto su GeometryLive.")
    print("Inserisci le grandezze da 0 a 1, quindi dividi per 100, il numero che ti serve.")
    print("Seleziona una figura 3D da disegnare:")
    print("1. Cubo")
    print("2. Parallelepipedo")
    print("3. Piramide a Base Rettangolare")
    print("4. Prisma a Base Triangolare")
    print("5. Cilindro")
    print("6. Cono")
    print("7. Sfera")
    print("8. Toro")
    print("9. Tronco di cono")
    print("10. Prisma Trapezoidale")

    scelta = int(input("Inserisci il numero corrispondente alla tua scelta: "))

    if scelta == 1:
        size = float(input("Inserisci la lunghezza del lato del cubo: "))
        draw_cube(ax, size)
    elif scelta == 2:
        base = float(input("Inserisci la lunghezza della base del parallelepipedo: "))
        altezza = float(input("Inserisci l'altezza del parallelepipedo: "))
        lunghezza = float(input("Inserisci la lunghezza del parallelepipedo: "))
        draw_parallelepipedo(ax, base, altezza, lunghezza)
    elif scelta == 3:
        base = float(input("Inserisci la lunghezza della base della piramide: "))
        altezza = float(input("Inserisci l'altezza della piramide: "))
        draw_piramide(ax, base, altezza)
    elif scelta == 4:
        base = float(input("Inserisci la lunghezza della base del prisma triangolare: "))
        altezza = float(input("Inserisci l'altezza del prisma triangolare: "))
        draw_prisma_triangolare(ax, base, altezza)
    elif scelta == 5:
        raggio = float(input("Inserisci il raggio del cilindro: "))
        altezza = float(input("Inserisci l'altezza del cilindro: "))
        draw_cilindro(ax, raggio, altezza)
    elif scelta == 6:
        raggio = float(input("Inserisci il raggio del cono: "))
        altezza = float(input("Inserisci l'altezza del cono: "))
        draw_cono(ax, raggio, altezza)
    elif scelta == 7:
        raggio_sfera = float(input("Inserisci il raggio della sfera: "))
        draw_sfera(ax, raggio_sfera)
    elif scelta == 8:
        raggio_toro = float(input("Inserisci il raggio del toro: "))
        raggio_tubo = float(input("Inserisci il raggio del tubo del toro: "))
        draw_toro(ax, raggio_toro, raggio_tubo)
    elif scelta == 9:
        raggio_inf = float(input("Inserisci il raggio inferiore del tronco di cono: "))
        raggio_sup = float(input("Inserisci il raggio superiore del tronco di cono: "))
        altezza_tronco_cono = float(input("Inserisci l'altezza del tronco di cono: "))
        draw_tronco_cono(ax, raggio_inf, raggio_sup, altezza_tronco_cono)
    elif scelta == 10:
        base_maggiore = float(input("Inserisci la lunghezza della base maggiore del trapezio: "))
        base_minore = float(input("Inserisci la lunghezza della base minore del trapezio: "))
        altezza = float(input("Inserisci l'altezza del trapezio: "))
        draw_trapezio(ax, base_maggiore, base_minore, altezza)
    else:
        print("Scelta non valida. Inserisci un numero valido.")

    plt.show(block=True)

if __name__ == "__main__":
    main()


