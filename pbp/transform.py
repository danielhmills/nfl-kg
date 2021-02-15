import pyodbc as db
from query import query

q = 'SELECT TOP 5 *  FROM nfl.pbp.demo'
clear_data  = 'SPARQL CLEAR GRAPH <urn:nfl:pbp:data>'
r2rml_qm_drop = 'SPARQL DROP QUAD MAP <https://raw.githubusercontent.com/danielhmills/nflkg/pbp/r2rml.ttl>'
r2rml_clear_graph = 'SPARQL CLEAR GRAPH <https://raw.githubusercontent.com/danielhmills/nflkg/pbp/r2rml.ttl>'
r2rml_insert = "DB.DBA.R2RML_GENERATE_LINKED_VIEW('https://raw.githubusercontent.com/danielhmills/nflkg/pbp/r2rml.ttl', 'http://demo.openlinksw.com/nfl-pbp-kg#',0 ,1)"
r2rml_physical = "RDF_VIEW_SYNC_TO_PHYSICAL ('http://demo.openlinksw.com/nfl-pbp#', 1, 'urn:kg:nfl:data')"
queries = [clear_data,r2rml_qm_drop,r2rml_clear_graph,r2rml_insert]

for y in queries:
    query(y)

