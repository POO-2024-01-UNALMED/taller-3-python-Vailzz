class TV:

    _numTv = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None

        TV._tv+=1
        
    #Getter and Setter de Marca
    def getMarca(self):
        return self._marca
    def setMarca(self, marca):
        self._marca = marca

#Getter and Setter de Canal
    def getCanal(self):
        return self._canal
    def setCanal(self, i):
        if (self._estado == True) and (i <=120 ) and ( i>=1 ):
            self._canal = i

#Getter and Setter de Precio
    def getPrecio(self):
        return self._precio
    def setPrecio(self, precio):
        self._precio = precio

#Getter and Setter de Volumen

    def getVolume(self):
        return self._volumen
    def setVolume(self, volumen):
        if self._estado == True and volumen>=0 and volumen <= 7:
            self._volumen = volumen


#Getter and Setter de Control
    def getControl(self):
        return self._control
    def setControl(self, control):
        self._control = control

#Getter and Setter de numTv
    @classmethod
    def getNumTV():
        return TV._numTv
    @classmethod
    def setNumTV( num):
        TV._numTv = num



    def turnOn(self):
        self._estado = True
    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado
    
    def canalUp(self):
        if (self._estado == True)and(self._canal<120):
            self._canal +=1
    def canalDown(self):
        if (self._estado == True)and(self._canal>1):
            self._canal -=1
    def volumenUp(self):
        if (self._estado == True)and(self._volumen<7):
            self._volumen +=1
    def volumenDown(self):
        if (self._estado == True)and(self._volumen>0):
            self._volumen -=1
    