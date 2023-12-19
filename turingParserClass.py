class TuringParserClass:
    #Constructor
    def __init__(self,estado_actual,char_en_string,char_escribir,movimiento,estado_nuevo):
        self._estado_actual=estado_actual
        self._char_en_string=char_en_string
        self._char_escribir=char_escribir
        self._movimiento=movimiento
        self._estado_nuevo=estado_nuevo
    
    #GETTERS
    def getEstadoActual(self):
        return self._estado_actual
    def getCharEnString(self):
        return self._char_en_string  
    def getCharEscribir(self):
        return self._char_escribir
    def getMovimiento(self):
        return self._movimiento
    def getEstadoNuevo(self):
        return self._estado_nuevo
    #SETTERS
    def setEstadoActual(self,estado_actual):
        self._estado_actual=estado_actual
    def setCharEnString(self,char_en_string):
        self._char_en_string=char_en_string
    def setCharEscribir(self,char_escribir):
        self._char_escribir=char_escribir
    def setMovimiento(self,movimiento):
        self._movimiento=movimiento
    def setEstadoNuevo(self,estado_nuevo):
        self._estado_nuevo=estado_nuevo
    def __str__(self):
        return f"{self._estado_actual}, {self._char_en_string}, {self._char_escribir}, {self._movimiento}, {self._estado_nuevo}"
        