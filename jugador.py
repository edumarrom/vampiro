import localidades
import localidad
import mapeado

"""
El jugador debe ser un único objeto de la clase Jugador (a ésto se le llama Singleton).
Fuente sobre patrón singleton: https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
"""

class Jugador:
    _loc_inicial = mapeado.vestibulo
    class __Jugador:
        def __init__(self, _loc_inicial):
            self._localidad_actual = _loc_inicial
        def __str__(self):
            return repr(self) + self._localidad_actual
    instance = None

    def __init__(self, _loc_inicial):
        if not Jugador.instance:
            Jugador.instance = Jugador.__Jugador(_loc_inicial)
        else:
            Jugador.instance._localidad_actual = _loc_inicial
    def __getattr__(self, name):
        return getattr(self.instance, name)

    # Selectores
    def localidad_actual(self):
        """Devuelve la localidad actual del jugador."""
        return self._localidad_actual

    # Mutadores
    def set_localidad_actual(self, destino):
        """Modifica la localidad del jugador"""
        _localidad_actual = destino
        self.describe_localidad_actual()

    # Ecuaciones
    def describe_localidad_actual(self):
        """Muestra en pantalla info sobre la localidad actual"""
        print(localidad.corta(self._localidad_actual))
        print(localidad.larga(self._localidad_actual))

    def intentar_mover(verbo):
        destino = localidades.salida_hacia(localidad_actual(), verbo)
        if destino is not None:
            mover_jugador(destino)
            return True
        return False
