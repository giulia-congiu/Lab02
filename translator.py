from dictionary import Dictionary
class Translator:

    def __init__(self):
        self.dictionary=Dictionary()

    def printMenu(self):
        print("-"*25)
        print(f"{'Translator Alien-Italian':^20}")
        print("-" * 25)
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print('3. Cerca con wildcard')
        print('4. Exit')
        print("-" * 25)
        pass



    def loadDictionary(self, dict):
        with open (dict, "r", encoding='utf-8') as file:
           # dict is a string with the filename of the dictionary
               for riga in file:
                   riga.strip().split()
                    #self.dictionary
                    #[[alieno]= italiano

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass