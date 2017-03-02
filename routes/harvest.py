#!flask/bin/python
from flask import Blueprint, request
from rest import index, retrieve, create, replace, destroy
from resources.harvest import HarvestProcess, HarvestSource


harvest = Blueprint('harvest', __name__)

## API for Harvest Process

@harvest.route('/harvest/processes/', methods=['GET'])
def index_processes():
	return index(HarvestProcess, request)

@harvest.route('/harvest/processes/', methods=['POST'])
def create_process():
	return create(HarvestProcess, request)

@harvest.route('/harvest/processes/<rabid>', methods=['GET'])
def retrieve_process(rabid):
	return retrieve(HarvestProcess, rabid)

@harvest.route('/harvest/processes/<rabid>', methods=['PUT'])
def replace_process(rabid):
	return replace(HarvestProcess, request, rabid)

@harvest.route('/harvest/processes/<rabid>', methods=['DELETE'])
def destroy_process(rabid):
	return destroy(HarvestProcess, request, rabid)


## API for Harvest Source

@harvest.route('/harvest/sources/', methods=['GET'])
def index_sources():
	return index(HarvestSource, request)

@harvest.route('/harvest/sources/', methods=['POST'])
def create_source():
	return create(HarvestSource, request)

@harvest.route('/harvest/sources/<rabid>', methods=['GET'])
def retrieve_source(rabid):
	return retrieve(HarvestSource, rabid)

@harvest.route('/harvest/sources/<rabid>', methods=['PUT'])
def replace_source(rabid):
	return replace(HarvestSource, request, rabid)

@harvest.route('/harvest/sources/<rabid>', methods=['DELETE'])
def destroy_source(rabid):
	return destroy(HarvestSource, request, rabid)
