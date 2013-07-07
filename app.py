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

@app.teardown_request
def teardown_request():
  pass

@app.route("/", methods=['GET'])
def home():
  return render_template('bookmarks.html')

@app.route("/bookmarks", methods=['GET'])
def get_bookmarks():
  pass

@app.route("/bookmarks", methods=['POST'])
def create_bookmark():
  pass

@app.route("/bookmarks/<string:bookmark_id>/", methods=['GET'])
def get_bookmark():
  pass
