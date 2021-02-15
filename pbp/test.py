import pyodbc as db
from query import query, query_nd

q = "SELECT TOP 5 *  FROM nfl.pbp.demo"
query_nd(q)