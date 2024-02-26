from televisores import Control
class TV:

    _numTv = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = Control

        TV._tv+=1
    #Getter and Setter de Marca
    def getMarca(self):
        return self.marca
    def setMarca(self, marca):
        self._marca = marca

#Getter and Setter de Canal
    def getCanal(self):
        return self.canal
    def setCanal(self, canal):
        self.canal = canal

#Getter and Setter de Precio
    def getPrecio(self):
        return self.precio
    def setPrecio(self, precio):
        self.precio = precio

#Getter and Setter de Volumen

    def getVolume(self):
        return self.volumen
    def setVolume(self, volumen):
        self.volumen = volumen


#Getter and Setter de Control
    def getControl(self):
        return self.control
    def setControl(self, control):
        self.control = control

#Getter and Setter de numTv
    @classmethod
    def getNumTV(self):
        return T.numTv
    @classmethod
    def setNumTV(self, numTv):
        self.numTv = numTv



    def turnOn(self):
        self.estado = True
    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado
    
    def canalUp(self):
        if self.estado == True and 1 >= self.canal <= 120:
            self.canal += 1

    def canalDown(self):
        if self.estado == True and 1 >= self.canal <= 120:
            self.canal -= 1
    
    def volumenUp(self):
        if self.estado == True and 1 >= self.volumen <= 7:
            self.volumen += 1
    
    def volumenDown(self):
        if self.estado == True and 1 >= self.volumen <= 7:
            self.volumen -= 1
    