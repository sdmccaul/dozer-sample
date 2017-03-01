import os

from dozer.graphschema import Schema, Attribute
from dozer.graphmap import Collection
from dozer.sparqler import Sparqler

from properties import rdfs, rdf, bharvest


query_api = os.environ['QUERY_URL']
update_api = os.environ['UPDATE_URL']
user_email = os.environ['UPDATE_EMAIL']
user_pass = os.environ['UPDATE_PASS']

spq = Sparqler( query_api, update_api,
				user_email, user_pass, 'http')

#rename presets as only; add parameter for allowed
harvestProcessSchema = Schema({
	'class'					: 	Attribute(rdf.rdfType, required=True,
									always=[	bharvest.HarvestProcess ],
									allowed=[ 	bharvest.HarvestProcess,
												bharvest.PubMedSearch,
												bharvest.WebOfScienceSearch,
												bharvest.AcademicAnalyticsUpload ]),
	'label'					:	Attribute(rdfs.label, required=True),
	'user'					:	Attribute(bharvest.hasUser, required=True),
	'source'				:	Attribute(bharvest.hasSource, required=True),
	'status'				:	Attribute(bharvest.status, optional=True),
	'query'					:	Attribute(bharvest.query, optional=True)
})

HarvestProcess = Collection(
				name='harvest process',
				schema=harvestProcessSchema,
				named_graph='http://vivo.brown.edu/data/harvest',
				namespace='http://vivo.brown.edu/individual/',
				prefix='harvest')
HarvestProcess.register_endpoint(spq)


harvestSourceSchema = Schema({
	'class'					: 	Attribute(rdf.rdfType, required=True,
									always	= [ bharvest.Source ],
									allowed	= [ bharvest.Source ]),
	'label'					:	Attribute(rdfs.label, required=True),
})

HarvestSource = Collection(
				name='harvest source',
				schema=harvestSourceSchema,
				named_graph='http://vivo.brown.edu/data/harvest',
				namespace='http://vivo.brown.edu/individual/',
				prefix='harvest')
HarvestSource.register_endpoint(spq)