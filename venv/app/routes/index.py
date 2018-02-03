from app import app
from flask import Flask, jsonify, render_template

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/data')
def data():
    data = {"test": "test"}
    return jsonify(data)