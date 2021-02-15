import pyodbc as db
import os
from query import query

#Attach Tables
def attach():
    p = os.listdir('data')
    table = 'nfl.pbp.demo'
    pk = '1,2,3,4,5'
    for c in p:
            q = "select(attach_from_csv('%s', 'nfl-kg/pbp/data/%s', ',', '\n', null, 1,vector(%s)))" % (table,c,pk)
            query(q)
    print("\n\nTest Query:\n\n")        
    query('select top 5 * from %s' % (table) )      

attach()