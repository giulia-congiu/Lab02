class Dictionary:

    def __init__(self):
        self.dizionario= {} #inizializzo un dizionario vuoto

    def addWord(self, alieno, traduzioni):
        # traduzioni è una lista ["gatto", "cat"]
        if alieno in self.dizionario:
            self.dizionario[alieno].extend(traduzioni)
            # extend aggiunge tutti gli elementi di una lista (o iterabile) a un'altra lista, uno per uno.
            # APPEND invece aggiunge l'oggetto intero
        else:
            self.dizionario[alieno] = list(traduzioni)

    def translate(self, alieno):
        #if self.dizionario.get(alieno)
        #ricorda che get restituisce none se non c'è l parola
        if alieno in self.dizionario:
        #equiv. a dizionario.containsKey(parola)
            return self.dizionario[alieno] #ho già controllato che esista
        return None

        #oppure direttamente return self.dizionario.get(alieno) !!!



    def translateWordWildCard(self, query):
        #restituisce un dizionario con tutte le parole che matchano la query.
        # nel dizionario hai:
        # "rakastan" → ["amo"]
        # "rakastun" → ["adoro"]  (ipotetico)
        # "kissa"    → ["gatto"]  (non matcha, lunghezza diversa)

        # la funzione restituisce:
        # {
        #     "rakastan": ["amo"],
        #     "rakastun": ["adoro"]
        # }

        # index() è un metodo delle stringhe che restituisce la posizione (indice) di un carattere nella stringa!
        posizione_punto_interrogativo = query.index("?")  # posizione del ? nella query
        risultati = {}

        for chiave in self.dizionario:
            if len(chiave) == len(query):  # stessa lunghezza?
                match = True
                for i in range(len(query)):
                    if i == posizione_punto_interrogativo:
                        continue  # salta il ?
                    if chiave[i] != query[i]:
                        match = False
                        break
                if match:
                    risultati[chiave] = self.dizionario[chiave]

        return risultati


    def printAll(self):
        for parola, traduzioni in self.dizionario.items():
            print(parola, traduzioni)

