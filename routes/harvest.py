#!flask/bin/python
from flask import Blueprint, request
from rest import index, retrieve, create, replace, destroy
from resources.harvest import HarvestProcess


harvest = Blueprint('harvest', __name__)

## API for Harvest Process

@harvest.route('/harvest/processes/', methods=['GET'])
def index_pubmed_queries():
	return index(HarvestProcess, request)

@harvest.route('/harvest/processes/', methods=['POST'])
def create_pubmed_query():
	return create(HarvestProcess, request)

@harvest.route('/harvest/processes/<rabid>', methods=['GET'])
def retrieve_pubmed_query(rabid):
	return retrieve(HarvestProcess, rabid)

@harvest.route('/harvest/processes/<rabid>', methods=['PUT'])
def replace_pubmed_query(rabid):
	return replace(HarvestProcess, request, rabid)

@harvest.route('/harvest/processes/<rabid>', methods=['DELETE'])
def destroy_pubmed_query(rabid):
	return destroy(HarvestProcess, request, rabid)
