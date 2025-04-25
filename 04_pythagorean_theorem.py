def main ():
    AB = float (input("Enter the length of AB: "))
    AC = float (input("Enter the length of AC: "))
   
   

    BC  = (AB ** 2 + AC ** 2) **0.5
    print (f"The length of BC (the hypotenuse) is: {BC}")

if __name__ == '__main__':
    main()
