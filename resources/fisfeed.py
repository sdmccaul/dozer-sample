import os

from dozer.graphschema import Schema, Attribute
from dozer.graphmap import Collection
from dozer.sparqler import Sparqler

from properties import foaf, vivo, blocal, rdfs, rdf, bdisplay


query_api = os.environ['QUERY_URL']
update_api = os.environ['UPDATE_URL']
user_email = os.environ['UPDATE_EMAIL']
user_pass = os.environ['UPDATE_PASS']

spq = Sparqler( query_api, update_api,
				user_email, user_pass, 'http')

#rename presets as only; add parameter for allowed
fisFacultySchema = Schema({
	'class'			: 	Attribute(rdf.rdfType, required=True,
							always=[ vivo.FacultyMember ],
							allowed=[	vivo.FacultyMember,
									blocal.BrownThing,
									bdisplay.Hidden ]),
	'label'			:	Attribute(rdfs.label, required=True, unique=True),
	'first'			:	Attribute(foaf.firstName, required=True, unique=True),
	'last'			:	Attribute(foaf.lastName, required=True, unique=True),
	'title'			:	Attribute(vivo.preferredTitle, required=True, unique=True),
	'email'			:	Attribute(vivo.primaryEmail, required=True, unique=True),
	'short_id'		: 	Attribute(blocal.shortId, required=True, unique=True),
	'middle'		:	Attribute(vivo.middleName, optional=True, unique=True),
	'updated'		: 	Attribute(blocal.fisUpdated, optional=True),
	'created'		:	Attribute(blocal.fisCreated, optional=True),
	'primary_ou'	: 	Attribute(blocal.primaryOrgLabel, optional=True),
})

# rename namespace; "resource namespace"?
fisFaculty = Collection(
				name='fisFaculty',
				schema=fisFacultySchema,
				named_graph='http://vivo.brown.edu/data/fis-faculty',
				namespace='http://vivo.brown.edu/individual/',
				prefix='faculty')
fisFaculty.register_endpoint(spq)

#rename presets as only; add parameter for allowed
fisDegreesSchema = Schema({
	'class'		: 	Attribute(rdf.rdfType, required=True,
						only=[ vivo.EducationalTraining ]),
	'degree'	:	Attribute(rdfs.label, required=True, unique=True),
	'faculty'	:	Attribute(vivo.educationalTrainingOf, required=True, unique=True),
	'org'		:	Attribute(vivo.trainingAtOrganization, required=True, unique=True),
	'date'		:	Attribute(blocal.degreeDate, required=True, unique=True),
})

# rename namespace; "resource namespace"?
fisDegrees = Collection(
				name='fisDegrees',
				schema=fisDegreesSchema,
				named_graph='http://vivo.brown.edu/data/fis-degrees',
				namespace='http://vivo.brown.edu/individual/',
				prefix='faculty')
fisDegrees.register_endpoint(spq)

#rename presets as only; add parameter for allowed
fisOrgsSchema = Schema({
	'class'		: 	Attribute(rdf.rdfType, required=True,
						only=[ foaf.Organization ]),
	'org'	:	Attribute(rdfs.label, required=True, unique=True),
})

# rename namespace; "resource namespace"?
fisOrgs = Collection(
				name='fisOrgs',
				schema=fisOrgsSchema,
				named_graph='http://vivo.brown.edu/data/fis-orgs',
				namespace='http://vivo.brown.edu/individual/',
				prefix='faculty')
fisOrgs.register_endpoint(spq)