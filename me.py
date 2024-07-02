from pymemcache.client import base as memcache_client
from cassandra.cluster import Cluster
import time
begin_time = time.time()

# connect to Memcached
memcached = memcache_client.Client(('localhost', 11211))

# connect to Cassandra
cluster = Cluster(['localhost'])
session = cluster.connect('mykeyspace')

# function to get data
def get_price_dish(dish_name):
    # First, it Try to get data in Memcached
    cached_value = memcached.get(dish_name)
    if cached_value:
        return cached_value.decode('utf-8')

    # If not found, fetch in Cassandra
    query = "SELECT price FROM dishes WHERE name=%s"
    result = session.execute(query, (dish_name,))
    price_dish = result.one()
    if price_dish:
        # store in Memcached to future searches
        memcached.set(dish_name, price_dish.price)
        return price_dish.price

    return None

# Test function
dish_name = 'Platano'
price_dish = get_price_dish(dish_name)
if price_dish:
    print(f"The dish {dish_name}, price: {price_dish}")
else:
    print(f"{dish_name} not found in data base.")


end_time = time.time()
# Calcula el tiempo transcurrido
delta_time = end_time - begin_time

print(f"Dish '{dish_name}' delay: '{delta_time}' seconds.")

