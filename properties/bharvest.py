from dozer.graphschema import Domain


### Model Namespace ###

ns =  'http://vivo.brown.edu/ontology/harvest#'

### Class Declarations ###

HarvestUser     =  ns + 'HarvestUser'
HarvestProcess  =  ns + 'HarvestProcess'

### Property Declarations ###

meshMajorTopic         =  Domain(ns + 'meshMajorTopic',         'string')
otherTerm              =  Domain(ns + 'otherTerm',              'string')
editor                 =  Domain(ns + 'editor',                 'string')
isbn                   =  Domain(ns + 'isbn',                   'string')
locationID             =  Domain(ns + 'locationID',             'string')
publicationType        =  Domain(ns + 'publicationType',        'string')
affiliation            =  Domain(ns + 'affiliation',            'string')
authorLastName         =  Domain(ns + 'authorLastName',         'string')
transliteratedTitle    =  Domain(ns + 'transliteratedTitle',    'string')
book                   =  Domain(ns + 'book',                   'string')
title                  =  Domain(ns + 'title',                  'string')
authorIdentifier       =  Domain(ns + 'authorIdentifier',       'string')
meshDate               =  Domain(ns + 'meshDate',               'string')
allFields              =  Domain(ns + 'allFields',              'string')
filterParam            =  Domain(ns + 'filterParam',            'string')
grantNumber            =  Domain(ns + 'grantNumber',            'string')
authorFirstName        =  Domain(ns + 'authorFirstName',        'string')
pharmacologicalAction  =  Domain(ns + 'pharmacologicalAction',  'string')
supplementaryConcept   =  Domain(ns + 'supplementaryConcept',   'string')
meshSubHeading         =  Domain(ns + 'meshSubHeading',         'string')
corporateAuthor        =  Domain(ns + 'corporateAuthor',        'string')
secondarySourceID      =  Domain(ns + 'secondarySourceID',      'string')
entrezDate             =  Domain(ns + 'entrezDate',             'string')
volume                 =  Domain(ns + 'volume',                 'string')
authorFullName         =  Domain(ns + 'authorFullName',         'string')
language               =  Domain(ns + 'language',               'string')
investigator           =  Domain(ns + 'investigator',           'string')
completionDate         =  Domain(ns + 'completionDate',         'string')
hasHarvestProcess      =  Domain(ns + 'hasHarvestProcess',      'uri')
hasUser                =  Domain(ns + 'hasUser',                'uri')
modificationDate       =  Domain(ns + 'modificationDate',       'string')
creationDate           =  Domain(ns + 'creationDate',           'string')
subjectPersonalName    =  Domain(ns + 'subjectPersonalName',    'string')
publicationDate        =  Domain(ns + 'publicationDate',        'string')
titleAbstract          =  Domain(ns + 'titleAbstract',          'string')
issue                  =  Domain(ns + 'issue',                  'string')
journal                =  Domain(ns + 'journal',                'string')
publisher              =  Domain(ns + 'publisher',              'string')
textWord               =  Domain(ns + 'textWord',               'string')
meshTerms              =  Domain(ns + 'meshTerms',              'string')
investigatorFullName   =  Domain(ns + 'investigatorFullName',   'string')
ecrnNumber             =  Domain(ns + 'ecrnNumber',             'string')
pagination             =  Domain(ns + 'pagination',             'string')
