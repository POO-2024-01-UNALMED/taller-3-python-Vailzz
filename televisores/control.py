from televisores import TV

class Control:
    def __init__(self):
        self.tv = TV


    def enlazar(self, televisor):
        self.tv = televisor

    def getTv(self):
        return self.tv
    def setTv(self, televisor):
        self.tv = televisor