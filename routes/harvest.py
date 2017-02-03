#!flask/bin/python
from flask import Blueprint, request
from rest import index, retrieve, create, replace, destroy
from resources.harvest import HarvestProcesses


harvest = Blueprint('harvest', __name__)

## API for R@B Harvest data

@harvest.route('/harvest/query/', methods=['GET'])
def index_harvest_queries():
	return index(HarvestProcesses, request)

@harvest.route('/harvest/query/', methods=['POST'])
def create_harvest_query():
	return create(HarvestProcesses, request)

@harvest.route('/harvest/query/<rabid>', methods=['GET'])
def retrieve_harvest_query(rabid):
	return retrieve(HarvestProcesses, rabid)

@harvest.route('/harvest/query/<rabid>', methods=['PUT'])
def replace_harvest_query(rabid):
	return replace(HarvestProcesses, request, rabid)

@harvest.route('/harvest/query/<rabid>', methods=['DELETE'])
def destroy_harvest_query(rabid):
	return destroy(HarvestProcesses, request, rabid)