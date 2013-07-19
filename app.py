import json
import os

from flask import Flask, jsonify, render_template, request, g, abort

import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError

RETHINKDB_HOST = os.getenv('WERCKER_RETHINKDB_HOST', 'localhost')
RETHINKDB_PORT = os.getenv('WERCKER_RETHINKDB_PORT', 28015)
DB_NAME = 'bookmarksapp'
TABLE_NAME = 'bookmarks'

def dbSetup():
  conn = r.connect(host=RETHINKDB_HOST, port=RETHINKDB_PORT)
  print 'Connection established on %s with port %d' % (RETHINKDB_HOST, RETHINKDB_PORT)
  try:
    r.db_create(DB_NAME).run(conn)
    r.db(DB_NAME).table_create(TABLE_NAME).run(conn)
    print 'Database and table created!'
  except RqlRuntimeError:
    print 'App exists'
  finally:
    print 'Connection closed'
    conn.close()

app = Flask(__name__)
app.config.from_object(__name__)

@app.before_request
def before_request():
  try:
    g.rdb_conn = r.connect(host=RETHINKDB_HOST, port=RETHINKDB_PORT,
        db=DB_NAME)
  except RqlDriverError:
    abort(503, "Unable to create database connection")

@app.teardown_request
def teardown_request(exception):
  try:
    g.rdb_conn.close()
  except AttributeError:
    pass

@app.route("/", methods=['GET'])
def home():
  #return render_template('bookmarks.html')
  result = list(r.table('bookmarks').run(g.rdb_conn))
  return json.dumps(result)

@app.route("/bookmarks", methods=['GET'])
def get_bookmarks():
  result = list(r.table('bookmarks').run(g.rdb_conn))
  return json.dumps(result)

@app.route("/bookmarks", methods=['POST'])
def create_bookmark():
  bookmark = r.table('bookmarks').insert(request.json).run(g.rdb_conn)
  return jsonify(id=bookmark['generated_keys'][0])

@app.route("/bookmarks/<string:bookmark_id>/", methods=['GET'])
def get_bookmark():
  pass

if __name__ == "__main__":
  port = int(os.getenv('PORT', 5000))
  if os.getenv('CI') == 'true':
    dbSetup()
  app.run(host='0.0.0.0', port=port, debug=True)
