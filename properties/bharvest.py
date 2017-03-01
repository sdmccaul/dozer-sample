from dozer.graphschema import Domain


### Model Namespace ###

ns =  'http://vivo.brown.edu/ontology/harvest#'

### Class Declarations ###

User                     =  ns + 'User'
WebOfScienceSearch       =  ns + 'WebOfScienceSearch'
AcademicAnalyticsUpload  =  ns + 'AcademicAnalyticsUpload'
HarvestProcess           =  ns + 'HarvestProcess'
Source                   =  ns + 'Source'
PubMedSearch             =  ns + 'PubMedSearch'

### Property Declarations ###

query             =  Domain(ns + 'query',             'string')
status            =  Domain(ns + 'status',            'string')
hasUser           =  Domain(ns + 'hasUser',           'uri')
sourceHasProcess  =  Domain(ns + 'sourceHasProcess',  'uri')
userHasProcess    =  Domain(ns + 'userHasProcess',    'uri')
hasSource         =  Domain(ns + 'hasSource',         'uri')
