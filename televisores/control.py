from televisores.tv import TV
class Control:
    def __init__(self, tv):
        self._tv = tv
    
    def enlazar(self, tv):
        self.tv = tv
        tv.setControl(self)
    
    def turnOn(self):
        self._tv.turnOn()
    
    def turnOff(self):
        self._tv.turnOff()
    
    def canalUp(self):
        self._tv.setCanal(self.tv.getCanal() + 1)
    
    def canalDown(self):
        self._tv.setCanal(self.tv.getCanal() - 1)
    
    def volumenUp(self):
        self._tv.setVolumen(self.tv.getVolumen() + 1)
    
    def volumenDown(self):
        self._tv.setVolumen(self.tv.getVolumen() - 1)
    
    def setCanal(self, canal):
        self._tv.setCanal(canal)
    
    def setVolumen(self, volumen):
        self._tv.setVolumen(volumen)