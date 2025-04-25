import random

def main ():

    first_die = random.randint (1, 6)
    second_die = random.randint (1, 6)

    total = first_die + second_die

    print (f"first dice rolled {first_die}")
    print (f"first dice rolled {second_die}")
    print(f"Total of two dice {total}")


if __name__ == "__main__":
    main()