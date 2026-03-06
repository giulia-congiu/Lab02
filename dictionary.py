class Dictionary:

    def __init__(self):
        self.dizionario= {} #inizializzo un dizionario vuoto

    def addWord(self, alieno, italiano):
        self.dizionario.setdefault(alieno, []).extend(italiano)

    def translate(self):
        pass

    def translateWordWildCard(self):
        pass