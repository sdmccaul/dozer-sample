from dozer.graphschema import Domain


### Model Namespace ###

ns =  'http://vivo.brown.edu/ontology/harvest#'

### Class Declarations ###

PubMedSearch        =  ns + 'PubMedSearch'
HarvestUser         =  ns + 'HarvestUser'
WebOfScienceSearch  =  ns + 'WebOfScienceSearch'
HarvestProcess      =  ns + 'HarvestProcess'

### Property Declarations ###

meshMajorTopic         =  Domain(ns + 'meshMajorTopic',         'string')
editor                 =  Domain(ns + 'editor',                 'string')
locationID             =  Domain(ns + 'locationID',             'string')
doi                    =  Domain(ns + 'doi',                    'string')
publicationType        =  Domain(ns + 'publicationType',        'string')
affiliation            =  Domain(ns + 'affiliation',            'string')
transliteratedTitle    =  Domain(ns + 'transliteratedTitle',    'string')
book                   =  Domain(ns + 'book',                   'string')
title                  =  Domain(ns + 'title',                  'string')
organization           =  Domain(ns + 'organization',           'string')
authorFirstName        =  Domain(ns + 'authorFirstName',        'string')
pharmacologicalAction  =  Domain(ns + 'pharmacologicalAction',  'string')
supplementaryConcept   =  Domain(ns + 'supplementaryConcept',   'string')
groupAuthor            =  Domain(ns + 'groupAuthor',            'string')
year                   =  Domain(ns + 'year',                   'string')
secondarySourceID      =  Domain(ns + 'secondarySourceID',      'string')
entrezDate             =  Domain(ns + 'entrezDate',             'string')
authorFullName         =  Domain(ns + 'authorFullName',         'string')
language               =  Domain(ns + 'language',               'string')
investigator           =  Domain(ns + 'investigator',           'string')
completionDate         =  Domain(ns + 'completionDate',         'string')
otherTerms             =  Domain(ns + 'otherTerms',             'string')
subjectPersonalName    =  Domain(ns + 'subjectPersonalName',    'string')
publicationDate        =  Domain(ns + 'publicationDate',        'string')
publisher              =  Domain(ns + 'publisher',              'string')
type                   =  Domain(ns + 'type',                   'string')
address                =  Domain(ns + 'address',                'string')
isbn                   =  Domain(ns + 'isbn',                   'string')
authorLastName         =  Domain(ns + 'authorLastName',         'string')
fundingAgency          =  Domain(ns + 'fundingAgency',          'string')
authorIdentifier       =  Domain(ns + 'authorIdentifier',       'string')
meshDate               =  Domain(ns + 'meshDate',               'string')
allFields              =  Domain(ns + 'allFields',              'string')
grantNumber            =  Domain(ns + 'grantNumber',            'string')
topic                  =  Domain(ns + 'topic',                  'string')
text                   =  Domain(ns + 'text',                   'string')
meshSubHeading         =  Domain(ns + 'meshSubHeading',         'string')
pmid                   =  Domain(ns + 'pmid',                   'string')
corporateAuthor        =  Domain(ns + 'corporateAuthor',        'string')
filter                 =  Domain(ns + 'filter',                 'string')
volume                 =  Domain(ns + 'volume',                 'string')
publication            =  Domain(ns + 'publication',            'string')
hasHarvestProcess      =  Domain(ns + 'hasHarvestProcess',      'uri')
conference             =  Domain(ns + 'conference',             'string')
author                 =  Domain(ns + 'author',                 'string')
hasUser                =  Domain(ns + 'hasUser',                'uri')
createDate             =  Domain(ns + 'createDate',             'string')
modificationDate       =  Domain(ns + 'modificationDate',       'string')
titleAbstract          =  Domain(ns + 'titleAbstract',          'string')
issue                  =  Domain(ns + 'issue',                  'string')
journal                =  Domain(ns + 'journal',                'string')
meshTerms              =  Domain(ns + 'meshTerms',              'string')
accessionNumber        =  Domain(ns + 'accessionNumber',        'string')
documentType           =  Domain(ns + 'documentType',           'string')
investigatorFullName   =  Domain(ns + 'investigatorFullName',   'string')
ecrnNumber             =  Domain(ns + 'ecrnNumber',             'string')
pagination             =  Domain(ns + 'pagination',             'string')
