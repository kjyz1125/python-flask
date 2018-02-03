from app import app
from flask import Flask

@app.route('/')
def main():
    return "hello world"