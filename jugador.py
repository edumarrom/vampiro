import localidades
import localidad

"""
El jugador debe ser un único objeto de la clase Jugador (a ésto se le llama Singleton).
Fuente sobre patrón singleton: https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
"""
class Jugador:

    class __Jugador:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    instance = None
    def __init__(self, arg):
        if not Jugador.instance:
            Jugador.instance = Jugador.__Jugador(arg)
        else:
            Jugador.instance.val = arg
    def __getattr__(self, name):
        return getattr(self.instance, name)

"""
    _localidad_actual = localidades.localidad(localidades.VESTIBULO)

    def localidad_actual():               # getter, selectora
        return _localidad_actual

    def mover_jugador(destino):
        global _localidad_actual
        _localidad_actual = destino
        describe_localidad_actual()

    def describe_localidad_actual():
        print(localidad.corta(_localidad_actual))
        print(localidad.larga(_localidad_actual))

    def intentar_mover(verbo):
        destino = localidades.salida_hacia(localidad_actual(), verbo)
        if destino is not None:
            mover_jugador(destino)
            return True
        return False
"""
