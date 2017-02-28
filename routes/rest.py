#!flask/bin/python
from flask import jsonify, make_response

from resources.errors import ValidationError, AliasError, RESTError


def index(resource, request):
	# Working for single strings
	# problems for dates, multival?
	params = { k: [v] for k, v in request.args.items() }
	try:
		all_resources = resource.search(params=params)
	except AliasError as e:
		raise RESTError('Bad parameter',
			status_code=400, payload=e.msg)
	except:
		raise RESTError('Resource not found', status_code=404)
	return jsonify([ res.to_dict() for res in all_resources ])

def retrieve(resource, rabid):
	try:
		res = resource.find(rabid=rabid)
	except:
		raise RESTError('Resource not found', status_code=404)
	resp = make_response( jsonify(res.to_dict()) )
	resp.headers['ETag'] = res.etag
	return resp

def create(resource, request):
	try:
		res = resource.create(data=request.get_json())
	except (AliasError, ValidationError) as e:
		raise RESTError('Bad data',
					status_code=400, payload=e.msg) 
	resp = make_response( jsonify(res.to_dict()) )
	resp.headers['ETag'] = res.etag
	return resp

def replace(resource, request, rabid):
	try:
		res = resource.find(rabid=rabid)
	except:
		raise RESTError('Resource not found', status_code=404)
	if res.etag == request.headers.get("If-Match"):
		try:
			updated = resource.overwrite(res, request.get_json())
		except (AliasError, ValidationError) as e:
			raise RESTError('Validation',
				status_code=400, payload=e.msg)
		resp = make_response( jsonify(updated.to_dict()) )
		resp.headers['ETag'] = updated.etag
		return resp
	else:
		raise RESTError('Data modified on server',
							status_code=409, payload=res.to_dict())

def destroy(resource, request, rabid):
	try:
		res = resource.find(rabid=rabid)
	except:
		raise RESTError('No resource to delete', status_code=410)
	if res.etag == request.headers.get("If-Match"):
		try:
			resource.remove(res)
			resp = make_response('', 204)
			return resp
		except (AliasError, ValidationError) as e:
			raise RESTError('Validation',
				status_code=400, payload=e.msg)
	else:
		raise RESTError('Data modified on server',
							status_code=409, payload=res.to_dict())