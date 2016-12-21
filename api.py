#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
import json
import os

app = Flask(__name__)
app.config.from_pyfile('config/api.cfg')

os.environ['QUERY_URL'] = app.config['QUERY_URL']
os.environ['UPDATE_URL'] = app.config['UPDATE_URL']
os.environ['UPDATE_EMAIL'] = app.config['UPDATE_EMAIL']
os.environ['UPDATE_PASS'] = app.config['UPDATE_PASS']

from resources.errors import ValidationError, \
	AliasError, RESTError

@app.errorhandler(RESTError)
def handle_rest_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


## API for FIS faculty data
from resources.fisfeed import fisFaculty

@app.route('/fisfaculty/', methods=['GET'])
def index_faculty():
	# Working for single strings
	# problems for dates, multival?
	params = { k: [v] for k, v in request.args.items() }
	try:
		allFisFaculty = fisFaculty.search(params=params)
	except AliasError as e:
		raise RESTError('Bad parameter',
			status_code=400, payload=e.msg)
	except:
		raise RESTError('Resource not found', status_code=404)
	return json.dumps([ fac.to_dict()
							for fac in allFisFaculty])

@app.route('/fisfaculty/<rabid>', methods=['GET'])
def retrieve_faculty(rabid):
	try:
		fisfac = fisFaculty.find(rabid=rabid)
	except:
		raise RESTError('Resource not found', status_code=404)
	resp = make_response(
				json.dumps(fisfac.to_dict()))
	resp.headers['ETag'] = fisfac.etag
	return resp

@app.route('/fisfaculty/', methods=['POST'])
def create_faculty():
	try:
		fisfac = fisFaculty.create(
					data=request.get_json())
	except (AliasError, ValidationError) as e:
		raise RESTError('Bad data',
					status_code=400, payload=e.msg) 
	resp = make_response(
				json.dumps(fisfac.to_dict()))
	resp.headers['ETag'] = fisfac.etag
	return resp

@app.route('/fisfaculty/<rabid>', methods=['PUT'])
def replace_faculty(rabid):
	try:
		fisfac = fisFaculty.find(rabid=rabid)
	except:
		raise RESTError('Resource not found', status_code=404)
	if fisfac.etag == request.headers.get("If-Match"):
		try:
			updated = fisFaculty.overwrite(fisfac, request.get_json())
		except (AliasError, ValidationError) as e:
			raise RESTError('Validation',
				status_code=400, payload=e.msg)
		resp = make_response(
				json.dumps(updated.to_dict()))
		resp.headers['ETag'] = updated.etag
		return resp
	else:
		raise RESTError('Data modified on server',
							status_code=409, payload=fisfac.to_dict())

@app.route('/fisfaculty/<rabid>', methods=['DELETE'])
def destroy_faculty(rabid):
	try:
		fisfac = fisFaculty.find(rabid=rabid)
	except:
		raise RESTError('No resource to delete', status_code=410)
	if fisfac.etag == request.headers.get("If-Match"):
		try:
			fisFaculty.remove(fisfac)
			resp = make_response('', 204)
			return resp
		except (AliasError, ValidationError) as e:
			raise RESTError('Validation',
				status_code=400, payload=e.msg)
	else:
		raise RESTError('Data modified on server',
							status_code=409, payload=fisfac.to_dict())


## API for FIS Degrees data
from resources.fisfeed import fisDegrees

@app.route('/fisdegrees/', methods=['GET'])
def index_degrees():
	# Working for single strings
	# problems for dates, multival?
	params = { k: [v] for k, v in request.args.items() }
	try:
		allFisDegrees = fisDegrees.search(params=params)
	except AliasError as e:
		raise RESTError('Bad parameter',
			status_code=400, payload=e.msg)
	except:
		raise RESTError('Resource not found', status_code=404)
	return json.dumps([ degree.to_dict()
							for degree in allFisDegrees])

@app.route('/fisdegrees/<rabid>', methods=['GET'])
def retrieve_degrees(rabid):
	try:
		fisdegree = fisDegrees.find(rabid=rabid)
	except:
		raise RESTError('Resource not found', status_code=404)
	resp = make_response(
				json.dumps(fisdegree.to_dict()))
	resp.headers['ETag'] = fisdegree.etag
	return resp

@app.route('/fisdegrees/', methods=['POST'])
def create_degrees():
	try:
		fisdegree = fisDegrees.create(
					data=request.get_json())
	except (AliasError, ValidationError) as e:
		raise RESTError('Bad data',
					status_code=400, payload=e.msg) 
	resp = make_response(
				json.dumps(fisdegree.to_dict()))
	resp.headers['ETag'] = fisdegree.etag
	return resp

@app.route('/fisdegrees/<rabid>', methods=['PUT'])
def replace_degrees(rabid):
	try:
		fisdegree = fisDegrees.find(rabid=rabid)
	except:
		raise RESTError('Resource not found', status_code=404)
	if fisdegree.etag == request.headers.get("If-Match"):
		try:
			updated = fisDegrees.overwrite(
						fisdegree, request.get_json())
		except (AliasError, ValidationError) as e:
			raise RESTError('Validation',
				status_code=400, payload=e.msg)
		resp = make_response(
				json.dumps(updated.to_dict()))
		resp.headers['ETag'] = updated.etag
		return resp
	else:
		raise RESTError('Data modified on server',
						status_code=409, payload=fisdegree.to_dict())

