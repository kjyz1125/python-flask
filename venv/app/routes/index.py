from app import app
from flask import Flask, jsonify

@app.route('/')
def main():
    return "hello world"


@app.route('/data')
def data():
    data = {"test": "test"}
    return jsonify(data)