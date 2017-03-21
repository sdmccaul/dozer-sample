#!flask/bin/python
from flask import Blueprint, request
from rest import index, retrieve, create, replace, destroy
from resources.vocab import Terms


vocab = Blueprint('vocab', __name__)

## API for vocab Process

@vocab.route('/vocab/', methods=['GET'])
def index_terms():
	return index(Terms, request)

@vocab.route('/vocab/', methods=['POST'])
def create_term():
	return create(Terms, request)

@vocab.route('/vocab/<rabid>', methods=['GET'])
def retrieve_term(rabid):
	return retrieve(Terms, rabid)

@vocab.route('/vocab/<rabid>', methods=['PUT'])
def replace_term(rabid):
	return replace(Terms, request, rabid)

@vocab.route('/vocab/<rabid>', methods=['DELETE'])
def destroy_term(rabid):
	return destroy(Terms, request, rabid)