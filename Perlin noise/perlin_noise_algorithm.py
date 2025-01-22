import numpy as np

def fade(f):
    """funkcja wygładzająca"""
    return 6 * f**5 - 15 * f**4 + 10 * f**3

def lerp(a, b, x):
    """interpolacja liniowa"""
    return a + x * (b - a)

def gradient(h, x, y):
    """obliczanie wektorów gradientu i iloczynu skalarnego"""
    vectors = np.array([[0, 1], [0, -1], [1, 0], [-1, 0]])
    g = vectors[h % 4]
    return g[..., 0] * x + g[..., 1] * y

def perlin(x, y, seed=0):
    # 1. Tworzenie pseudolosowej tabeli permutacji
    np.random.seed(seed)
    ptable = np.arange(256, dtype=int)
    np.random.shuffle(ptable)
    ptable = np.stack([ptable, ptable]).flatten()

    # 2. Wyznaczenie punktów (narożników) siatki
    xi, yi = x.astype(int) % 256, y.astype(int) % 256
    xg, yg = x - xi, y - yi # współrzędne wektora odległości

    # 3. Wygładzanie
    xf, yf = fade(xg), fade(yg)

    # 4. Obliczenie współrzędnych wektora gradientu w narożnikach
    n00 = gradient(ptable[(ptable[xi] + yi) % 256], xg, yg)
    n01 = gradient(ptable[(ptable[xi] + yi + 1) % 256], xg, yg - 1)
    n11 = gradient(ptable[(ptable[xi + 1] + yi + 1) % 256], xg - 1, yg - 1)
    n10 = gradient(ptable[(ptable[xi + 1] + yi) % 256], xg - 1, yg)

    # 5. Interpolacja
    x1 = lerp(n00, n10, xf)
    x2 = lerp(n01, n11, xf)
    return lerp(x1, x2, yf)


def generate_perlin_noise(width, height, scale, seed=0):
    # 1. Tworzenie siatki punktów dla danego obszaru
    x = np.linspace(0, scale, width, endpoint=False)
    y = np.linspace(0, scale, height, endpoint=False)
    x, y = np.meshgrid(x, y)

    # 2. Dla każdego punktu obliczamy wartość szumu
    noise = perlin(x, y, seed=seed)

    # 3. Skalowanie szumu z zakresu [-1, 1] na [0, 360]
    scaled_noise = (noise + 1) * 180
    return scaled_noise