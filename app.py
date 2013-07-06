import json
import os

from flask import Flask, jsonify, render_template, request

import rethinkdb as r

def dbSetup():
  conn = r.connect(host=RETHINKDB_HOST, port=RETHINKDB_PORT)
  try:
    r.db_create(DB_NAME).run(conn)
    r.db(DB_NAME).table_create(TABLE_NAME).run(conn)
  except RqlRuntimeError:
    print 'App exists'
  finally:
    conn.close()

app = Flask(__name__)
app.config.from_object(__name__)

@app.before_request
def before_request():
  pass

