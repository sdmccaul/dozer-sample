#!flask/bin/python
from flask import Blueprint, request
from rest import index, retrieve, create, replace, destroy
from resources.fisfeed import fisFaculty, fisOrgs, fisDegrees


fisfeed = Blueprint('fisfeed', __name__)

## API for FIS Faculty data

@fisfeed.route('/fisfaculty/', methods=['GET'])
def index_faculty():
	return index(fisFaculty, request)

@fisfeed.route('/fisfaculty/', methods=['POST'])
def create_faculty():
	return create(fisFaculty, request)

@fisfeed.route('/fisfaculty/<rabid>', methods=['GET'])
def retrieve_faculty(rabid):
	return retrieve(fisFaculty, rabid)

@fisfeed.route('/fisfaculty/<rabid>', methods=['PUT'])
def replace_faculty(rabid):
	return replace(fisFaculty, request, rabid)

@fisfeed.route('/fisfaculty/<rabid>', methods=['DELETE'])
def destroy_faculty(rabid):
	return destroy(fisFaculty, request, rabid)


## API for FIS Degrees data

@fisfeed.route('/fisdegrees/', methods=['GET'])
def index_degrees():
	return index(fisDegrees, request)

@fisfeed.route('/fisdegrees/', methods=['POST'])
def create_degrees():
	return create(fisDegrees, request)

@fisfeed.route('/fisdegrees/<rabid>', methods=['GET'])
def retrieve_degrees(rabid):
	return retrieve(fisDegrees, rabid)

@fisfeed.route('/fisdegrees/<rabid>', methods=['PUT'])
def replace_degrees(rabid):
	return replace(fisDegrees, request, rabid)

@fisfeed.route('/fisdegrees/<rabid>', methods=['DELETE'])
def destroy_degrees(rabid):
	return destroy(fisDegrees, request, rabid)


## API for FIS Organizations data

@fisfeed.route('/fisorgs/', methods=['GET'])
def index_fis_orgs():
	return index(fisOrgs, request)

@fisfeed.route('/fisorgs/', methods=['POST'])
def create_fis_orgs():
	return create(fisOrgs, request)

@fisfeed.route('/fisorgs/<rabid>', methods=['GET'])
def retrieve_fis_orgs(rabid):
	return retrieve(fisOrgs, rabid)

@fisfeed.route('/fisorgs/<rabid>', methods=['PUT'])
def replace_fis_orgs(rabid):
	return replace(fisOrgs, request, rabid)

@fisfeed.route('/fisorgs/<rabid>', methods=['DELETE'])
def destroy_fis_orgs(rabid):
	return destroy(fisOrgs, request, rabid)