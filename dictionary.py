class Dictionary:
    def __init__(self):
        self.data= {} #inizializzo un dizionario vuoto

    def addWord(self, alieno, italiano):
        self.data[alieno]=italiano

    def translate(self):
        pass

    def translateWordWildCard(self):
        pass