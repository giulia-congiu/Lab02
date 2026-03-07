import translator as tr

t = tr.Translator()
t.loadDictionary("dictionary.txt")

while True:

    t.printMenu()

    txtIn = input()
    while not txtIn.isdigit() or not (1 <= int(txtIn) <= 4):
            print("ERRORE, INSERISCI UN NUMERO DA 1 A 4!")
            txtIn=input() #torno all'inizio

     # Add input control here!

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere")
        inparola = input().lower()
        while not inparola.replace(" ","").isalpha():
            print("ERRORE, INSERISCI UNA PAROLA")
            inparola = input().lower()  # torno all'inizio
        parola = inparola.split() #in questo modo passo a handleadd una lista
        t.handleAdd(parola)
        print(parola)
        print("Aggiunta")

    if int(txtIn) == 2:
        print("Ok, quale parola devo cercare?")
        inparola = input().lower()
        while not inparola.isalpha():
            print("ERRORE, INSERISCI UNA PAROLA")
            inparola = input().lower()  # torno all'inizio

        t.handleTranslate(inparola)


    if int(txtIn) == 3:
        print("Ok, quale parola devo cercare?")
        inparola = input().lower()
        while not all(c.isalpha() or c == "?" for c in inparola) or inparola.count("?") != 1:
            #all(...) — restituisce True se tutti gli elementi soddisfano la condizione
            #inparola.count("?") != 1 — controlla che ci sia esattamente solo un ?:
            print("ERRORE, INSERISCI UNA PAROLA CON UN SOLO ?")
            inparola = input().lower()
        t.handleWildCard(inparola)

    if int(txtIn) == 4:
        if int(txtIn) == 4:
            t.handlePrintAll()

    if int(txtIn) == 5:
        break