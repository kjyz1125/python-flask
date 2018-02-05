from app import app
from flask import Flask, jsonify, render_template, json
from app.database import database

@app.route('/')
def main():
    database.init_db()
    query = database.engine.connect().execute('select * from MEMBER').fetchall()

    #return json.dumps([(dict(query.items())) for query in query], ensure_ascii=False)
    return jsonify([(dict(query.items())) for query in query])


@app.route('/data')
def data():
    data = {"test": "test"}
    return jsonify(data)

