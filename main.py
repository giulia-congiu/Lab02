import translator as tr

t = tr.Translator()


while True:

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()
    while not txtIn.isdigit() or not (1 <= int(txtIn) <= 4):
            print("ERRORE, INSERISCI UN NUMERO DA 1 A 4!")
            txtIn=input() #torno all'inizio

     # Add input control here!

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere")
        txtIn = input().lower()
        while not txtIn.isalpha():
            print("ERRORE, INSERISCI UNA PAROLA")
            txtIn = input().lower()  # torno all'inizio
        parola = txtIn.split()
        print(parola)
        print("Aggiunta")

    if int(txtIn) == 2:
        print("Ok, quale parola devo cercare?")
        txtIn = input()
        pass

    if int(txtIn) == 3:
        pass

    if int(txtIn) == 4:
        break