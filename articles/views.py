from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from articles.models import Article
from articles.serializers import ArticleSerializer

from elasticsearch import Elasticsearch

@api_view(['GET'])
def get_titles(request):
    """
    Returns title of all articles in database
    """
    if request.method == 'GET':
        es = Elasticsearch('http://ec2-52-202-185-94.compute-1.amazonaws.com:9200/')
        query = {
        	"query":{"match_all":{}},
        	"_source":"Title"
        }
        res = es.search(index="el-mundo", body=query)
        
    return Response([el['_source'] for el in res['hits']['hits']])

@api_view(['GET'])
def get_bodys(request):
    """
    Returns body of all articles in database
    """
    if request.method == 'GET':
        es = Elasticsearch('http://ec2-52-202-185-94.compute-1.amazonaws.com:9200/')
        query = {
        	"query":{"match_all":{}},
        	"_source":"Body"
        }
        res = es.search(index="el-mundo", body=query)
	return Response([el['_source'] for el in res['hits']['hits']])

@api_view(['GET'])
def search(request, title):
    """
    Returns the body of the title provided
    """
    if request.method == 'GET':
        es = Elasticsearch('http://ec2-52-202-185-94.compute-1.amazonaws.com:9200/')
        query = {
        	"query":{"match":{"Title":title.replace("_", " ")}},
        	"_source":"Body",
        	"size":1
        }
        res = es.search(index="el-mundo", body=query)

	return Response([el['_source'] for el in res['hits']['hits']])