@app.route('/fisdegrees/<rabid>', methods=['DELETE'])
def destroy_degrees(rabid):
	try:
		fisdegree = fisDegrees.find(rabid=rabid)
	except:
		raise RESTError('No resource to delete', status_code=410)
	if fisdegree.etag == request.headers.get("If-Match"):
		try:
			fisDegrees.remove(fisdegree)
			resp = make_response('', 204)
			return resp
		except (AliasError, ValidationError) as e:
			raise RESTError('Validation',
				status_code=400, payload=e.msg)
	else:
		raise RESTError('Data modified on server',
						status_code=409,
						payload=fisdegree.to_dict())


## API for FIS Organizations data
from resources.fisfeed import fisOrgs

@app.route('/fisorgs/', methods=['GET'])
def index_fis_orgs():
	# Working for single strings
	# problems for dates, multival?
	params = { k: [v] for k, v in request.args.items() }
	try:
		allFisOrgs = fisOrgs.search(params=params)
	except AliasError as e:
		raise RESTError('Bad parameter',
			status_code=400, payload=e.msg)
	except:
		raise RESTError('Resource not found', status_code=404)
	return json.dumps([ fisorg.to_dict()
							for fisorg in allFisOrgs])

@app.route('/fisorgs/<rabid>', methods=['GET'])
def retrieve_fis_orgs(rabid):
	try:
		fisorg = fisOrgs.find(rabid=rabid)
	except:
		raise RESTError('Resource not found', status_code=404)
	resp = make_response(
				json.dumps(fisorg.to_dict()))
	resp.headers['ETag'] = fisorg.etag
	return resp

@app.route('/fisorgs/', methods=['POST'])
def create_fis_orgs():
	try:
		fisorg = fisOrgs.create(
					data=request.get_json())
	except (AliasError, ValidationError) as e:
		raise RESTError('Bad data',
					status_code=400, payload=e.msg) 
	resp = make_response(
				json.dumps(fisorg.to_dict()))
	resp.headers['ETag'] = fisorg.etag
	return resp

@app.route('/fisorgs/<rabid>', methods=['PUT'])
def replace_fis_orgs(rabid):
	try:
		fisorg = fisOrgs.find(rabid=rabid)
	except:
		raise RESTError('Resource not found', status_code=404)
	if fisorg.etag == request.headers.get("If-Match"):
		try:
			updated = fisOrgs.overwrite(
						fisorg, request.get_json())
		except (AliasError, ValidationError) as e:
			raise RESTError('Validation',
				status_code=400, payload=e.msg)
		resp = make_response(
				json.dumps(updated.to_dict()))
		resp.headers['ETag'] = updated.etag
		return resp
	else:
		raise RESTError('Data modified on server',
						status_code=409, payload=fisorg.to_dict())

@app.route('/fisorgs/<rabid>', methods=['DELETE'])
def destroy_fis_orgs(rabid):
	try:
		fisorg = fisOrgs.find(rabid=rabid)
	except:
		raise RESTError('No resource to delete', status_code=410)
	if fisorg.etag == request.headers.get("If-Match"):
		try:
			fisOrgs.remove(fisorg)
			resp = make_response('', 204)
			return resp
		except (AliasError, ValidationError) as e:
			raise RESTError('Validation',
				status_code=400, payload=e.msg)
	else:
		raise RESTError('Data modified on server',
						status_code=409,
						payload=fisorg.to_dict())


## API for R@B Citations data
from resources.citations import Citations

@app.route('/citations/', methods=['GET'])
def index_citations():
	# Working for single strings
	# problems for dates, multival?
	params = { k: [v] for k, v in request.args.items() }
	try:
		allCitations = Citations.search(params=params)
	except AliasError as e:
		raise RESTError('Bad parameter',
			status_code=400, payload=e.msg)
	except:
		raise RESTError('Resource not found', status_code=404)
	return json.dumps([ citation.to_dict()
							for citation in allCitations])

@app.route('/citations/<rabid>', methods=['GET'])
def retrieve_citation(rabid):
	try:
		citation = Citations.find(rabid=rabid)
	except:
		raise RESTError('Resource not found', status_code=404)
	resp = make_response(
				json.dumps(citation.to_dict()))
	resp.headers['ETag'] = citation.etag
	return resp

@app.route('/citations/', methods=['POST'])
def create_citation():
	try:
		citation = Citations.create(
					data=request.get_json())
	except (AliasError, ValidationError) as e:
		raise RESTError('Bad data',
					status_code=400, payload=e.msg) 
	resp = make_response(
				json.dumps(citation.to_dict()))
	resp.headers['ETag'] = citation.etag
	return resp

@app.route('/citations/<rabid>', methods=['PUT'])
def replace_citation(rabid):
	try:
		citation = Citations.find(rabid=rabid)
	except:
		raise RESTError('Resource not found', status_code=404)
	if citation.etag == request.headers.get("If-Match"):
		try:
			updated = Citations.overwrite(
						citation, request.get_json())
		except (AliasError, ValidationError) as e:
			raise RESTError('Validation',
				status_code=400, payload=e.msg)
		resp = make_response(
				json.dumps(updated.to_dict()))
		resp.headers['ETag'] = updated.etag
		return resp
	else:
		raise RESTError('Data modified on server',
						status_code=409, payload=citation.to_dict())

@app.route('/citations/<rabid>', methods=['DELETE'])
def destroy_citation(rabid):
	try:
		citation = Citations.find(rabid=rabid)
	except:
		raise RESTError('No resource to delete', status_code=410)
	if citation.etag == request.headers.get("If-Match"):
		try:
			Citations.remove(citation)
			resp = make_response('', 204)
			return resp
		except (AliasError, ValidationError) as e:
			raise RESTError('Validation',
				status_code=400, payload=e.msg)
	else:
		raise RESTError('Data modified on server',
						status_code=409,
						payload=citation.to_dict())

if __name__ == '__main__':
	app.run(host='0.0.0.0')
