from localidad import Localidad
from coleccion import Coleccion
from conexion import Conexion

c = Conexion('NORTE', )

vestibulo = Localidad('VESTIBULO', 'Estás en el vestibulo...',)
pasillo = Localidad('PASILLO', 'Te encuentras en el pasillo...')
cocina = Localidad('COCINA', 'Estás en la cocina...')
biblioteca = Localidad('BIBLIOTECA', 'La biblioteca del castillo...')


vestibulo.set_conexiones({
    'NORTE': pasillo
})

pasillo.set_conexiones({
    'NORTE': vestibulo,
    'ESTE': biblioteca,
    'OESTE': cocina
})

cocina.set_conexiones({
    'ESTE': pasillo
})


al_pasillo = Conexion('NORTE' , pasillo)
