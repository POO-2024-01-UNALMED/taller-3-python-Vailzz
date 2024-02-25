
from televisores.tv import TV
class Control:
    def __init__(self, tv):
        self.tv = tv
    
    def enlazar(self, tv):
        self.tv = tv
        self.tv.setControl(self)
    
    def turnOn(self):
        self.tv.turnOn()
    
    def turnOff(self):
        self.tv.turnOff()
    
    def canalUp(self):
        self.tv.setCanal(self.tv.getCanal() + 1)
    
    def canalDown(self):
        self.tv.setCanal(self.tv.getCanal() - 1)
    
    def volumenUp(self):
        self.tv.setVolumen(self.tv.getVolumen() + 1)
    
    def volumenDown(self):
        self.tv.setVolumen(self.tv.getVolumen() - 1)
    
    def setCanal(self, canal):
        self.tv.setCanal(canal)
    
    def setVolumen(self, volumen):
        self.tv.setVolumen(volumen)