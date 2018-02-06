from flask import Flask
from app import app
app.config['JSON_AS_ASCII'] = False


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(8080), debug=True)