# Benutzereingabe der Seitenlängen
while True:
    a = input("Geben Sie die Länge der ersten Seite ein: ")
    while not a.replace(".", "").isnumeric():
        a = input("Input soll Float sein.\nGeben Sie die Länge der ersten Seite ein: ")
    a = float(a)

    b = input("Geben Sie die Länge der zweiten Seite ein: ")
    while not b.replace(".", "").isnumeric():
        b = input("Input soll Float sein.\nGeben Sie die Länge der zweiten Seite ein: ")
    b = float(b)

    c = input("Geben Sie die Länge der dritten Seite ein: ")
    while not c.replace(".", "").isnumeric():
        c = input("Input soll Float sein.\nGeben Sie die Länge der dritten Seite ein: ")
    c = float(c)

    # Überprüfung, ob es sich um ein gültiges Dreieck handelt
    if a + b > c:
        if a + c > b:
            if b + c > a:
    # Funktion zur Berechnung des Flächeninhalts eines Dreiecks
                s = (a + b + c) / 2
                fläche = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        
    # Funktion zur Berechnung des Umfangs eines Dreiecks
                umfang = a + b + c
                print(f"Es handelt sich um ein gültiges Dreieck.")
                print(f"Flächeninhalt des Dreiecks: {round(fläche, 2)}")
                print(f"Umfang des Dreiecks: {round(umfang, 2)}")
                break
            else:
                print("b + c darf nicht länger als a sein.")
        else:
            print("a + c darf nicht länger als b sein.")  
    else:
        print("a + b darf nicht länger als c sein.")

