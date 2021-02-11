from localidad import Localidad
from coleccion import Coleccion
from conexion import Conexion

c = Conexion('NORTE', )

vestibulo = Localidad('VESTIBULO', 'Estás en el vestibulo...')
pasillo = Localidad('PASILLO', 'Te encuentras en el pasillo...')
cocina = Localidad('COCINA', 'Estás en la cocina...')
biblioteca = Localidad('BIBLIOTECA', 'La biblioteca del castillo...' )


"""
    N
E - | - O
    S
    Cocina --- Mitad pasillo --- Biblioteca
                    |
                Vestíbulo
"""

vestibulo.set_conexiones({
    'NORTE': pasillo
})

pasillo.set_conexiones({
    'SUR': vestibulo,
    'ESTE': biblioteca,
    'OESTE': cocina
})

cocina.set_conexiones({
    'ESTE': pasillo
})

biblioteca.set_conexiones({
    'OESTE': pasillo
})


al_pasillo = Conexion('NORTE', pasillo)
al_vestibulo = Conexion('SUR', vestibulo)
