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
pubmedSearchSchema = Schema({
	'class'					: 	Attribute(rdf.rdfType, required=True,
									always=[	bharvest.HarvestProcess,
												bharvest.PubMedSearch ],
									allowed=[ 	bharvest.HarvestProcess,
												bharvest.PubMedSearch ]),
	'label'					:	Attribute(rdfs.label, required=True),
	'user'					:	Attribute(bharvest.hasUser, required=True),
	'affiliation'			:	Attribute(bharvest.affiliation, optional=True),
	'all_fields'			:	Attribute(bharvest.allFields, optional=True),
	'corporate'				:	Attribute(bharvest.corporateAuthor, optional=True),
	'first_name'			:	Attribute(bharvest.authorFirstName, optional=True),
	'full_name'				:	Attribute(bharvest.authorFullName, optional=True),
	'author_id'				:	Attribute(bharvest.authorIdentifier, optional=True),
	'last_name'				:	Attribute(bharvest.authorLastName, optional=True),
	'book'					:	Attribute(bharvest.book, optional=True),
	'completed_date'		:	Attribute(bharvest.completionDate, optional=True),
	'created_date'			:	Attribute(bharvest.createDate, optional=True),
	'entrez_date'			:	Attribute(bharvest.entrezDate, optional=True),
	'mesh_date'				:	Attribute(bharvest.meshDate, optional=True),
	'mod_date'				:	Attribute(bharvest.modificationDate, optional=True),
	'publication_date'		:	Attribute(bharvest.publicationDate, optional=True),
	'ecrn_num'				:	Attribute(bharvest.ecrnNumber, optional=True),
	'editor'				:	Attribute(bharvest.editor, optional=True),
	'filter_param'			:	Attribute(bharvest.filter, optional=True),
	'grant_num'				:	Attribute(bharvest.grantNumber, optional=True),
	'isbn'					:	Attribute(bharvest.isbn, optional=True),
	'investigator'			:	Attribute(bharvest.investigator, optional=True),
	'investigator_full'		:	Attribute(bharvest.investigatorFullName, optional=True),
	'issue'					:	Attribute(bharvest.issue, optional=True),
	'journal'				:	Attribute(bharvest.journal, optional=True),
	'language'				:	Attribute(bharvest.language, optional=True),
	'location_id'			:	Attribute(bharvest.locationID, optional=True),
	'mesh_major'			:	Attribute(bharvest.meshMajorTopic, optional=True),
	'mesh_subhead'			:	Attribute(bharvest.meshSubHeading, optional=True),
	'mesh_terms'			:	Attribute(bharvest.meshTerms, optional=True),
	'other_term'			:	Attribute(bharvest.otherTerms, optional=True),
	'pagination'			:	Attribute(bharvest.pagination, optional=True),
	'pharma_action'			:	Attribute(bharvest.pharmacologicalAction, optional=True),
	'publication_type'		:	Attribute(bharvest.publicationType, optional=True),
	'publisher'				:	Attribute(bharvest.publisher, optional=True),
	'secondary_src_id'		:	Attribute(bharvest.secondarySourceID, optional=True),
	'sbj_personal_name'		:	Attribute(bharvest.subjectPersonalName, optional=True),
	'supplmnt_concept'		:	Attribute(bharvest.supplementaryConcept, optional=True),
	'text_word'				:	Attribute(bharvest.text, optional=True),
	'title'					:	Attribute(bharvest.title, optional=True),
	'title_abstract'		:	Attribute(bharvest.titleAbstract, optional=True),
	'translit_title'		:	Attribute(bharvest.transliteratedTitle, optional=True),
	'volume'				:	Attribute(bharvest.volume, optional=True)
})

PubmedSearch = Collection(
				name='pubmed processes',
				schema=pubmedSearchSchema,
				named_graph='http://vivo.brown.edu/data/harvest',
				namespace='http://vivo.brown.edu/individual/',
				prefix='harvest')
PubmedSearch.register_endpoint(spq)


wosSearchSchema = Schema({
	'class'					: 	Attribute(rdf.rdfType, required=True,
									always=[	bharvest.HarvestProcess,
												bharvest.WebOfScienceSearch ],
									allowed=[ 	bharvest.HarvestProcess,
												bharvest.WebOfScienceSearch ]),
	'label'					:	Attribute(rdfs.label, required=True),
	'user'					:	Attribute(bharvest.hasUser, required=True),
	'topic'					:	Attribute(bharvest.topic, optional=True),
	'title'					:	Attribute(bharvest.title, optional=True),
	'author'				:	Attribute(bharvest.author, optional=True),
	'author_ids'			:	Attribute(bharvest.authorIdentifier, optional=True),
	'group_author'			:	Attribute(bharvest.groupAuthor, optional=True),
	'editor'				:	Attribute(bharvest.editor, optional=True),
	'publication'			:	Attribute(bharvest.publication, optional=True),
	'doi'					:	Attribute(bharvest.doi, optional=True),
	'year'					:	Attribute(bharvest.year, optional=True),
	'address'				:	Attribute(bharvest.address, optional=True),
	'organizations'			:	Attribute(bharvest.organization, optional=True),
	'conference'			:	Attribute(bharvest.conference, optional=True),
	'language'				:	Attribute(bharvest.language, optional=True),
	'doc_typ'				:	Attribute(bharvest.documentType, optional=True),
	'funding_agency'		:	Attribute(bharvest.fundingAgency, optional=True),
	'grant_number'			:	Attribute(bharvest.grantNumber, optional=True),
	'accession_number'		:	Attribute(bharvest.accessionNumber, optional=True),
	'pmid'					:	Attribute(bharvest.pmid, optional=True)
})

WosSearch = Collection(
				name='pubmed processes',
				schema=wosSearchSchema,
				named_graph='http://vivo.brown.edu/data/harvest',
				namespace='http://vivo.brown.edu/individual/',
				prefix='harvest')
WosSearch.register_endpoint(spq)