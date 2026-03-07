from dictionary import Dictionary
class Translator:

    def __init__(self):
        self.dizionario=Dictionary()

    def printMenu(self):
        print("-"*25)
        print(f"{'Translator Alien-Italian':^20}")
        print("-" * 25)
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print('3. Cerca con wildcard')
        print('4. Stampa tutto')
        print('5. Esci')
        print("-" * 25)
        pass


    def loadDictionary(self, dict):
        with open (dict, "r", encoding='utf-8') as file:
           # dict is a string with the filename of the dictionary
               for riga in file:
                    coppia= riga.strip().split()
                    alieno= coppia[0]
                    italiano= coppia[1:] # lista di tutte le traduzioni
                    self.dizionario.addWord(alieno, italiano)


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        chiave= entry[0]
        traduzioni= entry[1:]
        self.dizionario.addWord(chiave, traduzioni)


    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        traduzioni= self.dizionario.translate(query)
        if traduzioni is None:
            print("Parola non trovata!")
        else:
            print(traduzioni)



    def handleWildCard(self,query):
        #query is a string with a ? --> <par?la_aliena>
        risultati = self.dizionario.translateWordWildCard(query) #è un dizionario
        if not risultati:
            print("Nessuna parola trovata!")
        else:
            for parola, traduzioni in risultati.items():
                print(parola)
                for t in traduzioni:
                    print(t)


    def handlePrintAll(self):
        self.dizionario.printAll()