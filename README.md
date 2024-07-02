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

    CREATE TABLE dishes (
        name text PRIMARY KEY,
        price int
    );

# Copy data in docker

    docker cp dishes cassandra:/home/dishes

# Copy data to cassandra bash

    COPY mykeyspace.dishes (name, price) FROM '/home/dishes' WITH DELIMITER='|' AND HEADER=TRUE;

# Insert into dishes table

    INSERT INTO mykeyspace.dishes (name, price) VALUES ('Platano', 145000);


---
# Others:

Row count:

    SELECT COUNT(*) FROM mykeyspace.dishes;

Only 5 Row:

    SELECT * FROM dishes LIMIT 5;

Fetch something:

    SELECT price FROM mykeyspace.dishes WHERE name='Platano';