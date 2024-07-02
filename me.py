from pymemcache.client import base

# Conectar al servidor Memcached
client = base.Client(('localhost', 11211))

# Enviar el valor "Platano" a Memcached con la clave "fruit"
client.set('fruit', 'Platano')

# Recuperar el valor de la clave "fruit"
value = client.get('fruit')

# Mostrar el valor recuperado
print(value.decode('utf-8'))  # Decodificar de bytes a cadena

# Cerrar la conexión
client.close()
