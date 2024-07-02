from pymemcache.client import base as memcache_client
from cassandra.cluster import Cluster

# Conectar a Memcached
memcached = memcache_client.Client(('localhost', 11211))

# Conectar a Cassandra
cluster = Cluster(['localhost'])
session = cluster.connect('mykeyspace')

# Función para obtener datos de Memcached o Cassandra
def get_fruit_description(fruit_name):
    # Intentar obtener el valor de Memcached
    cached_value = memcached.get(fruit_name)
    if cached_value:
        return cached_value.decode('utf-8')

    # Si no está en Memcached, buscar en Cassandra
    query = "SELECT description FROM fruits WHERE name=%s"
    result = session.execute(query, (fruit_name,))
    description = result.one()
    if description:
        # Almacenar el resultado en Memcached para futuras búsquedas
        memcached.set(fruit_name, description.description)
        return description.description

    return None

# Prueba de la función
fruit_name = 'Platano'
description = get_fruit_description(fruit_name)
if description:
    print(f"Descripción de {fruit_name}: {description}")
else:
    print(f"{fruit_name} no encontrado en la base de datos.")
