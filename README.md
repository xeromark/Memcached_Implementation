# Memcached_Implementation

    https://hub.docker.com/_/memcached

# 1) Install pymemcache cassandra-driver in python

    pip install pymemcache cassandra-driver

# 2) attach shell

    docker exec -it cassandra cqlsh


---

# Commands:

cassandra:

    CREATE KEYSPACE mykeyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 1};

    USE mykeyspace;

    CREATE TABLE fruits (
        name text PRIMARY KEY,
        description text
    );

    INSERT INTO fruits (name, description) VALUES ('Platano', 'Una fruta amarilla.');

