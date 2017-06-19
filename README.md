# DjangoREST

Basic <a href=https://en.wikipedia.org/wiki/Representational_state_transfer>REST</a> api that serves as an interface for an Elasticsearch database. It is built with *Django*, <a href=http://www.django-rest-framework.org/>Django REST framework</a> and <a href=https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/index.html> elasticsearch-py</a>. The database contains news articles with two different fields: *title* and *body*.

There are three views defined for the api:

- */articles/titles/*, which retrieves all titles from the database
- */articles/bodys/*, which retrieves all news bodies
- */articles/(title)/*, which retrieves the body corresponding to a specific title
