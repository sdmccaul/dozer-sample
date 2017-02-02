#!flask/bin/python
from flask import Blueprint, request
from rest import index, retrieve, create, replace, destroy
from resources.citations import Citations


citations = Blueprint('citations', __name__)

## API for R@B Citations data

@citations.route('/citations/', methods=['GET'])
def index_citations():
	return index(Citations, request)

@citations.route('/citations/', methods=['POST'])
def create_citation():
	return create(Citations, request)

@citations.route('/citations/<rabid>', methods=['GET'])
def retrieve_citation(rabid):
	return retrieve(Citations, rabid)

@citations.route('/citations/<rabid>', methods=['PUT'])
def replace_citation(rabid):
	return replace(Citations, request, rabid)

@citations.route('/citations/<rabid>', methods=['DELETE'])
def destroy_citation(rabid):
	return destroy(Citations, request, rabid)