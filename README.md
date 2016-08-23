Project where Django and Cassandra are used, was created as a pattern of interaction of Django and Cassandra to use in the future.
It uses django-cassandra-engine version 0.11.0. 
Cassandra server was started on Docker, the database was accessible through cqlsh.


To start cassandra server on docker:
docker login
docker pull cassandra
sudo docker run -p 9042:9042 -p 8888:8888 -p 7000:7000 -p 7001:7001 -p 7199:7199 -p 8983:8983 -p 9160:9160 -p 61620:61620 -p 61621:61621 -it cassandra


Currently there exist a bug in django_cassandra_engine, the fix for it is described here:
https://github.com/r4fek/django-cassandra-engine/issues/70


Command for syncronising models with the database:
python manage.py sync_cassandra
