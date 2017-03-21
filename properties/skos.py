from dozer.graphschema import Domain


### Model Namespace ###

## This is not being picked up by scaffolding
## due to W3C weirdness. Check 'about' attributes
## in SKOS rdf/xml
ns =  'http://www.w3.org/2004/02/skos/core#'

### Class Declarations ###

Concept            =  ns + 'Concept'
ConceptScheme      =  ns + 'ConceptScheme'
Collection         =  ns + 'Collection'
OrderedCollection  =  ns + 'OrderedCollection'

### Property Declarations ###

inScheme            =  Domain(ns + 'inScheme',            'uri')
hasTopConcept       =  Domain(ns + 'hasTopConcept',       'uri')
topConceptOf        =  Domain(ns + 'topConceptOf',        'uri')
notation            =  Domain(ns + 'notation',            'string')
semanticRelation    =  Domain(ns + 'semanticRelation',    'uri')
broader             =  Domain(ns + 'broader',             'uri')
narrower            =  Domain(ns + 'narrower',            'uri')
related             =  Domain(ns + 'related',             'uri')
broaderTransitive   =  Domain(ns + 'broaderTransitive',   'uri')
narrowerTransitive  =  Domain(ns + 'narrowerTransitive',  'uri')
member              =  Domain(ns + 'member',              'uri')
memberList          =  Domain(ns + 'memberList',          'uri')
mappingRelation     =  Domain(ns + 'mappingRelation',     'uri')
broadMatch          =  Domain(ns + 'broadMatch',          'uri')
narrowMatch         =  Domain(ns + 'narrowMatch',         'uri')
relatedMatch        =  Domain(ns + 'relatedMatch',        'uri')
exactMatch          =  Domain(ns + 'exactMatch',          'uri')
closeMatch          =  Domain(ns + 'closeMatch',          'uri')
## Scaffolding needs reworking to handle Annotation Properties
## see SKOS rdf/xml
altLabel			=  Domain(ns + 'altLabel',            'string')
hiddenLabel			=  Domain(ns + 'hiddenLabel',         'string')