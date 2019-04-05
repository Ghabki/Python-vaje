from random import*
Ana = 1
Berta = 1

while True:
    a = randint(1, 6)
    Ana = Ana + a
    print("Ana vrže", a, "in je na polju", Ana)

    while a == 6:

        if Ana >= 30:
            break

        a = randint(1, 6)
        Ana = Ana + a
        print("Ana vrže ponovno,", a, "in je na polju", Ana)
        if Berta == Ana:
            Berta = 0
            print("Berta gre na začetek")

    if Ana >= 30:
        print("Ana je zmagala")
        break

    if Berta == Ana:
        Berta = 0
        print("Berta gre na začetek")
#-------------------------------------
    b = randint(1, 6)
    Berta = Berta + b
    print("Berta vrže", b, "in je na polju", Berta)

    while b == 6:
        if Berta >= 30:
            break

        b = randint(1, 6)
        Berta = Berta + b
        print("Berta vrže ponovno,", b, "in je na polju", Berta)
        if Ana == Berta:
            Ana = 0
            print("Ana gre na začetek")


    if Berta >= 30:
        print("Berta je zmagala")
        break

    if Ana == Berta:
        Ana = 0
        print("Ana gre na začetek")

print("Konec igre")