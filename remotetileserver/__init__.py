from flask import Flask
from localtileserver.tileserver.blueprint import cache, tileserver

app = Flask(__name__)
cache.init_app(app)
app.register_blueprint(tileserver, url_prefix='/')
app.config.JSONIFY_PRETTYPRINT_REGULAR = True
app.config.SWAGGER_UI_DOC_EXPANSION = "list"
