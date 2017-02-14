#!flask/bin/python
from flask import Blueprint, request
from rest import index, retrieve, create, replace, destroy
from resources.harvest import PubmedSearch, WosSearch


harvest = Blueprint('harvest', __name__)

## API for PubMed Search

@harvest.route('/harvest/pubmed/', methods=['GET'])
def index_pubmed_queries():
	return index(PubmedSearch, request)

@harvest.route('/harvest/pubmed/', methods=['POST'])
def create_pubmed_query():
	return create(PubmedSearch, request)

@harvest.route('/harvest/pubmed/<rabid>', methods=['GET'])
def retrieve_pubmed_query(rabid):
	return retrieve(PubmedSearch, rabid)

@harvest.route('/harvest/pubmed/<rabid>', methods=['PUT'])
def replace_pubmed_query(rabid):
	return replace(PubmedSearch, request, rabid)

@harvest.route('/harvest/pubmed/<rabid>', methods=['DELETE'])
def destroy_pubmed_query(rabid):
	return destroy(PubmedSearch, request, rabid)

## API for Web of Science Search

@harvest.route('/harvest/wos/', methods=['GET'])
def index_wos_queries():
	return index(WosSearch, request)

@harvest.route('/harvest/wos/', methods=['POST'])
def create_wos_query():
	return create(WosSearch, request)

@harvest.route('/harvest/wos/<rabid>', methods=['GET'])
def retrieve_wos_query(rabid):
	return retrieve(WosSearch, rabid)

@harvest.route('/harvest/wos/<rabid>', methods=['PUT'])
def replace_wos_query(rabid):
	return replace(WosSearch, request, rabid)

@harvest.route('/harvest/wos/<rabid>', methods=['DELETE'])
def destroy_wos_query(rabid):
	return destroy(WosSearch, request, rabid)