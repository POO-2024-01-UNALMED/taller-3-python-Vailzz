class TV:
    def __init__(self, marca, estado):
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1
        self.control = control
        self.numTv = 0

    def getMarca(self):
        return self.marca
    def setMarca(self, marca):
        self.marca = marca

    def getCanal(self):
        return self.canal
    def setCanal(self, canal):
        self.canal = canal

    def getPrecio(self):
        return self.precio
    def setPrecio(self, precio):
        self.precio = precio

    def getVolume(self):
        return self.volumen
    def setVolume(self, volumen):
        self.volumen = volumen

    def getControl(self):
        return self.control
    def setControl(self, control):
        self.control = control

    def getNumTV(self):
        return self.numTv
    def setNumTV(self, numTv):
        self.numTv = numTv

    def turnOn(self):
        self.estado = True
    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado
    