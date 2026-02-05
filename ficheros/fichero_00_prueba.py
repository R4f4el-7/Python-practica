try:
    with open("hola.txt", "w") as f:
        f.write("Now the file has more content!")

    #open and read the file after the appending:
    with open("hola.txt") as f:
        print(f.read())
except:
    print("Fichero no existe")