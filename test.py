import os

import rethinkdb as r

conn = r.connect(host=os.getenv('WERCKER_RETHINKDB_HOST', db='test'))

print conn

conn.close()
