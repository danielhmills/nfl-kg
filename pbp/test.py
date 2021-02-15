import pyodbc as db
from query import query, query_nd, query_n1

q = "select top 2 * from kg.wine.raw"
query(q)
query_n1("SPARQL CLEAR GRAPH <urn:nfl:kg:pbp>")