from dozer.graphschema import Domain


### Model Namespace ###

ns =  'http://vivo.brown.edu/ontology/citation#'

### Class Declarations ###

Citation            =  ns + 'Citation'
Review              =  ns + 'Review'
Abstract            =  ns + 'Abstract'
Article             =  ns + 'Article'
Contributor         =  ns + 'Contributor'
Conference          =  ns + 'Conference'
Publisher           =  ns + 'Publisher'
Location            =  ns + 'Location'
ConferencePaper     =  ns + 'ConferencePaper'
Book                =  ns + 'Book'
Chapter             =  ns + 'Chapter'
Venue               =  ns + 'Venue'
ConferenceLocation  =  ns + 'ConferenceLocation'
BookSection         =  ns + 'BookSection'
Patent              =  ns + 'Patent'
WorkingPaper        =  ns + 'WorkingPaper'

### Property Declarations ###

contributorTo          =  Domain(ns + 'contributorTo',          'uri')
conferenceDate         =  Domain(ns + 'conferenceDate',         'dateTime')
authorList             =  Domain(ns + 'authorList',             'string')
title                  =  Domain(ns + 'title',                  'string')
doi                    =  Domain(ns + 'doi',                    'string')
issn                   =  Domain(ns + 'issn',                   'string')
book                   =  Domain(ns + 'book',                   'string')
hasVenue               =  Domain(ns + 'hasVenue',               'uri')
url                    =  Domain(ns + 'url',                    'string')
hasConferenceLocation  =  Domain(ns + 'hasConferenceLocation',  'uri')
editorList             =  Domain(ns + 'editorList',             'string')
version                =  Domain(ns + 'version',                'string')
cvId                   =  Domain(ns + 'cvId',                   'string')
cites                  =  Domain(ns + 'cites',                  'uri')
wokId                  =  Domain(ns + 'wokId',                  'string')
pageStart              =  Domain(ns + 'pageStart',              'string')
hasPublisher           =  Domain(ns + 'hasPublisher',           'uri')
hasLocation            =  Domain(ns + 'hasLocation',            'uri')
issue                  =  Domain(ns + 'issue',                  'string')
pageEnd                =  Domain(ns + 'pageEnd',                'string')
firstName              =  Domain(ns + 'firstName',              'string')
locationFor            =  Domain(ns + 'locationFor',            'uri')
conferenceLocationFor  =  Domain(ns + 'conferenceLocationFor',  'uri')
middleName             =  Domain(ns + 'middleName',             'string')
isbn                   =  Domain(ns + 'isbn',                   'string')
oclc                   =  Domain(ns + 'oclc',                   'string')
lastName               =  Domain(ns + 'lastName',               'string')
pmid                   =  Domain(ns + 'pmid',                   'string')
citedAs                =  Domain(ns + 'citedAs',                'uri')
volume                 =  Domain(ns + 'volume',                 'string')
number                 =  Domain(ns + 'number',                 'string')
hasContributor         =  Domain(ns + 'hasContributor',         'uri')
pages                  =  Domain(ns + 'pages',                  'string')
venueFor               =  Domain(ns + 'venueFor',               'uri')
hasConference          =  Domain(ns + 'hasConference',          'uri')
date                   =  Domain(ns + 'date',                   'dateTime')
pmcid                  =  Domain(ns + 'pmcid',                  'string')
publisherFor           =  Domain(ns + 'publisherFor',           'uri')
conferenceFor          =  Domain(ns + 'conferenceFor',          'uri')

# Added by hand
hasAssignee            =  Domain(ns + 'hasAssignee',            'uri')
hasAuthority           =  Domain(ns + 'hasAuthority',           'uri')
hasCountry             =  Domain(ns + 'hasCountry',             'uri')
chapter                =  Domain(ns + 'chapter',                'string')
eissn                  =  Domain(ns + 'eissn',                  'string')
patentNumber           =  Domain(ns + 'patentNumber',           'string')
publishedIn            =  Domain(ns + 'publishedIn',            'string')
reviewOf               =  Domain(ns + 'reviewOf',               'string')