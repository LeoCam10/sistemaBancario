class Transferencia():
    def __init__(self,monto= str, tipo= str, documento=str, internacional=None, dolares=None, verificado=None, motivo=str):
        self._tipo = tipo
        self._documento = documento
        self._motivo = motivo
        self._monto = monto
        self._dolares = dolares
        self._internacional = internacional

class DepositoInternacional():
    def __init__(self,monto= str, tipo= str, documento=str, nombre1 = str, nombre2= str, apellido1= str, apellido2= str, sexo=str, internacional = True , dolares = True, fechanacimiento= None, lugarnacimiento=str, terminos = bool, motivo=str):
        self._tipo = tipo
        self._documento = documento
        self._motivo = motivo
        self._monto = monto
        self._dolares = dolares
        self._internacional = internacional
        self._nombre1 = nombre1
        self._nombre2 = nombre2
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._fechanacimiento = fechanacimiento
        self._lugarnacimiento = lugarnacimiento
        self._terminos = terminos
        self._sexo = sexo
      





