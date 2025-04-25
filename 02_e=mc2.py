def main ():
    mass =float (input("\033[1;3mEnter a mass in kilogram: "))
    print("e = m * C^2...")
    m = mass
    c = 299792458 
    E = m * c**2
    print(f"m = {m} kg")
    print(f"c = {c} m/s\n ")
    print(f"{E} joules of energy!\033[0m")

if __name__ == '__main__':
    main()
