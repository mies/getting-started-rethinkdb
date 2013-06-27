import os

import rethinkdb as r

print os.getenv('WERCKER_RETHINKDB_HOST')
conn = r.connect(host=os.getenv('WERCKER_RETHINKDB_HOST'), db='test')

print conn

conn.close()
