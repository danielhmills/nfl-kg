import pyodbc as db
from query import query_n1

source = "https://raw.githubusercontent.com/danielhmills/nfl-kg/master/pbp/r2rml.ttl"
destination = "http://demo.openlinksw.com/nfl-pbp-kg#"

queries = {
    "q": 'SELECT TOP 5 *  FROM nfl.pbp.demo',
    "clear_data":'SPARQL CLEAR GRAPH <urn:nfl:kg:pbp>',
    "r2rml_qm_drop":'SPARQL DROP QUAD MAP <%s>' % (source),
    "r2rml_clear_graph":'SPARQL CLEAR GRAPH <%s>' % (source),
    "r2rml_insert":"DB.DBA.R2RML_GENERATE_LINKED_VIEW('%s', '%s',0 ,1)" % (source,destination),
    "r2rml_physical":"RDF_VIEW_SYNC_TO_PHYSICAL ('%s', 1, 'urn:nfl:kg:pbp')" % (destination),
}

for y in queries.values():
    query_n1(y)