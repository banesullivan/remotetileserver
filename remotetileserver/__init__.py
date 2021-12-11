from flask import Flask
from localtileserver.tileserver.blueprint import cache, tileserver

app = Flask(__name__)
cache.init_app(app)
app.register_blueprint(tileserver, url_prefix='/')
