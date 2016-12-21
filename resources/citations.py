import os

from dozer.graphschema import Schema, Attribute
from dozer.graphmap import Collection
from dozer.sparqler import Sparqler

from properties import rdfs, rdf, bcite


query_api = os.environ['QUERY_URL']
update_api = os.environ['UPDATE_URL']
user_email = os.environ['UPDATE_EMAIL']
user_pass = os.environ['UPDATE_PASS']

spq = Sparqler( query_api, update_api,
				user_email, user_pass, 'http')

#rename presets as only; add parameter for allowed
citationSchema = Schema({
	'class'						: 	Attribute(rdf.rdfType, required=True,
										always=[ bcite.Citation ],
										allowed=[	bcite.Citation,
											bcite.Review,
											bcite.Abstract,
											bcite.Article,
											bcite.ConferencePaper,
											bcite.Book,
											bcite.Chapter,
											bcite.BookSection,
											bcite.Patent,
											bcite.WorkingPaper ]),
	'label'						:	Attribute(rdfs.label, required=True, unique=True),
	'assignee'					:	Attribute(bcite.hasAssignee, optional=True),
	'authority'					:	Attribute(bcite.hasAuthority, optional=True),
	'conference'				:	Attribute(bcite.hasConference, optional=True),
	'conference_location'		:	Attribute(bcite.hasConferenceLocation, optional=True),
	'contributor'				:	Attribute(bcite.hasContributor, optional=True),
	'country'					:	Attribute(bcite.hasCountry, optional=True),
	'location'					:	Attribute(bcite.hasLocation, optional=True),
	'publisher'					:	Attribute(bcite.hasPublisher, optional=True),
	'venue'						:	Attribute(bcite.hasVenue, optional=True),
	'author_list'				:	Attribute(bcite.authorList, optional=True),
	'book'						:	Attribute(bcite.book, optional=True),
	'chapter'					:	Attribute(bcite.chapter, optional=True),
	'conference_date'			:	Attribute(bcite.conferenceDate, optional=True),
	'date'						:	Attribute(bcite.date, optional=True),
	'doi'						:	Attribute(bcite.doi, optional=True),
	'editor_list'				:	Attribute(bcite.editorList, optional=True),
	'eissn'						:	Attribute(bcite.eissn, optional=True),
	'isbn'						:	Attribute(bcite.isbn, optional=True),
	'issn'						:	Attribute(bcite.issn, optional=True),
	'issue'						:	Attribute(bcite.issue, optional=True),
	'number'					:	Attribute(bcite.number, optional=True),
	'pages'						:	Attribute(bcite.pages, optional=True),
	'patent_number'				:	Attribute(bcite.patentNumber, optional=True),
	'pmcid'						:	Attribute(bcite.pmcid, optional=True),
	'pmid'						:	Attribute(bcite.pmid, optional=True),
	'published_in'				:	Attribute(bcite.publishedIn, optional=True),
	'review_of'					:	Attribute(bcite.reviewOf, optional=True),
	'title'						:	Attribute(bcite.title, optional=True),
	'url'						:	Attribute(bcite.url, optional=True),
	'version'					:	Attribute(bcite.version, optional=True),
	'volume'					:	Attribute(bcite.volume, optional=True)
})

Citations = Collection(
				name='citations',
				schema=citationSchema,
				named_graph='http://vivo.brown.edu/data/citations',
				namespace='http://vivo.brown.edu/individual/',
				prefix='citation')
Citations.register_endpoint(spq)