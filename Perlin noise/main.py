from visual_simulations import run_perlin_noise, run_cloud_simulation

def main():
    print("Wybierz symulację:")
    print("1. Szum Perlin (mapa wysokości)")
    print("2. Symulacja chmur")
    choice = input("Twój wybór (1/2): ")

    if choice == "1":
        run_perlin_noise()
    elif choice == "2":
        run_cloud_simulation()
    else:
        print("Nieprawidłowy wybór.")

if __name__ == "__main__":
    main()
