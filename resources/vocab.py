import os

from dozer.graphschema import Schema, Attribute
from dozer.graphmap import Collection
from dozer.sparqler import Sparqler

from properties import rdfs, rdf, skos

query_api = os.environ['QUERY_URL']
update_api = os.environ['UPDATE_URL']
user_email = os.environ['UPDATE_EMAIL']
user_pass = os.environ['UPDATE_PASS']

spq = Sparqler( query_api, update_api,
				user_email, user_pass, 'http')

#rename presets as only; add parameter for allowed
termSchema = Schema({
	'class'			: 	Attribute(rdf.rdfType, required=True,
							only=[ skos.Concept ]),
	'label'			:	Attribute(rdfs.label, required=True, unique=True),
	'related'		:	Attribute(skos.related),
	'broader'		:	Attribute(skos.broader),
	'narrower'		:	Attribute(skos.narrower),
	'alternative'	:	Attribute(skos.altLabel),
	'hidden'		: 	Attribute(skos.hiddenLabel)
})

# rename namespace; "resource namespace"?
Terms = Collection(
				name='Terms',
				schema=termSchema,
				named_graph='http://vivo.brown.edu/data/rabvocab',
				namespace='http://vivo.brown.edu/individual/',
				prefix='vocab')
Terms.register_endpoint(spq)